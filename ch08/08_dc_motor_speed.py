from adafruit_crickit import crickit
import time

DELAY = 0.1


def change_throttle(motor, start, increment):
    throttle = start
    for i in range(21):
        print(throttle)
        motor.throttle = throttle
        throttle += increment
        throttle = round(throttle, 1)
        time.sleep(DELAY)


def main():
    while True:
        change_throttle(crickit.dc_motor_1, -1.0, 0.1)
        change_throttle(crickit.dc_motor_1, 1.0, -0.1)


main()
