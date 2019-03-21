from digitalio import DigitalInOut
import board


def enable_speakers():
    speaker_control = DigitalInOut(board.SPEAKER_ENABLE)
    speaker_control.switch_to_output(value=True)


enable_speakers()
