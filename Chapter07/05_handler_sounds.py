from touchio import TouchIn
from digitalio import DigitalInOut
from audioio import WaveFile, AudioOut
import board


def enable_speakers():
    speaker_control = DigitalInOut(board.SPEAKER_ENABLE)
    speaker_control.switch_to_output(value=True)


def play_file(speaker, path):
    file = open(path, "rb")
    audio = WaveFile(file)
    speaker.play(audio)


class Handler:
    def __init__(self, speaker):
        self.speaker = speaker

    def handle(self, name, state):
        if state:
            play_file(self.speaker, 'piano.wav')


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
handler = Handler(speaker)
event = TouchEvent('A1', handler.handle)
while True:
    event.process()
