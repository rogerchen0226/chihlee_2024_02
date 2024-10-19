#! usr/bin/micropython

'''
led->gpio15
光敏電阻 -> gpio28
可變電阻 -> gpio26
內建溫度sensor -> adc最後1pin,共5pin
'''

from machine import Timer,ADC,Pin,PWM,RTC
import binascii
from umqtt.simple import MQTTClient
import tools


def do_thing(t):
    '''
    :param t:Timer的實體
    負責偵測溫度和光線
    每2秒執行1次
    '''
    conversion_factor = 3.3 / (65535)
    reading = adc.read_u16() * conversion_factor
    temperature = round(27 - (reading - 0.706)/0.001721,2)
    formatted_number = "{:.2f}".format(temperature)
    print(f'溫度:{formatted_number}')
    mqtt.publish('SA-21/TEMP', f'{formatted_number}')
    adc_value = adc_light.read_u16()
    #adc_value = (adc_value // 1000) * 1000 # 固定尾碼為000
    line_state = 0 if adc_value < 10000 else 1
    print(f'光線:{line_state}')
    mqtt.publish('SA-21/LIGHT', f'{line_state}')
    
    
def do_thing1(t):
    '''
    :param t:Timer的實體
    負責可變電阻和改變led的亮度
    '''
    
    duty = adc1.read_u16()
    pwm.duty_u16(duty)
    led_level = round(duty/65535*10)
    print(f'可變電阻:{led_level}')
    mqtt.publish('SA-21/LED_LEVEL', f'{led_level}')

def main():
    try:
        tools.connect()
        mqtt.connect()
    except RuntimeError as e:
        print(e)
    except Exception:
        print('不知明的錯誤')
    else:
        t1 = Timer(period=2000, mode=Timer.PERIODIC, callback=do_thing)
        t2 = Timer(period=500, mode=Timer.PERIODIC, callback=do_thing1)
        

if __name__ == '__main__':
    adc = ADC(4) #內建溫度
    adc1 = ADC(Pin(26)) #可變電阻
    adc_light = ADC(Pin(28)) #光敏電阻
    pwm = PWM(Pin(15),freq=50) #pwm led
    
    #MQTT
    SERVER = "192.168.0.252"
    CLIENT_ID = binascii.hexlify(machine.unique_id())
    mqtt = MQTTClient(CLIENT_ID, SERVER,user='pi',password='raspberry')
    main()