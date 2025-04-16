import asyncio
from machine import Pin, SoftI2C
from ci_device_mqtt import *
from dht_20 import DHT20
from lcd_1602 import LCD1602

SCL_PIN = 6
SDA_PIN = 5

i2c = SoftI2C(scl=Pin(SCL_PIN), sda=Pin(SDA_PIN), freq=100000)

lcd = LCD1602(i2c, addr=0x21)
dht_sensor = DHT20(i2c)

SSID = 'Sandiego2'
PASSWORD = '0988807067'
TOKEN = 'ls08rk52xm7umejxebn7'

ci_client = CIDeviceMqttClient(SSID, PASSWORD, TOKEN, 'app.coreiot.io', 1883)


async def task1(): # send telemetry to core iot
  while True:
    if ci_client.connected:
        temp = dht_sensor.temperature()
        humid = dht_sensor.humidity()
        await ci_client.send_telemetry(
            {'temperature':temp,'humidity':humid}
        )
        print('Sent')
    await asyncio.sleep_ms(5000)

async def task2(): # print to LCD
  lcd.backlight_on()
  while True:
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr('Nhiet do: ' + str(dht_sensor.temperature()) + '*C')
    lcd.move_to(0, 1)
    lcd.putstr('Do am:    ' + str(dht_sensor.humidity()) + '%')
    await asyncio.sleep_ms(5000)

async def main():
  await ci_client.connect()
  asyncio.create_task(task1())
  asyncio.create_task(task2())

  while True:
    await asyncio.sleep_ms(100)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('Code stopped')
finally:
    ci_client.close()
    asyncio.new_event_loop()