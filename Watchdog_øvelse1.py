from machine import WDT, Timer

def reset_watchdog(obj): # callback der "fodrer" watchdog
    print("Feeding the Watchdog!")
    wdt.feed() # metoden feed benyttes til at "fodre" watchdog
    
wdt = WDT(timeout=2000) # timeout 2000 ms

timer_0 = Timer(1)# esp32 har 4 hardware Timers der kan anvendes
# initialiserer periodisk timer der kalder reset_watchdog hvert 2.1 sekund
timer_0.init(period=2100, mode=Timer.PERIODIC, callback=reset_watchdog)


    