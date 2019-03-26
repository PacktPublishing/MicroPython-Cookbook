from adafruit_crickit import crickit
import time

while True:
    crickit.dc_motor_1.throttle = 1
    time.sleep(1)
    crickit.dc_motor_1.throttle = 0
    time.sleep(1)
