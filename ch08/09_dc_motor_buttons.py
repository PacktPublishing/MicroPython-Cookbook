from adafruit_crickit import crickit
from adafruit_circuitplayground.express import cpx
import time

STEP = 0.1
DELAY = 0.1
MIN_THROTTLE = -1
MAX_THROTTLE = 1


def move(motor, throttle, direction):
    new = throttle + STEP * direction
    if MIN_THROTTLE <= new <= MAX_THROTTLE:
        throttle = round(new, 1)
        print(throttle)
        motor.throttle = throttle
    return throttle


def main():
    throttle = 0
    while True:
        if cpx.button_a:
            throttle = move(crickit.dc_motor_1, throttle, 1)
        if cpx.button_b:
            throttle = move(crickit.dc_motor_1, throttle, -1)
        time.sleep(DELAY)


main()
