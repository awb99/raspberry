 import asyncio

import RPi.GPIO as GPIO

async def flash_led(pin, duration):
while stop.run:
GPIO.output(pin, 0)
await asyncio.sleep(duration / 2)
GPIO.output(pin, 1)
await asyncio.sleep(duration / 2)

def stop(coro):
stop.run = False
GPIO.cleanup()

loop = asyncio.get_event_loop()
stop.run = True
coro = flash_led(7, 0.5)
loop.call_later(5, stop, coro)
loop.run_until_complete(coro)


