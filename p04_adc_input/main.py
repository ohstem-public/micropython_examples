# Read ADC input

import time
from machine import Pin, ADC

adc_input = ADC(Pin(1))  # create ADC instance on GPIO6
adc_input.atten(ADC.ATTN_11DB) # ADC range max input 3.3V
adc_input.width(ADC.WIDTH_12BIT) # ADC max value 4095

while True:
  print(adc_input.read())
  time.sleep_ms(100)
