import adafruit_ssd1306
import board
import busio


def main():
    i2c = busio.I2C(board.SCL, board.SDA)
    oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
    for i in range(10):
        oled.fill(1)
        oled.show()
        oled.fill(0)
        oled.show()


main()
