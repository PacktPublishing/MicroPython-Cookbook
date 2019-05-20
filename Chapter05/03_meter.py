from adafruit_circuitplayground.express import cpx
import time

BLACK = 0x000000
BLUE = 0x0000FF
MAX_LUX = 330
cpx.pixels.brightness = 0.10


def gauge(level):
    cpx.pixels[0:level] = [BLUE] * level


last = 0
while True:
    level = int((cpx.light / MAX_LUX) * 10)
    if level != last:
        cpx.pixels.fill(BLACK)
        gauge(level)
        last = level
    time.sleep(0.05)
