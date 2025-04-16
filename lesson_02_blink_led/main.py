# Blink a LED

import time
from machine import Pin

led = Pin(48, Pin.OUT) # change to 8 if using Yolo Node

while True:
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)