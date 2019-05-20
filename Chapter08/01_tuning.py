import time
from adafruit_circuitplayground.express import cpx
from adafruit_crickit import crickit

MIN_PULSE = 750
MAX_PULSE = 2250

crickit.servo_1.set_pulse_width_range(MIN_PULSE, MAX_PULSE)
crickit.servo_1.angle = 0
time.sleep(3)
crickit.servo_1.angle = 90
time.sleep(60)
