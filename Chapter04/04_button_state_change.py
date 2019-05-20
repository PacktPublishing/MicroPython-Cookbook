from adafruit_circuitplayground.express import cpx


def button_change(pressed):
    print('pressed:', pressed)


last = cpx.button_a
while True:
    if cpx.button_a != last:
        button_change(cpx.button_a)
        last = cpx.button_a
