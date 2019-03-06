import time
import touchio
import board

a1 = touchio.TouchIn(board.A1)
while True:
    touch = a1.raw_value > a1.threshold
    print('raw:', a1.raw_value, 'threshold:', a1.threshold, 'touch:', touch)
    time.sleep(0.5)
