from microbit import display, Image
import time

CLOCK = [getattr(Image, 'CLOCK%s' % i) for i in range(1, 13)]
while True:
    for image in CLOCK:
        display.show(image)
        time.sleep(0.1)
