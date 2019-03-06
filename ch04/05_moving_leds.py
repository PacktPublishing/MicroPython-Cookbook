from adafruit_circuitplayground.express import cpx
import time

BLACK = 0x000000
BLUE = 0x0000FF

cpx.pixels.brightness = 0.10
i = 0
direction = 1
while True:
    if cpx.button_a:
        direction = 1
    if cpx.button_b:
        direction = -1
    i += direction
    i = i % 10
    cpx.pixels.fill(BLACK)
    cpx.pixels[i] = BLUE
    time.sleep(0.05)
