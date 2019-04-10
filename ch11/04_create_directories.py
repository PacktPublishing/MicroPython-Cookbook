import os


def exists(path):
    try:
        os.stat(path)
    except OSError:
        return False
    return True


def mkdir_safe(path):
    if not exists(path):
        os.mkdir(path)


def makedirs(path):
    items = path.strip('/').split('/')
    count = len(items)
    paths = ['/' + '/'.join(items[0:i + 1]) for i in range(count)]
    for path in paths:
        os.mkdir(path)
