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


def move(servo, angle, direction):
    new = angle + STEP * direction
    if 0 <= new <= MAX_ANGLE:
        angle = new
        print(angle)
        servo.angle = angle
    return angle


def main():
    servos = [crickit.servo_1, crickit.servo_4]
    angles = [0, 0]
    init(servos[0])
    init(servos[1])
    while True:
        switch = int(cpx.switch)
        if cpx.button_a:
            angles[switch] = move(servos[switch], angles[switch], 1)
        if cpx.button_b:
            angles[switch] = move(servos[switch], angles[switch], -1)
        time.sleep(DELAY)


main()
