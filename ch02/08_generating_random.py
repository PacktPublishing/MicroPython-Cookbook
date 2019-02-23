from adafruit_circuitplayground.express import cpx
from random import randint

randint(0, 255)


def get_random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


get_random_color()


cpx.pixels[0] = get_random_color()


cpx.pixels.fill(get_random_color())
