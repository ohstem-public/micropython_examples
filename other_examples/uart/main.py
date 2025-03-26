# UART example

import machine
import time

uart = machine.UART(2, baudrate=9600, rx=6, tx=7, timeout=10)
uart.init(parity=None, stop=1, bits=8)

while True:
  print(uart.readline())
  time.sleep(0.1)

'''
# write text to uart
uart.write('print(1+2)\r\n'); 

# write bytes list to uart
import ubinascii
cmd = [0x7e, 0x03, 0x11, 0x12, 0xef]
cmd_next = [0x7e, 0x03, 0x13, 0x10, 0xef]
u.write(ubinascii.hexlify(bytes(cmd_next)))'
'''

        
