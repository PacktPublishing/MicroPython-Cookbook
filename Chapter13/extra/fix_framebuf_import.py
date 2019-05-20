import os
import sys

OLD_CODE = 'import framebuf'
NEW_CODE = 'import adafruit_framebuf as framebuf'


def main():
    assert sys.version_info.major >= 3, 'Python 3 or above required'
    os.rename('adafruit_ssd1306.py', 'old_adafruit_ssd1306.py')
    old = open('old_adafruit_ssd1306.py').read()
    new = old.replace(OLD_CODE, NEW_CODE)
    with open('adafruit_ssd1306.py', 'w') as f:
        f.write(new)

main()
