# LCD 1602 I2C example

import time
from machine import Pin, SoftI2C
from lcd_1602 import LCD1602

SCL_PIN = 22
SDA_PIN = 21

i2c = SoftI2C(scl=Pin(SCL_PIN), sda=Pin(SDA_PIN), freq=100000)
lcd = LCD1602(i2c, addr=0x21)

lcd.backlight_on()

while True:
  lcd.move_to(0, 0)
  lcd.putstr('OhStem')
   
  lcd.move_to(0, 1)
  lcd.putstr('Xin chao ban')
  time.sleep(2)
  
  lcd.clear()
  time.sleep(1)