# Read ADC input

import time
from machine import Pin, ADC

led = Pin(48, Pin.OUT)

adc_input = ADC(Pin(1))
adc_input.atten(ADC.ATTN_11DB) # ADC range max input 3.3V

while True:
  sensor_value = adc_input.read()
  print(sensor_value)
  led.on()
  time.sleep_ms(sensor_value)
  led.off()
  time.sleep_ms(sensor_value)
