BLACK = 0x000000
SEQUENCE = [
    0xFFFF00,   # Yellow
    0xFF8C00,   # DarkOrange
    0xFF0000,   # Red
    0xFF00FF,   # Magenta
]
PLAYER_PIXELS1 = [0, 1, 2, 3, 4]
PLAYER_PIXELS2 = [9, 8, 7, 6, 5]


def generate_colors(positions):
    yield 0, BLACK
    for i in positions:
        for color in SEQUENCE:
            yield i, color


COLORS = dict()
COLORS[1] = list(generate_colors(PLAYER_PIXELS1))
COLORS[2] = list(generate_colors(PLAYER_PIXELS2))
