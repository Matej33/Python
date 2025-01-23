import M5Stick
from machine import Pin, PWM, Signal
from time import sleep

display = M5Stick.lcd
display.rotation(3)
display.init()
display.jpg("Pucik.jpg", 0, 0, 1)
M5Stick.pmu.lcd_on()

buzzer = PWM(Pin(2))
buzzer.deinit()
buzzer.init(freq=0, duty_u16=0)

led = Signal(10, Pin.OUT, invert=True)
led.off()

noty = {
    "c": 523, "d": 587, "e": 660, "f": 698, "g": 784
}

melodia = [
    ("e", 0.1), ("e", 0.1), ("e", 0.4), ("e", 0.1), ("e", 0.1), ("e", 0.4), ("e", 0.1), ("g", 0.1), ("c", 0.1),
    ("d", 0.1), ("e", 0.4), ("f", 0.1), ("f", 0.1), ("f", 0.1), ("f", 0.1), ("f", 0.1), ("e", 0.1), ("e", 0.1),
    ("e", 0.1), ("e", 0.1), ("d", 0.1), ("d", 0.1), ("e", 0.1), ("d", 0.4), ("g", 0.4), ("e", 0.1), ("e", 0.1),
    ("e", 0.4), ("e", 0.1), ("e", 0.1), ("e", 0.4), ("e", 0.1), ("g", 0.1), ("c", 0.1), ("d", 0.1), ("e", 0.4),
    ("f", 0.1), ("f", 0.1), ("f", 0.1), ("f", 0.1), ("f", 0.1), ("e", 0.1), ("e", 0.1), ("e", 0.1), ("g", 0.1),
    ("g", 0.1), ("e", 0.1), ("d", 0.1), ("c", 0.1)
]

for nota, pauza in melodia:
    frekvencia = noty[nota]
    buzzer.freq(frekvencia)
    buzzer.duty_u16(2**15)
    led.on()
    sleep(0.25)
    buzzer.duty_u16(0)
    led.off()
    sleep(pauza)
