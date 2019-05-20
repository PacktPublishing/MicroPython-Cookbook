from adafruit_circuitplayground.express import cpx


class ButtonEvent:
    def __init__(self, name):
        self.name = name
        self.last = False

    def is_pressed(self):
        pressed = getattr(cpx, self.name)
        changed = (pressed != self.last)
        self.last = pressed
        return (pressed and changed)


button = ButtonEvent('button_a')
while True:
    if button.is_pressed():
        print('button A pressed')
