from machine import Timer,ADC,Pin
import time

red_led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

adc = machine.ADC(4)
conversion_factor = 3.3 / (65535)
'''
while True:
    reading = adc.read_u16() * conversion_factor
    print(reading)
    # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
    # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree. 
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    utime.sleep(2)
'''
def mycallback(t:Timer):
    reading = adc.read_u16() * conversion_factor
    print(reading)
    # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
    # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree. 
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    print(f"current time:",time.localtime())
    
Timer(period=2000,mode=Timer.PERIODIC,callback=mycallback)

while True:
    if button.value():
        red_led.toggle()
        time.sleep(0.5)
