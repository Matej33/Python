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

farba_pozadie = color565(20, 0, 0)
farba_text = color565(255, 10, 10)

farby = (color565(20, 0, 0), color565(255, 10, 10))

deň = ("Pondelok", "Utorok", "Streda", "Štvrtok", "Piatok", "Sobota", "Nedela")

displej.fill(farba_pozadie)

tlačidlo1 = Signal(37, Pin.IN)


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


while True:
    if localtime()[3] < 10 and localtime()[4] < 10 and localtime()[5] < 10:
        PíšText(displej, font32, " {}:0{}:0{}".format(localtime()[3] + 1, localtime()[4], localtime()[5]), 55, 30,
                farby[1], farby[0])
        PíšText(displej, font22, "{}.{}.{}".format(localtime()[2], localtime()[1], localtime()[0]), 70, 60, farby[1],
                farby[0])
        PíšText(displej, font22, "{}".format(deň[localtime()[6]]), 85, 80, farby[1], farby[0])
    elif localtime()[4] < 10 and localtime()[5] < 10:
        PíšText(displej, font32, "{}:0{}:0{}".format(localtime()[3] + 1, localtime()[4], localtime()[5]), 55, 30,
                farby[1], farby[0])
        PíšText(displej, font22, "{}.{}.{}".format(localtime()[2], localtime()[1], localtime()[0]), 70, 60, farby[1],
                farby[0])
        PíšText(displej, font22, "{}".format(deň[localtime()[6]]), 85, 80, farby[1], farby[0])
    elif localtime()[4] < 10:
        PíšText(displej, font32, "{}:0{}:{}".format(localtime()[3] + 1, localtime()[4], localtime()[5]), 55, 30,
                farby[1], farby[0])
        PíšText(displej, font22, "{}.{}.{}".format(localtime()[2], localtime()[1], localtime()[0]), 70, 60, farby[1],
                farby[0])
        PíšText(displej, font22, "{}".format(deň[localtime()[6]]), 85, 80, farby[1], farby[0])
    elif localtime()[5] < 10:
        PíšText(displej, font32, "{}:{}:0{}".format(localtime()[3] + 1, localtime()[4], localtime()[5]), 55, 30,
                farby[1], farby[0])
        PíšText(displej, font22, "{}.{}.{}".format(localtime()[2], localtime()[1], localtime()[0]), 70, 60, farby[1],
                farby[0])
        PíšText(displej, font22, "{}".format(deň[localtime()[6]]), 85, 80, farby[1], farby[0])
    else:
        PíšText(displej, font32, "{}:{}:{}".format(localtime()[3] + 1, localtime()[4], localtime()[5]), 55, 30,
                farby[1], farby[0])
        PíšText(displej, font22, "{}.{}.{}".format(localtime()[2], localtime()[1], localtime()[0]), 70, 60, farby[1],
                farby[0])
        PíšText(displej, font22, "{}".format(deň[localtime()[6]]), 85, 80, farby[1], farby[0])
