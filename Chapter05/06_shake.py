from adafruit_circuitplayground.express import cpx
import time

while True:
    print('shake detected:', cpx.shake())
    time.sleep(0.1)
