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
ZahrajTón(buzzer, 196, 0.5, 0.1)
ZahrajTón(buzzer, 262, 0.5, 0.1)
ZahrajTón(buzzer, 262, 0.5, 0.1)
ZahrajTón(buzzer, 294, 0.25, 0.1)
ZahrajTón(buzzer, 330, 0.25, 0.1)
ZahrajTón(buzzer, 349, 0.25, 0.1)
ZahrajTón(buzzer, 294, 0.25, 0.1)
ZahrajTón(buzzer, 330, 0.35, 0.25)
ZahrajTón(buzzer, 294, 0.25, 0.1)
ZahrajTón(buzzer, 330, 0.25, 0.1)
ZahrajTón(buzzer, 349, 0.5, 0.1)
ZahrajTón(buzzer, 330, 0.5, 0.1)
ZahrajTón(buzzer, 294, 0.25, 0.1)
ZahrajTón(buzzer, 262, 0.25, 0.1)
ZahrajTón(buzzer, 294, 0.5, 0.1)
ZahrajTón(buzzer, 262, 1, 0.5)
ZahrajTón(buzzer, 196, 0.5, 0.1)
ZahrajTón(buzzer, 262, 0.5, 0.1)
ZahrajTón(buzzer, 262, 0.5, 0.1)
ZahrajTón(buzzer, 294, 0.25, 0.1)
ZahrajTón(buzzer, 330, 0.25, 0.1)
ZahrajTón(buzzer, 349, 0.25, 0.1)
ZahrajTón(buzzer, 294, 0.25, 0.1)
ZahrajTón(buzzer, 330, 0.35, 0.25)
ZahrajTón(buzzer, 294, 0.25, 0.1)
ZahrajTón(buzzer, 330, 0.25, 0.1)
ZahrajTón(buzzer, 349, 0.5, 0.1)
ZahrajTón(buzzer, 330, 0.5, 0.1)
ZahrajTón(buzzer, 294, 0.25, 0.1)
ZahrajTón(buzzer, 262, 0.25, 0.1)
ZahrajTón(buzzer, 294, 0.5, 0.1)
ZahrajTón(buzzer, 262, 1, 0.5)

ZahrajTón(buzzer, 330, 0.25, 0.1)
ZahrajTón(buzzer, 349, 0.25, 0.1)
ZahrajTón(buzzer, 392, 1, 0.1)
ZahrajTón(buzzer, 440, 0.5, 0.1)
ZahrajTón(buzzer, 392, 1, 0.1)
ZahrajTón(buzzer, 349, 0.5, 0.1)
ZahrajTón(buzzer, 330, 0.5, 0.1)
ZahrajTón(buzzer, 294, 0.25, 0.1)
ZahrajTón(buzzer, 330, 0.25, 0.1)
ZahrajTón(buzzer, 349, 0.5, 0.1)
ZahrajTón(buzzer, 330, 0.5, 0.1)
ZahrajTón(buzzer, 294, 0.5, 0.1)
ZahrajTón(buzzer, 262, 0.5, 0.1)
ZahrajTón(buzzer, 294, 0.5, 0.1)

ZahrajTón(buzzer, 196, 0.5, 0.1)
ZahrajTón(buzzer, 262, 0.25, 0.1)
ZahrajTón(buzzer, 247, 0.25, 0.1)
ZahrajTón(buzzer, 262, 0.25, 0.1)
ZahrajTón(buzzer, 294, 0.25, 0.1)
ZahrajTón(buzzer, 330, 0.5, 0.1)
ZahrajTón(buzzer, 294, 1, 0.1)
ZahrajTón(buzzer, 262, 0.5, 0.1)
ZahrajTón(buzzer, 247, 0.5, 0.1)
ZahrajTón(buzzer, 196, 0.5, 0.1)
ZahrajTón(buzzer, 220, 0.25, 0.1)
ZahrajTón(buzzer, 247, 0.25, 0.1)
ZahrajTón(buzzer, 262, 0.5, 0.1)
ZahrajTón(buzzer, 262, 0.5, 0.1)
ZahrajTón(buzzer, 247, 1, 0.1)
ZahrajTón(buzzer, 262, 2, 0.1)










