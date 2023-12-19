from machine import Timer
import time
from time import sleep
# oprette timer objekt
timer = Timer(-1)

# funktoin der henter nuværende tid
def timer_callback(timer):
    # Get current time
    current_time = time.localtime()

    # tjek om sekund = 22
    if current_time[5] == 22:
        print("Triggered")
        print("Datetime:", current_time)

# inddstiler timer så den udløser funktionen hvert 900 millisekund
timer.init(period=900, mode= Timer.PERIODIC, callback=timer_callback)

# uendeligt loop
while True:
    #kort sleep for at redde cpu'en
    sleep(0.1)