import board
import time


def fade_in():
    for i in range(0, 11):
        brightness = i / 10
        print('brightness:', brightness)
        board.DISPLAY.brightness = brightness
        time.sleep(0.1)


def main():
    while True:
        fade_in()


main()
