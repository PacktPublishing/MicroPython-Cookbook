from adafruit_circuitplayground.express import cpx
cpx.pixels[0:2] = [0xFF0000, 0xFF0000]

cpx.pixels[2:5] = [0x00FF00] * 3
cpx.pixels[5:10] = [0x0000FF] * 5
