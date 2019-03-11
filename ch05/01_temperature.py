from adafruit_circuitplayground.express import cpx
import time

start = time.monotonic()
while True:
    elapsed = time.monotonic() - start
    temp = cpx.temperature
    print('{elapsed:.2f}\t{temp}'.format(**locals()))
    time.sleep(0.1)
