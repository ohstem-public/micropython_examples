# Asyncio multi tasking example

import asyncio

async def task1():
    while True:
        print("Task 1")
        await asyncio.sleep(1)

async def task2():
    while True:
        print("Task 2")
        await asyncio.sleep(2)

async def main():
  print("Code started")
  asyncio.create_task(task1())
  asyncio.create_task(task2())
  
  while True:
    await asyncio.sleep_ms(100)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('Code stopped')
finally:
    asyncio.new_event_loop()