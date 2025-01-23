from time import sleep, ticks_ms, ticks_diff
from machine import Pin, PWM, Signal
from random import uniform

button = Pin(37, Pin.IN, Pin.PULL_UP)
buzzer = PWM(Pin(2))
buzzer.deinit()
buzzer.init(freq=2000, duty_u16=0)
minimumBuzzer = 100000
priemerBuzzer = 0
led = Signal(10, Pin.OUT, 0, invert=True)
led.off()

for i in range(3):
    print("Začínam test o 2 sekundy")
    sleep(2)
    print("Štart")
    sleep(uniform(1, 5))
    buzzer.duty_u16(2 ** 15)
    startTime = ticks_ms()
    sleep(0.1)
    buzzer.duty_u16(0)
    while True:
        if button.value() == 0:
            endTime = (ticks_diff(ticks_ms(), startTime))
            print("čas: {} ms".format(endTime))
            priemerBuzzer += endTime
            if minimumBuzzer > endTime:
                minimumBuzzer = endTime
            break

print("minimum Buzzer: {} ms".format(minimumBuzzer))
print("priemer Buzzer: {} ms".format(priemerBuzzer / 3))

minimumLed = 1000000
priemerLed = 0

for i in range(3):
    print("Začínam test o 2 sekundy")
    sleep(2)
    print("Štart")
    sleep(uniform(1, 5))
    led.on()
    startTime = ticks_ms()
    sleep(0.1)
    buzzer.duty_u16(0)
    while True:
        if button.value() == 0:
            led.off()
            endTime = (ticks_diff(ticks_ms(), startTime))
            print("čas: {} ms".format(endTime))
            priemerLed += endTime
            if minimumLed > endTime:
                minimumLed = endTime
            break

print("minimum Led: {} ms".format(minimumLed))
print("priemer Led: {} ms".format(priemerLed / 3))
