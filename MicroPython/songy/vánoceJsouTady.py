from machine import Pin, PWM
from time import sleep

def ZahrajTón(buzzer, freq, trvanie, pauza=0):
    buzzer.init(freq=freq, duty_u16=2 ** 15)
    sleep(trvanie)
    buzzer.duty_u16(0)
    sleep(pauza)

buzzer = PWM(Pin(2))
buzzer.deinit()

sleep(1)
ZahrajTón(buzzer, 660, 0.25, 0.1) #E
ZahrajTón(buzzer, 660, 0.25, 0.1)
ZahrajTón(buzzer, 660, 0.25, 0.4)            #
ZahrajTón(buzzer, 660, 0.25, 0.1)
ZahrajTón(buzzer, 660, 0.25, 0.1)
ZahrajTón(buzzer, 660, 0.25, 0.4)                 #
ZahrajTón(buzzer, 660, 0.25, 0.1)
ZahrajTón(buzzer, 784, 0.25, 0.1) #G
ZahrajTón(buzzer, 523, 0.25, 0.1) #C
ZahrajTón(buzzer, 587, 0.25, 0.1) #D
ZahrajTón(buzzer, 660, 0.25, 0.4)              #
ZahrajTón(buzzer, 698, 0.25, 0.1) #F
ZahrajTón(buzzer, 698, 0.25, 0.1)
ZahrajTón(buzzer, 698, 0.25, 0.1)
ZahrajTón(buzzer, 698, 0.25, 0.1)
ZahrajTón(buzzer, 698, 0.25, 0.1)
ZahrajTón(buzzer, 660, 0.25, 0.1)
ZahrajTón(buzzer, 660, 0.25, 0.1)
ZahrajTón(buzzer, 660, 0.25, 0.1)
ZahrajTón(buzzer, 660, 0.25, 0.1)
ZahrajTón(buzzer, 587, 0.25, 0.1)
ZahrajTón(buzzer, 587, 0.25, 0.1)
ZahrajTón(buzzer, 660, 0.25, 0.1)
ZahrajTón(buzzer, 587, 0.25, 0.4)              #
ZahrajTón(buzzer, 784, 0.25, 0.4)              #
ZahrajTón(buzzer, 660, 0.25, 0.1)
ZahrajTón(buzzer, 660, 0.25, 0.1)
ZahrajTón(buzzer, 660, 0.25, 0.4)
ZahrajTón(buzzer, 660, 0.25, 0.1)
ZahrajTón(buzzer, 660, 0.25, 0.1)
ZahrajTón(buzzer, 660, 0.25, 0.4)              #
ZahrajTón(buzzer, 660, 0.25, 0.1)
ZahrajTón(buzzer, 784, 0.25, 0.1)
ZahrajTón(buzzer, 523, 0.25, 0.1)
ZahrajTón(buzzer, 587, 0.25, 0.1)
ZahrajTón(buzzer, 660, 0.25, 0.4)              #
ZahrajTón(buzzer, 698, 0.25, 0.1)
ZahrajTón(buzzer, 698, 0.25, 0.1)
ZahrajTón(buzzer, 698, 0.25, 0.1)
ZahrajTón(buzzer, 698, 0.25, 0.1)
ZahrajTón(buzzer, 698, 0.25, 0.1)
ZahrajTón(buzzer, 660, 0.25, 0.1)
ZahrajTón(buzzer, 660, 0.25, 0.1)
ZahrajTón(buzzer, 660, 0.25, 0.1)
ZahrajTón(buzzer, 784, 0.25, 0.1)
ZahrajTón(buzzer, 784, 0.25, 0.1)
ZahrajTón(buzzer, 660, 0.25, 0.1)
ZahrajTón(buzzer, 587, 0.25, 0.1)
ZahrajTón(buzzer, 523, 0.25, 0.1)

