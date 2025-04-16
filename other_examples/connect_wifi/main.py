# Wifi example

import network

ssid = "YOUR_WIFI_NAME"
password = "YOUR_WIFI_PASSWORD"

station = network.WLAN(network.STA_IF)
station.active(False)
station.active(True)
station.config(txpower=8.5)
station.connect(ssid, password)

print('Connecting to wifi...')

while station.isconnected() == False:
    print('.')
    time.sleep(1)

print("Connected")
print(station.ifconfig())
