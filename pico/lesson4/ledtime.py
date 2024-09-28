from machine import Pin
import time
led = Pin("LED",Pin.OUT)
for i in range(0,30,2):
    print(f"loop:{i} ",time.localtime())
    led.value(1)
    time.sleep_ms(100)
    led.value(0)
    time.sleep_ms(100)
