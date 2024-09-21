from machine import Pin
import time
#led = Pin("LED",Pin.OUT)
led = Pin("LED",mode=Pin.OUT)
status = False

while True:
    if status == False:
        led.on()
        status = True
    else:
        led.off()
        status = False
    time.sleep_ms(100)

print("end")


