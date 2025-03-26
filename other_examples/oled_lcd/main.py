# OLED I2C example

import time
from machine import Pin, SoftI2C
import ssd1306
import dht

d = dht.DHT11(machine.Pin(6))

# ESP32 Pin assignment 
i2c = SoftI2C(scl=Pin(SCL_PIN), sda=Pin(SDA_PIN), freq=100000)

oled = ssd1306.SSD1306_I2C(128, 64, i2c) # OLED 128x64

while True:
  d.measure()
  oled.text('Temp:     %.1f' % d.temperature(), 0, 20)
  oled.text('Humidity: %.1f' % d.humidity(), 0, 50)
  oled.show()
  time.sleep(5)