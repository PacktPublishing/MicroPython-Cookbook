from machine import Pin
import time

PINS = dict(a=0, b=16, c=2)


def format(name, buttons):
    pressed = not buttons[name].value()
    return '{name}: {pressed}'.format(name=name, pressed=pressed)


def get_status(names, buttons):
    items = [format(i, buttons) for i in names]
    return ' '.join(items)


def get_buttons():
    return dict(
        a=Pin(PINS['a'], Pin.IN, Pin.PULL_UP),
        b=Pin(PINS['b']),
        c=Pin(PINS['c'], Pin.IN, Pin.PULL_UP),
    )


def main():
    names = sorted(PINS.keys())
    buttons = get_buttons()
    while True:
        status = get_status(names, buttons)
        print(status)
        time.sleep(0.1)


main()
