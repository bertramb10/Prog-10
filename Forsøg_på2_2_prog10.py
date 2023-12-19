from machine import Pin, deepsleep
import esp32
from neopixel import NeoPixel
from time import sleep
from random import randint

# oprettervariabler
button_pin = 14
np_pin = 26
num_pixels = 12

#laver instansser(pinobjekter)
button = Pin(button_pin, Pin.IN, Pin.PULL_UP)
np = NeoPixel(Pin(np_pin, Pin.OUT), num_pixels)

# laver wakeup fra deepsleep når REPB trykkes
esp32.wake_on_ext0(pin=button, level=0)

def set_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)

    for i in range(num_pixels):
        np[i] = (red, green, blue)
    np.write()
    sleep(5)  # vis farve i 5 sek


print("ESP32 going to sleep...")

 #gå i deepsleep
deepsleep() #HVIS DENNE LINJE UDKOMMENTERES KØRER FARVEANIMATIONEN. KAN IKKE FÅ DET TIL AT VIRKE MED DEN VÅGNER

# kode heruner udføres når deepsleep afbrydes(troede jeg i hvert fald)
print("ESP32 waking up...")

# venter på kanp trykkes
while True:
    if button.value() == 1:
        set_random_color() #kører color funktoin



# slukker np igen når der deepsleepes
for i in range(num_pixels):
    np[i] = (0, 0, 0)
np.write()

