from hcsr04 import HCSR04
import uasyncio as asyncio
from gpio_lcd import GpioLcd
from machine import Pin

# Educaboard GPIO 4 -> PB2, 0->PB1
# 26 -> LED1, 15 EXPCS, 14 -> ROT ENC PB, 34 -> POTM
ultrasonic = HCSR04(15, 2)

# Knap tilstand
button = Pin(14, Pin.IN)

# Opretter instans af lcd klassen
lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25),
              d4_pin=Pin(33), d5_pin=Pin(32),
              d6_pin=Pin(21), d7_pin=Pin(22),
              num_lines=4, num_columns=20,
              backlight_pin=Pin(23, Pin.OUT))

async def distance():
    while True:
        dist_cm = ultrasonic.distance_cm()
        print(f"distance: {dist_cm} CM")

        # Opdaterer distance data
        lcd.clear()
        lcd.move_to(0, 0)

        if dist_cm < 30:
            lcd.putstr("Too close")
        elif 30 <= dist_cm <= 60:
            lcd.putstr("Good distance")
        else:
            lcd.putstr("Too far")

        await asyncio.sleep_ms(1000)

async def button_handler():
    while True:
        # Tjekker om knappen er trykket
        if not button.value():
            print("Button pressed!")
            lcd.move_to(0, 1)
            lcd.putstr("Knap Trykket")

            # Her kan du tilføje yderligere handlinger baseret på knaptryk, hvis nødvendigt.

            await asyncio.sleep_ms(500)  # Vent for at undgå gentagne registreringer

        await asyncio.sleep_ms(100)

# Opretter event loop
loop = asyncio.get_event_loop()
loop.create_task(distance())
loop.create_task(button_handler())
loop.run_forever()