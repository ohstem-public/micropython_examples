# Read button status and turn on LED

import time
from machine import Pin # import the Pin class from the machine library

led = Pin(48, Pin.OUT)  # create LED instance on GPIO48
button = Pin(0, Pin.IN, Pin.PULL_UP) # create button instance on GPIO0

while True:
    if button.value():
        led.off()
    else:
        led.on()

    time.sleep(0.1)
