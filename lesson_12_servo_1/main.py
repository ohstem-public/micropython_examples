# Servo example

import time
from machine import Pin, PWM

servo_pwm = PWM(Pin(5), freq=50, duty=0)

# Angle 0: 0.5ms/20ms = 0.025 = 2.5% duty cycle
# => duty = 0.025*1024 = 25.6 ~ 26
# Angle 180: 2.4ms/20ms = 0.12 = 12% duty cycle
# => duty: 0.12*1024 = 122.88 ~ 123

while True:
    servo_pwm.duty(26) # 0 degree
    time.sleep(1)
    servo_pwm.duty(123) # 180 degree
    time.sleep(1)