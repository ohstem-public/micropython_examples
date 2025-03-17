# DHT20 example

import machine, time
from dht20 import DHT20

i2c = machine.SoftI2C(scl=machine.Pin(SCL_PIN), sda=machine.Pin(SDA_PIN))
dht20 = DHT20(i2c)

while True:
  temper = dht20.temperature()
  humidity = dht20.humidity()
  print("temperature: " + str(temper))
  print("humidity   : " + str(humidity))
  time.sleep(2)