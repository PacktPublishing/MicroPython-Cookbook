import network
station = network.WLAN(network.STA_IF)

station.active(True)

networks = station.scan()

len(networks)
names = [i[0] for i in networks]
