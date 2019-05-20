from netcheck import wait_for_networking
import urequests
import time

ISS_API_URL = 'http://api.open-notify.org/iss-now.json'


def track_space_station():
    for i in range(10):
        data = urequests.get(ISS_API_URL).json()
        position = data['iss_position']
        print(i, 'lat: {latitude} long: {longitude}'.format(**position))
        time.sleep(1)


def main():
    wait_for_networking()
    track_space_station()

main()
