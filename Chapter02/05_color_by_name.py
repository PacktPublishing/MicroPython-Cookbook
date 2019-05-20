from adafruit_circuitplayground.express import cpx

RGB = dict(black=0x000000, blue=0x0000FF, green=0x00FF00, cyan=0x00FFFF,
           red=0xFF0000, magenta=0xFF00FF, yellow=0xFFFF00, white=0xFFFFFF)
cpx.pixels[0] = RGB['red']

for i, name in enumerate(sorted(RGB)):
    cpx.pixels[i] = RGB[name]
