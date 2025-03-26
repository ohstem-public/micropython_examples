# DHT20 and LCD 1602 I2C example

import time
from machine import Pin, SoftI2C
from lcd_1602 import LCD1602
from dht_20 import DHT20

SCL_PIN = 6
SDA_PIN = 5

i2c = SoftI2C(scl=Pin(SCL_PIN), sda=Pin(SDA_PIN), freq=100000)

lcd = LCD1602(i2c, addr=0x21)
dht_sensor = DHT20(i2c)

lcd.backlight_on()

while True:
  dht_sensor.read()
  lcd.clear()
  lcd.move_to(0, 0)
  lcd.putstr('Nhiet do: ' + str(dht_sensor.temperature()) + '*C')
  lcd.move_to(0, 1)
  lcd.putstr('Do am:    ' + str(dht_sensor.humidity()) + '%')
  time.sleep(3)
