from touchio import TouchIn
from digitalio import DigitalInOut
from audioio import WaveFile, AudioOut
from neopixel import NeoPixel
import board

PIXEL_COUNT = 10


def enable_speakers():
    speaker_control = DigitalInOut(board.SPEAKER_ENABLE)
    speaker_control.switch_to_output(value=True)


def play_file(speaker, path):
    file = open(path, "rb")
    audio = WaveFile(file)
    speaker.play(audio)


class Handler:
    def __init__(self, speaker, pixels):
        self.speaker = speaker
        self.pixels = pixels

    def handle(self, name, state):
        if state:
            play_file(self.speaker, 'piano.wav')
            self.pixels[0] = 0xFF0000
        else:
            self.pixels[0] = 0x000000


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


enable_speakers()
speaker = AudioOut(board.SPEAKER)
pixels = NeoPixel(board.NEOPIXEL, PIXEL_COUNT)
pixels.brightness = 0.05
handler = Handler(speaker, pixels)
event = TouchEvent('A1', handler.handle)
while True:
    event.process()
