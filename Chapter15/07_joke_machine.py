from displayio import OnDiskBitmap, ColorConverter, TileGrid, Group
import board
import random
import time
import touchio
import os


def show_image(path):
    print('showing image', path)
    with open(path, 'rb') as f:
        bitmap = OnDiskBitmap(f)
        pixel_shader = ColorConverter()
        sprite = TileGrid(bitmap, pixel_shader=pixel_shader)
        group = Group()
        group.append(sprite)
        board.DISPLAY.show(group)
        board.DISPLAY.wait_for_frame()


def wait_for_touch(touch):
    while not touch.value:
        print('waiting...')
        time.sleep(0.1)


def get_questions():
    paths = sorted(os.listdir())
    return [i for i in paths if i.endswith('question.bmp')]


def main():
    touch = touchio.TouchIn(board.TOUCH1)
    questions = get_questions()
    while True:
        question = random.choice(questions)
        response = question.replace('question.bmp', 'response.bmp')
        show_image(question)
        wait_for_touch(touch)
        show_image(response)
        wait_for_touch(touch)


main()
