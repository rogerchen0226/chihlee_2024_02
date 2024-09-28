from machine import Timer,ADC,Pin,PWM
import time

green_led = Pin("LED",Pin.OUT)

pwm = PWM(Pin(15))
pwm.freq(1000)

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
def do_thing0(t:Timer):
    green_led.toggle()
    
def do_thing1(t:Timer):
    reading = adc.read_u16() * conversion_factor
    print(reading)
    # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
    # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree. 
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    print(f"current time:",time.localtime())
    
def do_thing2(t:Timer):
    adc1 =ADC(Pin(26))
    duty = adc1.read_u16()
    pwm.duty_u16(duty)
    print(f'可變電組:{round(duty/65535*10)}')

t0 = Timer(period=500,mode=Timer.PERIODIC,callback=do_thing0)
t1 = Timer(period=2000,mode=Timer.PERIODIC,callback=do_thing1)
t2 = Timer(period=500,mode=Timer.PERIODIC,callback=do_thing2)



