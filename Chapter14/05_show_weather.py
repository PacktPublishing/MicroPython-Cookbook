from screen import Screen, get_oled
from netcheck import wait_for_networking
import urequests
import json

CONF_PATH = 'conf.json'
API_URL = 'http://api.openweathermap.org/data/2.5/weather'
CITIES = ['Berlin', 'London', 'Paris', 'Tokyo', 'Rome', 'Oslo', 'Bangkok']
WEATHER = """\
City: {city}
Temp: {temp}
Wind: {wind}
"""


def get_conf():
    content = open(CONF_PATH).read()
    return json.loads(content)


def get_weather(APPID, city):
    url = API_URL + '?units=metric&APPID=' + APPID + '&q=' + city
    return urequests.get(url).json()


def show_weather(screen, APPID, city):
    weather = get_weather(APPID, city)
    data = {}
    data['city'] = city
    data['temp'] = weather['main']['temp']
    data['wind'] = weather['wind']['speed']
    text = WEATHER.format(**data)
    print('-------- %s --------' % city)
    print(text)
    screen.write(text)


def main():
    oled = get_oled()
    screen = Screen(oled)
    wait_for_networking()
    conf = get_conf()
    APPID = conf['APPID']
    for city in CITIES:
        show_weather(screen, APPID, city)


main()
