# Pin Interrupt example

from machine import Pin

button = Pin(0, Pin.IN, Pin.PULL_UP)
led = Pin(48, Pin.OUT)

led_state = 1

def button_interrupt(p):
    print('Button pin state: ', p.value())
    led_state = 1 - led_state # reverse led state
    if led_state == 1:
        led.on()
    else:
        led.off()


button.irq(trigger=Pin.IRQ_FALLING, handler=button_interrupt)