from machine import Pin
import time

red = Pin(0, Pin.OUT)
blue = Pin(2, Pin.OUT)
while True:
    blue.value(0)
    red.value(1)
    time.sleep(1)
    blue.value(1)
    red.value(0)
    time.sleep(1)
