from adafruit_circuitplayground.express import cpx
import time

while True:
    if cpx.shake(20):
        cpx.play_tone(900, 0.2)
    time.sleep(0.1)
