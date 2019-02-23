from adafruit_circuitplayground.express import cpx
import time

RAINBOW = [
    0xFF0000,   # red
    0xFFA500,   # orange
    0xFFFF00,   # yellow
    0x00FF00,   # green
    0x0000FF,   # blue
    0x4b0082,   # indigo
    0xEE82EE,   # violet
]

cpx.pixels.brightness = 0.10
cpx.pixels.fill(0x000000)
while True:
    for i, color in enumerate(RAINBOW):
        cpx.pixels[i] = color
        time.sleep(0.2)
    for i in range(len(RAINBOW)):
        cpx.pixels[i] = 0x000000
        time.sleep(0.2)
