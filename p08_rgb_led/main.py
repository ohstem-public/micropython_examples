# RGB led example

import neopixel
import machine
import random

NUM_LEDS = 1
RGB_LED_PIN = 45

np = neopixel.NeoPixel(machine.Pin(RGB_LED_PIN), NUM_LEDS)

while True:
  for i in range(NUM_LEDS):
    np[i] = (random.randrange(255), random.randrange(255), random.randrange(255))
    np.write()
    time.sleep_ms(200)