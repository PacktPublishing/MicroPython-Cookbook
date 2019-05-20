import os

FILE_CODE = 0x8000


def isfile(path):
    return os.stat(path)[0] == FILE_CODE


def main():
    files = [i for i in sorted(os.listdir()) if isfile(i)]
    print('files:', files)
    dirs = [i for i in sorted(os.listdir()) if not isfile(i)]
    print('dirs:', dirs)


main()
