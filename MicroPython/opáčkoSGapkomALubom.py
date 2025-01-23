from machine import Pin, Signal, PWM
from time import sleep, ticks_ms, ticks_diff
from random import uniform

ledDevice = Pin(10)
ledPWM = PWM(ledDevice, freq= 500, duty_u16=2**16-1)
led = Pin()
button = Signal(37, Pin.IN, Pin.PULL_UP)
led = Signal(10, Pin.OUT, invert=True, value=0)
led.off()
buzzer = PWM(Pin(2))
buzzer.deinit()
buzzer.init(freq=4000, duty_u16=0)

minLed = 9999999
minBuzzer = 9999999
averageLed = 0
averageBuzzer = 0

for i in range(6):
    if i < 3:
        if i == 0:
            print("Now it will test your reaction time on light")
        print("starting in 3 seconds")
        sleep(3)
        print("start!")
        sleep(uniform(2, 4))
        led.on()
        startTime = ticks_ms()
        if button.value() == 0:
            print("Cheater!")
            continue
        while True:
            if button.value() == 0:
                led.off()
                endTime = (ticks_diff(ticks_ms(), startTime))
                averageLed += endTime
                if endTime < minLed:
                    minLed = endTime
                print("Your reaction time: {} ms".format(endTime))
                break
    else:
        if i == 3:
            print("Now it will test your reaction time on sound")
        print("starting in 3 seconds")
        sleep(3)
        print("start!")
        sleep(uniform(2, 4))
        buzzer.duty_u16(2 ** 15)
        startTime = ticks_ms()
        if button.value() == 0:
            print("Cheater!")
            continue
        while True:
            if button.value() == 0:
                buzzer.duty_u16(0)
                endTime = (ticks_diff(ticks_ms(), startTime))
                averageBuzzer += endTime
                if endTime < minBuzzer:
                    minBuzzer = endTime

                print("Your reaction time: {} ms".format(endTime))
                break

print("")
print("Min time for led {} ms".format(minLed))
print("Min time for buzzer {} ms".format(minBuzzer))
print("Average time for led {} ms".format(averageLed / 3))
print("Average time for buzzer {} ms".format(averageBuzzer / 3))
print("Average time for both {} ms".format((averageBuzzer / 3 + averageLed / 3) / 2))

