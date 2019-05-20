import urequests

API_URL = 'http://api.openweathermap.org/data/2.5/weather'

APPID = 'put-your-API-key(APPID)-here'
city = 'Berlin'
url = API_URL + '?units=metric&APPID=' + APPID + '&q=' + city

response = urequests.get(url)
response
data = response.json()
len(data)

data['main']
data['main']['temp']
data['main']['humidity']
data['wind']
data['wind']['speed']
