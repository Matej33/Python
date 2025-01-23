from time import sleep, time, gmtime, localtime
from machine import RTC, Pin, PWM, Signal

import M5Stick
from st7789 import color565
import vga1_8x16 as font16, vga1_16x32 as font32, vga1_bold_16x32 as font32b
import inconsolata_num_64 as font64

rtc = RTC()

print(M5Stick.spi)
displej = M5Stick.lcd
displej.rotation(3)
displej.init()
M5Stick.pmu.lcd_on()

farba_pozadie = color565(20, 0, 0)
farba_text = color565(255, 10, 10)

farby = (color565(20, 0, 0), color565(255, 10, 10))

displej.fill(farba_pozadie)

tlačidlo1 = Signal(37, Pin.IN)

def PíšText(displej, font, text, x, y, farba_text = None, farba_pozadie = None):
    if farba_text:
        font.PALETTE[0] = farba_text << 8 & 0xff00 | farba_text >> 8
    if farba_pozadie:
        font.PALETTE[1] = farba_pozadie << 8 & 0xff00 | farba_pozadie >> 8
    for znak in text:
        if znak != "\n":
            try: displej.bitmap(font, x, y, font.MAP.index(znak))
            except: pass
            x += font.WIDTH

while True:
    #if tlačidlo1 is pressed:
    farby = tuple(list(farby)[::-1])
    if localtime()[4] < 10:
        PíšText(displej, font64, "{}:0{}".format(localtime()[3], localtime()[4]), 40, 35, farby[1], farby[0])
    else:
        PíšText(displej, font64, "{}:{}".format(localtime()[3], localtime()[4]), 40, 35, farby[1], farby[0])
    if localtime()[3] < 10:
        PíšText(displej, font64, " {}:{}".format(localtime()[3], localtime()[4]), 40, 35, farby[1], farby[0])
    sleep(0.5)
    PíšText(displej, font64, " ", 105, 35, farba_text, farba_pozadie)
    sleep(0.5)


