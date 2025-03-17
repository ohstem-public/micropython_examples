# DHT example

import time
import machine
import dht

d = dht.DHT11(machine.Pin(6))
#d = dht.DHT22(machine.Pin(4))

while True:
  d.measure()
  print('Temperature: %.1f' % d.temperature())
  print('Humidity: %.1f' % d.humidity())
  time.sleep(1)