import adafruit_ssd1306
import board
import busio

BLACK = 0
WHITE = 1


class Screen:
    def __init__(self, oled):
        self.oled = oled
        self.oled.fill(BLACK)
        self.oled.show()

    def write(self, text):
        self.oled.fill(BLACK)
        lines = text.strip().split('\n')
        for row, line in enumerate(lines):
            self.oled.text(line, 0, 10 * row, WHITE)
        self.oled.show()


def get_oled():
    i2c = busio.I2C(board.SCL, board.SDA)
    return adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
