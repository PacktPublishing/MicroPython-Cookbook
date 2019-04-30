import board
import busio


def main():
    i2c = busio.I2C(board.SCL, board.SDA)
    while not i2c.try_lock():
        print('getting lock...')
    devices = [hex(x) for x in i2c.scan()]
    print('devices found:', devices)


main()
