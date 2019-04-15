from netcheck import wait_for_networking
import urequests
import json

CONF_PATH = 'conf.json'
API_URL = 'http://api.openweathermap.org/data/2.5/weather'


def get_conf():
    content = open(CONF_PATH).read()
    return json.loads(content)


def get_weather(APPID, city):
    url = API_URL + '?units=metric&APPID=' + APPID + '&q=' + city
    return urequests.get(url).json()


def main():
    wait_for_networking()
    conf = get_conf()
    APPID = conf['APPID']
    data = get_weather(APPID, 'London')
    print('temp:', data['main']['temp'])
    print('wind:', data['wind']['speed'])
    print('name:', data['name'])
    print('country:', data['sys']['country'])


main()
