from adafruit_circuitplayground.express import cpx

BEEP_HIGH = 960
BEEP_LOW = 800

for i in range(3):
    cpx.play_tone(BEEP_HIGH, 0.5)
    cpx.play_tone(BEEP_LOW, 0.5)
