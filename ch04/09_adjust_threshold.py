from adafruit_circuitplayground.express import cpx
import time

cpx.adjust_touch_threshold(200)
while True:
    if cpx.touch_A1:
        print('detected touch')
    time.sleep(0.5)
