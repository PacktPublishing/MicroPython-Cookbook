import adafruit_ssd1306
import board
import busio

BLACK = 0
WHITE = 1
ALPHA_NUMERIC = [
    'abcdefghijklmnopqrstu',
    'vwxyzABCDEFGHIJKLMNOP',
    'QRSTUVWXYZ0123456789',
]


def countdown(oled, start):
    for i in range(start, -1, -1):
        oled.fill(BLACK)
        oled.text(str(i), 0, 0, WHITE)
        oled.show()


def show_alpha_numeric(oled):
    for i, text in enumerate(ALPHA_NUMERIC):
        oled.text(text, 0, 10 * i, WHITE)
        oled.show()


def main():
    i2c = busio.I2C(board.SCL, board.SDA)
    oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
    oled.fill(BLACK)
    countdown(oled, 10)
    oled.fill(BLACK)
    show_alpha_numeric(oled)


main()
