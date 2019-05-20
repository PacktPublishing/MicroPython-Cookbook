from microbit import display, button_a
import time

NUMBERS = list(range(9, 0, -1))


def countdown():
    for i in NUMBERS:
        display.show(i)
        time.sleep(1)
    display.clear()


while True:
    if button_a.is_pressed():
        countdown()
