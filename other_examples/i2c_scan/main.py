# Scan I2C example

import machine

i2c = machine.SoftI2C(scl=machine.Pin(SCL_PIN), sda=machine.Pin(SDA_PIN))
print('Scan i2c bus...')
devices = i2c.scan()

if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))

  for device in devices:  
    print("Decimal address: ", device, " | Hexa address: ", hex(device))