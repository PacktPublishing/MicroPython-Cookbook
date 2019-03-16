from button import ButtonEvent


def main():
    buttons = {1: ButtonEvent('button_a'), 2: ButtonEvent('button_b')}
    while True:
        for player, button in buttons.items():
            if button.is_pressed():
                print('button pressed for player', player)


main()
