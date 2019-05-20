import os

FILE_CODE = 0x8000


def isfile(path):
    return os.stat(path)[0] == FILE_CODE


def any_remove(path):
    func = os.remove if isfile(path) else os.rmdir
    func(path)
