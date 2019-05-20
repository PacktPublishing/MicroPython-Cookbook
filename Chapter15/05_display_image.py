import board
from displayio import OnDiskBitmap, ColorConverter, TileGrid, Group


IMAGES = ['joke_01_question.bmp', 'joke_01_response.bmp']


def show_image(path):
    with open(path, 'rb') as f:
        bitmap = OnDiskBitmap(f)
        pixel_shader = ColorConverter()
        sprite = TileGrid(bitmap, pixel_shader=pixel_shader)
        group = Group()
        group.append(sprite)
        board.DISPLAY.show(group)
        board.DISPLAY.wait_for_frame()


def main():
    while True:
        for image in IMAGES:
            show_image(image)


main()
