from machine import Timer, Pin

# tim = Timer(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print(1))
# tim.init(period=2000, mode=Timer.PERIODIC, callback=lambda t:print(2))
green_led = Pin("LED",Pin.OUT)

green_count = 0
def green_led_mycallback(t:Timer):

    global green_count
    green_count += 1
    green_led.toggle()
#     print(f"目前green mycallback被執行:{count}次")
    if green_count>=10:
        t.deinit()
        print("green_led_end")
        
red_count = 0
red_led = Pin(15,Pin.OUT)
def red_led_mycallback(t:Timer):
    global red_count
    red_count += 1
    red_led.toggle()
    print(f"目前red mycallback被執行:{red_count}次")
    if red_count>=10:
        t.deinit()
        print("red_led_end")

green_led_timer = Timer(period=1000,mode=Timer.PERIODIC,callback=green_led_mycallback)
red_led_timer = Timer(period=2000,mode=Timer.PERIODIC,callback=red_led_mycallback)
print("end")