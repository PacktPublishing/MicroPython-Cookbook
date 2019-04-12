from netcheck import wait_for_networking
import urequests


def main():
    wait_for_networking()
    url = 'http://micropython.org/ks/test.html'
    html = urequests.get(url).text
    print(html)


main()
