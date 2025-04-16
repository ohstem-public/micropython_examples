# Read button status and turn on LED

import time
from machine import Pin

led = Pin(48, Pin.OUT) # change to 8 if using Yolo Node
button = Pin(0, Pin.IN, Pin.PULL_UP) # change to 9 if using Yolo Node

while True:
    if button.value() == 0:
        led.on()
    else:
        led.off()

    time.sleep(0.1)
