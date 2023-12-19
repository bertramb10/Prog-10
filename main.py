import umqtt_robust2 as mqtt

# Her kan i placere globale varibaler, og instanser af klasser
from machine import Pin, deepsleep, reset_cause
import esp32
import uasyncio as asyncio
from hcsr04 import HCSR04
from time import sleep
###################
button_pin = 14
led_pin = 26
trig_pin = 15
echo_pin = 2
##################

button = Pin(button_pin, Pin.IN, Pin.PULL_UP)
led = (Pin(led_pin, Pin.OUT))
trig = Pin(trig_pin, Pin.OUT)
echo = Pin(echo_pin, Pin.IN)
dist_cm = ultrasonic.distance_cm()

def toggle_led():
    for _ in range(10):
        led.on()  # Tænd LED
        sleep(0.2)  # Vent 1 sekund
        led.off()  # Sluk LED
        sleep(0.2)
        
def handle_interrupt(pin):
    print("Interrupt triggered!")
    
        

    
        
def measure_distance():
     Trigger the ultrasonic sensor
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    # Wait for the echo pin to go high
    while echo.value() == 0:
        pass
    pulse_start = time.ticks_us()

    # Wait for the echo pin to go low
    while echo.value() == 1:
        pass
    pulse_end = time.ticks_us()

    # Calculate distance in centimeters
    pulse_duration = pulse_end - pulse_start
    distance = (pulse_duration * 0.0343) / 2

    return distance


echo.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)
#tjek om vågn fra deepsleep
if reset_cause() == 4:
    print("Woke up from a deepsleep")
    toggle_led()
    print(echo)
    
    


sleep(4)
esp32.wake_on_ext0(pin = echo,
                   level = esp32.WAKEUP_ALL_LOW)

print("Going into deepsleep")
deepsleep()

