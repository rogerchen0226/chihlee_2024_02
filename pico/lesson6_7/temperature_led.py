from machine import Timer,ADC,Pin
import time

green_led = Pin("LED",Pin.OUT)

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
def do_thing1(t:Timer):
    reading = adc.read_u16() * conversion_factor
    print(reading)
    # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
    # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree. 
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    print(f"current time:",time.localtime())
    
def do_thing2(t:Timer):
    green_led.toggle()
    
t1 = Timer(period=2000,mode=Timer.PERIODIC,callback=do_thing1)
t1 = Timer(period=300,mode=Timer.PERIODIC,callback=do_thing2)



