from adafruit_circuitplayground.express import cpx
import time

while True:
    x, y, z = cpx.acceleration
    print('x: {x:.2f} y: {y:.2f} z: {z:.2f}'.format(**locals()))
    time.sleep(0.1)
