from touchio import TouchIn
from digitalio import DigitalInOut
from audioio import WaveFile, AudioOut
from neopixel import NeoPixel
import board

PIXEL_COUNT = 10
TOUCH_PADS = ['A1', 'A2', 'A5', 'A6']
SOUND = dict(
    A1='hit.wav',
    A2='piano.wav',
    A5='tin.wav',
    A6='wood.wav',
)
RGB = dict(
    black=0x000000,
    white=0xFFFFFF,
    green=0x00FF00,
    red=0xFF0000,
    yellow=0xFFFF00,
)
PIXELS = dict(
    A1=(6, RGB['white']),
    A2=(8, RGB['red']),
    A5=(1, RGB['yellow']),
    A6=(3, RGB['green']),
)


def play_file(speaker, path):
    file = open(path, "rb")
    audio = WaveFile(file)
    speaker.play(audio)


def enable_speakers():
    speaker_control = DigitalInOut(board.SPEAKER_ENABLE)
    speaker_control.switch_to_output(value=True)


class Handler:
    def __init__(self, speaker, pixels):
        self.speaker = speaker
        self.pixels = pixels

    def handle(self, name, state):
        pos, color = PIXELS[name]
        if state:
            play_file(self.speaker, SOUND[name])
            self.pixels[pos] = color
        else:
            self.pixels[pos] = RGB['black']


class TouchEvent:
    THRESHOLD_ADJUSTMENT = 400

    def __init__(self, name, onchange):
        self.name = name
        self.last = False
        self.onchange = onchange
        pin = getattr(board, name)
        self.touch = TouchIn(pin)
        self.touch.threshold += self.THRESHOLD_ADJUSTMENT

    def process(self):
        current = self.touch.value
        if current != self.last:
            self.onchange(self.name, current)
            self.last = current


def main():
    enable_speakers()
    speaker = AudioOut(board.SPEAKER)
    pixels = NeoPixel(board.NEOPIXEL, PIXEL_COUNT)
    pixels.brightness = 0.05
    handler = Handler(speaker, pixels)
    events = [TouchEvent(i, handler.handle) for i in TOUCH_PADS]
    while True:
        for event in events:
            event.process()


main()
