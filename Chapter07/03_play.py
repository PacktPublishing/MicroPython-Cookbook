from digitalio import DigitalInOut
from audioio import WaveFile, AudioOut
import board
import time


def play_file(speaker, path):
    file = open(path, "rb")
    audio = WaveFile(file)
    speaker.play(audio)


def enable_speakers():
    speaker_control = DigitalInOut(board.SPEAKER_ENABLE)
    speaker_control.switch_to_output(value=True)


enable_speakers()
speaker = AudioOut(board.SPEAKER)
play_file(speaker, 'piano.wav')
time.sleep(100)
