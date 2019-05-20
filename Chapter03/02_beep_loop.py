from adafruit_circuitplayground.express import cpx
for i in range(500, 1000, 100):
    print(i)
    cpx.play_tone(i, 0.2)


for i in range(200, 500, 100):
    print(i)
    cpx.play_tone(i, i / 1000)
