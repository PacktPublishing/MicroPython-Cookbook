from adafruit_circuitplayground.express import cpx
import time

while True:
    if cpx.touch_A1:
        print('detected touch')
    time.sleep(0.05)
