from adafruit_circuitplayground.express import cpx

while True:
    if cpx.button_a:
        cpx.play_tone(500, 0.2)
    if cpx.button_b:
        cpx.play_tone(900, 0.2)
