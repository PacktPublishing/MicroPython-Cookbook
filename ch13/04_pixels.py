import adafruit_ssd1306
import board
import busio

BLACK = 0
WHITE = 1


def animate_pixel(oled, x, y, step_x, step_y, count):
    for i in range(count):
        x += step_x
        y += step_y
        oled.pixel(x, y, WHITE)
        oled.show()


def zig_zag(oled):
    animate_pixel(oled, x=0, y=0, step_x=1, step_y=1, count=30)
    animate_pixel(oled, x=30, y=30, step_x=1, step_y=-1, count=30)
    animate_pixel(oled, x=60, y=0, step_x=1, step_y=1, count=30)
    animate_pixel(oled, x=90, y=30, step_x=1, step_y=-1, count=30)


def main():
    i2c = busio.I2C(board.SCL, board.SDA)
    oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
    zig_zag(oled)


main()
