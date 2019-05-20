from adafruit_circuitplayground.express import cpx

BLACK = 0x000000
GREEN = 0x00FF00

cpx.pixels.brightness = 0.10
while True:
    cpx.pixels[2] = GREEN if cpx.button_a else BLACK
    cpx.pixels[7] = GREEN if cpx.button_b else BLACK
