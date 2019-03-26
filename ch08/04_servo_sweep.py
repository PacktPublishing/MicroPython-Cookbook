import time
from adafruit_circuitplayground.express import cpx
from adafruit_crickit import crickit

MIN_PULSE = 750
MAX_PULSE = 2250
MAX_ANGLE = 160
STEP = 10
DELAY = 0.1


def init(servo):
    servo.set_pulse_width_range(MIN_PULSE, MAX_PULSE)
    servo.angle = 0
    servo.actuation_range = MAX_ANGLE


def sweep(servo, direction):
    angle = int(servo.angle)
    while 0 <= angle <= MAX_ANGLE:
        print(angle)
        servo.angle = angle
        time.sleep(DELAY)
        angle += STEP * direction


def main():
    init(crickit.servo_1)
    while True:
        sweep(crickit.servo_1, 1)
        sweep(crickit.servo_1, -1)


main()
