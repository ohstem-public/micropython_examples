# Blink a LED

import time
from machine import Pin # import the Pin class from the machine library

led = Pin(48, Pin.OUT)  # create the LED instance (from GPIO pin 48)

while True:
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
