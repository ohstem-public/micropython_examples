# Wifi example

import network

ssid = "YOUR_WIFI_NAME"
password = "YOUR_WIFI_PASSWORD"

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

print('Connecting to wifi...')

while station.isconnected() == False:
    print('.')
    time.sleep(0.1)

print("Connected")
print(station.ifconfig())
