from microbit import display

TEXT = [
    ('slow', 300),
    ('normal', 150),
    ('fast', 75),

]

for text, delay in TEXT:
    display.scroll(text, delay=delay)
