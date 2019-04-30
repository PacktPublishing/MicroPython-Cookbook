from adafruit_lis3dh import LIS3DH_I2C
import board
import busio
import time

ACCEL_ADDRESS = 0x18


def main():
    i2c = busio.I2C(board.SCL, board.SDA)
    accel = LIS3DH_I2C(i2c, address=ACCEL_ADDRESS)
    while True:
        face = 'up' if accel.acceleration.z < 0 else 'down'
        print('board is face', face)
        time.sleep(0.1)


main()
