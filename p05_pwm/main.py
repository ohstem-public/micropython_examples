# Example using PWM to fade an LED.

import time
from machine import Pin, PWM

led_pwm = PWM(Pin(48), freq=1000, duty=0)

while True:
	for i in range(1023):
		led_pwm.duty(i)
		time.sleep_ms(1)

	for i in range(1023):
		led_pwm.duty(1023-i)
		time.sleep_ms(1)	
