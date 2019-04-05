import network
ap = network.WLAN(network.AP_IF)
ap.config(essid='PyWifi', password='12345678')
ap.active(True)
ap.ifconfig()
