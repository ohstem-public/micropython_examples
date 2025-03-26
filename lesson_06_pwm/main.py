# Example using PWM to fade an LED using rotary

import time
from machine import Pin, PWM, ADC

led_pwm = PWM(Pin(48), freq=1000, duty=0)

adc_input = ADC(Pin(1))  # create ADC instance on GPIO1
adc_input.atten(ADC.ATTN_11DB) # ADC range max input 3.3V

while True:
  sensor_value = adc_input.read()
  pwm_value = (int) (1023*sensor_value/4095)
  led_pwm.duty(pwm_value)
  time.sleep_ms(100)