from button import ButtonEvent

button = ButtonEvent('button_a')
while True:
    if button.is_pressed():
        print('button A pressed')
