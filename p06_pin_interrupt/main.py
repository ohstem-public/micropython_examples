# Pin Interrupt

from machine import Pin
p0 = Pin(0, Pin.IN)

def callback(p):
	print('Pin change state to', p.value())

p0.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=callback)