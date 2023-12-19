from hcsr04 import HCSR04
import uasyncio as asyncio
from gpio_lcd import GpioLcd
from machine import Pin

# Educaboard GPIO 4 -> PB2, 0->PB1
# 26 -> LED1, 15 EXPCS, 14 -> ROT ENC PB, 34 -> POTM
ultrasonic = HCSR04(15, 2)

# opretter instans af lcd klassen
lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25),
              d4_pin=Pin(33), d5_pin=Pin(32),
              d6_pin=Pin(21), d7_pin=Pin(22),
              num_lines=4, num_columns=20,
              backlight_pin=Pin(23, Pin.OUT))

async def distance():
    while True:
        dist_cm = ultrasonic.distance_cm()
        print(f"distance: {dist_cm} CM")
        
        #opdaterer distance data 
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr(f"Distance: {dist_cm} CM")

        await asyncio.sleep_ms(1000)

# kær event loop
loop = asyncio.get_event_loop()
loop.create_task(distance())
loop.run_forever()