from microbit import display, button_a, button_b

while True:
    if button_a.is_pressed():
        display.show('a')
    elif button_b.is_pressed():
        display.show('b')
    else:
        display.clear()
