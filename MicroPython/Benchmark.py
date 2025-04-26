from machine import Pin, Signal
from st7789 import color565
from time import sleep, ticks_us, ticks_diff
import M5Stick

print(M5Stick.spi)
displej = M5Stick.lcd
displej.rotation(0)
displej.init()
M5Stick.pmu.lcd_on()

tlačidlo = Signal(37, Pin.IN, invert = True)
farby = (color565(64, 64, 255), color565(192, 192, 0))

while not tlačidlo():
    t1 = ticks_us()
    for f in farby:
        displej.fill(f)
    t = ticks_diff(ticks_us(), t1)
    print("{:.2f} fps ".format(1_000_000 / t * len(farby)), end = "\r")
sleep(1)
M5Stick.pmu.lcd_off()
displej.sleep_mode(True)
