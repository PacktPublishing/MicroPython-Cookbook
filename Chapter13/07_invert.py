import adafruit_ssd1306
import board
import busio
import time

BLACK = 0
WHITE = 1


def measure_time(label, func, args=(), count=3):
    for i in range(count):
        start = time.monotonic()
        func(*args)
        total = (time.monotonic() - start) * 1000
        print(label + ':', '%s ms' % total)


def main():
    i2c = busio.I2C(board.SCL, board.SDA)
    oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
    oled.fill(BLACK)
    oled.show()

    measure_time('fill', oled.fill, [BLACK])
    measure_time('show', oled.show, [])
    measure_time('text', oled.text, ['hello', 0, 0, WHITE])
    measure_time('invert', oled.invert, [True])


main()
