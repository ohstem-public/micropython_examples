# MQTT example

import asyncio
from machine import Pin
from mqtt_as import MQTTClient, config
from abutton import *

async def on_mqtt_msg(topic, msg):
  print('Got MQTT message: ', msg, ', topic: ', topic)
  led_state = int(msg)
  if led_state == 1:
      led.on()
  else:
      led.off()

cfg = config.copy()
cfg['ssid'] = 'WIFI_NAME'
cfg['wifi_pw'] = 'WIFI_PASSWORD'
cfg['server'] = 'test.mosquitto.org'
cfg['port'] = 1883
cfg['user'] = ''
cfg['password'] = ''
cfg['topics'].append(('mqtt/led/command', on_mqtt_msg))

mqtt_client = MQTTClient(cfg)

led = Pin(48, Pin.OUT)
led_state = 0

async def on_button_pressed():
  global led_state
  led_state = 1-led_state
  if led_state:
      led.on()
  else:
      led.off()
  await mqtt_client.publish('mqtt/led/state', led_state)

button = aButton(9)

async def main():
  await mqtt_client.connect()
  button.pressed(on_button_pressed)
  while True:
    await asyncio.sleep_ms(100)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('Code stopped')
finally:
    mqtt_client.close()
    asyncio.new_event_loop()