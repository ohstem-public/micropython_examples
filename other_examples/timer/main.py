# Timer example

import time
from machine import Timer
timer1 = Timer(0)
timer1.init(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print('Timer 1 run'))

timer2 = Timer(1)  
counter = 0

def handle_timer_interrupt(timer):
  global counter
  counter += 1
  print('Timer2 interrupted: ', counter)
 
timer2.init(period=1000, mode=Timer.PERIODIC, callback=handle_timer_interrupt)