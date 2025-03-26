# DHT20 and LCD 1602 I2C example

import time
from machine import Pin, ADC
from servo import Servo

adc_input = ADC(Pin(1))  # create ADC instance on GPIO1
adc_input.atten(ADC.ATTN_11DB) # ADC range max input 3.3V

servo = Servo(5)

while True:
  sensor_value = adc_input.read()
  angle = int(180*(sensor_value/4095))
  servo.turn(angle)
  time.sleep_ms(100)