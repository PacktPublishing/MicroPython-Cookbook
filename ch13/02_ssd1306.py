import adafruit_ssd1306
import board
import busio


def main():
    print('initialize I2C bus')
    i2c = busio.I2C(board.SCL, board.SDA)
    print('create SSD1306_I2C object')
    oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
    print('ALL DONE')


main()
