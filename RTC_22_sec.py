from machine import RTC
import time

# instans af RTC klassen
rtc = RTC()

# funktion der printer "triggered" samt tidsdata
def triggered_callback():
    print("Triggered")
    print("RTC datetime:", rtc.datetime())

# while løkke
while True:
    # gemmer lokal tid i variabel
    current_time = time.localtime()

    # tjekker om det er 22'ende sekund
    if current_time[5] == 22:
        triggered_callback()

        # sleep for at undgå mange triggers i løbet af det 22'ende sekund
        time.sleep(1)