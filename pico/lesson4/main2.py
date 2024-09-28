from machine import Timer


# tim = Timer(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print(1))
# tim.init(period=2000, mode=Timer.PERIODIC, callback=lambda t:print(2))
def mycallback_Pass(t:Timer):
    pass

def led_switch():
    from machine import Pin, time
    led = Pin("LED",Pin.OUT)
    led.value(1)
    time.sleep_ms(300)
    led.value(0)
    
count = 0;
def mycallback(t:Timer):

    global count
    count += 1
    led_switch()
    print(f"目前mycallback被執行:{count}次")

    if count>=10:
        t.deinit()


led_timer = Timer(period=1000,mode=Timer.PERIODIC,callback=mycallback)

print("end")