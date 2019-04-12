from netcheck import wait_for_networking


def main():
    ip = wait_for_networking()
    print('main started')
    print('device ip:', ip)


main()
