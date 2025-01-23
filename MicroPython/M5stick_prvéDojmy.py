from machine import PWM, Timer, Signal, Pin
from time import sleep

def Časovač(časovač):
    global sekunda, led, buzzer
    sekunda += 1
    print("\nUplynula {}. sekunda!".format(sekunda))
    buzzer.duty_u16(2**15)
    led.on()
    sleep(0.1)
    buzzer.duty_u16(0)
    led.off()

def Tlačidlo(button):
    sleep(0.01)
    global pressed
    pressed = True

pressed = False
button = Pin(37, Pin.IN, Pin.PULL_UP)
led = Signal(10, Pin.OUT, invert = True)
buzzer = PWM(Pin(2))
buzzer.deinit()
buzzer.init(freq = 3000, duty_u16 = 0)

časovač = Timer(-1)
časovač.deinit()

button.irq(handler=Tlačidlo, trigger=Pin.IRQ_FALLING)

while True:
    if pressed:
        i = sekunda = 0
        časovač.init(callback=Časovač, period=1000)
        while sekunda < 5:
            i += 1
            print("Odpočívam ({})...".format(i), end="\r")
            sleep(0.1)

        časovač.deinit()
        pressed = False

