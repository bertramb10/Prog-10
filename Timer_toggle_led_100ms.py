from machine import Pin, Timer
from time import sleep

# definer pin numer for led
led_pin = 26

# led blir instans af pin klassen
led = Pin(led_pin, Pin.OUT)

# laver callback funktoin der toggler led
def toggle_led(timer):
    led.value(not led.value())

# oprette Timeren
timer = Timer(-1)

# callback funktion udløses hvert 100 milliskeund af timeren
timer.init(period=100, mode=Timer.PERIODIC, callback=toggle_led)

# Kør en evighedsloop for at holde programmet kørende
while True:
    # kører hvert 0.1 sekund
    sleep(0.1)