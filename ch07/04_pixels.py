from neopixel import NeoPixel
import board

PIXEL_COUNT = 10
RGB = dict(
    black=0x000000,
    white=0xFFFFFF,
    green=0x00FF00,
    red=0xFF0000,
    yellow=0xFFFF00,
)

pixels = NeoPixel(board.NEOPIXEL, PIXEL_COUNT)
pixels.brightness = 0.05
pixels[0] = RGB['red']
pixels[1] = RGB['green']

while True:
    pass
