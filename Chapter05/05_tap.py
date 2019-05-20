from adafruit_circuitplayground.express import cpx
import time

cpx.detect_taps = 1
while True:
    print('tap detected:', cpx.tapped)
    time.sleep(0.1)
