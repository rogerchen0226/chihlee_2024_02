import machine
import time
led = machine.Pin("LED",machine.Pin.OUT)
led.value(1)
time.sleep(1)
led.value(0)