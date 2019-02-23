from adafruit_circuitplayground.express import cpx
from random import randint
import time


def get_random_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


for i in range(10):
    cpx.pixels[i] = get_random_color()
    time.sleep(1)


cpx.pixels.fill(0x000000)
for cycle in range(3):
    for i in range(10):
        cpx.pixels[i] = get_random_color()
        time.sleep(1)


cpx.pixels.fill(0x000000)
for i in range(5):
    cpx.pixels.fill(get_random_color())
    time.sleep(1)
