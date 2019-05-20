import network
station = network.WLAN(network.STA_IF)
station.active(True)
networks = station.scan()
names = [i[0] for i in networks]

station.connect('MyAmazingWiFi', 'MyAmazingPassword')
station.isconnected()
station.ifconfig()
station.active(False)
