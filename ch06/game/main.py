from button import ButtonEvent
from score import ScoreBoard


def main():
    buttons = {1: ButtonEvent('button_a'), 2: ButtonEvent('button_b')}
    board = ScoreBoard()
    while True:
        for player, button in buttons.items():
            if button.is_pressed():
                board.scored(player)


main()
