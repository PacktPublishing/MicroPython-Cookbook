from adafruit_circuitplayground.express import cpx
from colors import COLORS


class ScoreBoard:
    def __init__(self):
        self.score = {1: 0, 2: 0}
        cpx.pixels.brightness = 0.02
        cpx.play_file('start.wav')

    def scored(self, player):
        self.score[player] += 1
        self.show(player)
        if self.score[player] == 20:
            cpx.play_file('win%s.wav' % player)

    def show(self, player):
        score = self.score[player]
        pos, color = COLORS[player][score]
        cpx.pixels[pos] = color
