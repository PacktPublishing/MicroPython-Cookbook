from screen import Screen, get_oled

MESSAGE = """\
top line %s
middle line
last line
"""


def main():
    oled = get_oled()
    screen = Screen(oled)
    screen.write('hello')

    for i in range(10):
        print(i)
        screen.write(MESSAGE % i)


main()
