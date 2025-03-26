# Example using PWM to fade an LED using rotary

import time
import neopixel
from machine import Pin, ADC

NUM_LEDS = 1

np = neopixel.NeoPixel(machine.Pin(45), NUM_LEDS)

adc_input = ADC(Pin(1))  # create ADC instance on GPIO1
adc_input.atten(ADC.ATTN_11DB) # ADC range max input 3.3V

led_state = 0

while True:
  sound_value = adc_input.read()
  
  if sound_value > 1000:
    led_state = 1 - led_state
    time.sleep(0.3)
  
    if led_state == 0:
      for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)
    else:
      for i in range(NUM_LEDS):
        np[i] = (255, 0, 0)
  
    np.write()

  time.sleep(10)

