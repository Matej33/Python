from time import sleep, time, gmtime, localtime
from machine import RTC, Pin, PWM, Signal

import M5Stick
from st7789 import color565
import inconsolata_32 as font32, inconsolata_num_64 as font64, inconsolata_22 as font22

rtc = RTC()

print(M5Stick.spi)
displej = M5Stick.lcd
displej.rotation(3)
displej.init()
M5Stick.pmu.lcd_on()

farby = (color565(20, 0, 0), color565(255, 10, 10))
deň = ("Pondelok", "Utorok", "Streda", "Štvrtok", "Piatok", "Sobota", "Nedela")

displej.fill(farby[0])

mod = 0


def zmenFarbu(x):
    global farby
    farby = tuple(list(farby)[::-1])
    displej.fill(farby[0])


def zmenMod(y):
    global mod
    if mod:
        mod = 0
    else:
        mod = 1
    displej.fill(farby[0])


tlačidlo1 = Pin(39, Pin.IN, pull=Pin.PULL_UP)
tlačidlo2 = Pin(37, Pin.IN, pull=Pin.PULL_UP)

tlačidlo1.irq(handler=zmenFarbu, trigger=Pin.IRQ_FALLING)
tlačidlo2.irq(handler=zmenMod, trigger=Pin.IRQ_FALLING)


def PíšText(displej, font, text, x, y, farba_text=None, farba_pozadie=None):
    if farba_text:
        font.PALETTE[0] = farba_text << 8 & 0xff00 | farba_text >> 8
    if farba_pozadie:
        font.PALETTE[1] = farba_pozadie << 8 & 0xff00 | farba_pozadie >> 8
    for znak in text:
        if znak != "\n":
            try:
                displej.bitmap(font, x, y, font.MAP.index(znak))
            except:
                pass
            x += font.WIDTH


# neviem preco obcas dlhsie trva zmena modov (max 1 sekundu)

while True:
    t = localtime()
    if mod:
        if t[4] < 10:
            PíšText(displej, font64, "{}:0{}".format(t[3], t[4]), 40, 35, farby[1], farby[0])
        else:
            PíšText(displej, font64, "{}:{}".format(t[3], t[4]), 40, 35, farby[1], farby[0])
        if t[3] < 10:
            PíšText(displej, font64, " {}:{}".format(t[3], t[4]), 40, 35, farby[1], farby[0])
        sleep(0.5)
        PíšText(displej, font64, " ", 105, 35, farby[1], farby[0])
        sleep(0.5)
        # treba mat jeden sleep na cca 0.47 aby to islo presne lebo takto asi trva chvilu kym prejde kod
        if not mod:
            displej.fill(farby[0])
    else:
        if t[3] < 10 and t[4] < 10 and t[5] < 10:
            PíšText(displej, font32, " {}:0{}:0{}".format(t[3], t[4], t[5]), 55, 30, farby[1], farby[0])
            PíšText(displej, font22, "{}.{}.{}".format(t[2], t[1], t[0]), 70, 60, farby[1], farby[0])
            PíšText(displej, font22, "{}".format(deň[t[6]]), 85, 80, farby[1], farby[0])
        elif t[4] < 10 and t[5] < 10:
            PíšText(displej, font32, "{}:0{}:0{}".format(t[3], t[4], t[5]), 55, 30, farby[1], farby[0])
            PíšText(displej, font22, "{}.{}.{}".format(t[2], t[1], t[0]), 70, 60, farby[1], farby[0])
            PíšText(displej, font22, "{}".format(deň[t[6]]), 85, 80, farby[1], farby[0])
        elif t[4] < 10:
            PíšText(displej, font32, "{}:0{}:{}".format(t[3], t[4], t[5]), 55, 30, farby[1], farby[0])
            PíšText(displej, font22, "{}.{}.{}".format(t[2], t[1], t[0]), 70, 60, farby[1], farby[0])
            PíšText(displej, font22, "{}".format(deň[t[6]]), 85, 80, farby[1], farby[0])
        elif t[5] < 10:
            PíšText(displej, font32, "{}:{}:0{}".format(t[3], t[4], t[5]), 55, 30, farby[1], farby[0])
            PíšText(displej, font22, "{}.{}.{}".format(t[2], t[1], t[0]), 70, 60, farby[1], farby[0])
            PíšText(displej, font22, "{}".format(deň[t[6]]), 85, 80, farby[1], farby[0])
        else:
            PíšText(displej, font32, "{}:{}:{}".format(t[3], t[4], t[5]), 55, 30, farby[1], farby[0])
            PíšText(displej, font22, "{}.{}.{}".format(t[2], t[1], t[0]), 70, 60, farby[1], farby[0])
            PíšText(displej, font22, "{}".format(deň[t[6]]), 85, 80, farby[1], farby[0])
        if mod:
            displej.fill(farby[0])


