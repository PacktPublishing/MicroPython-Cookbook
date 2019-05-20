import os
import sys

OLD_CODE = 'usocket.getaddrinfo(host, port, 0, usocket.SOCK_STREAM)'
NEW_CODE = 'usocket.getaddrinfo(host, port)'


def main():
    assert sys.version_info.major >= 3, 'Python 3 or above required'
    os.rename('urequests.py', 'old_urequests.py')
    old = open('old_urequests.py').read()
    new = old.replace(OLD_CODE, NEW_CODE)
    with open('urequests.py', 'w') as f:
        f.write(new)

main()
