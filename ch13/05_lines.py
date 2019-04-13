import adafruit_ssd1306
import board
import busio

BLACK = 0
WHITE = 1


def draw_hi(oled):
    print('drawing H')
    oled.vline(x=50, y=0, height=30, color=WHITE)
    oled.hline(x=50, y=15, width=30, color=WHITE)
    oled.vline(x=80, y=0, height=30, color=WHITE)
    oled.show()
    print('drawing I')
    oled.vline(x=100, y=0, height=30, color=WHITE)
    oled.show()


def animate_boxes(oled, x, y, step_x, step_y, size, count):
    for i in range(count):
        oled.rect(x, y, width=size, height=size, color=WHITE)
        oled.show()
        x += step_x
        y += step_y


def draw_x_boxes(oled):
    animate_boxes(oled, x=0, y=0, step_x=5, step_y=5, size=5, count=6)
    animate_boxes(oled, x=0, y=25, step_x=5, step_y=-5, size=5, count=6)


def main():
    i2c = busio.I2C(board.SCL, board.SDA)
    oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
    draw_x_boxes(oled)
    draw_hi(oled)


main()
