from machine import Pin, Timer, RTC
from time import sleep_ms, time_ns
import M5Stick
from st7789 import color565
import inconsolata_num_80 as font80
import inconsolata_num_60 as font60
import inconsolata_32 as font32
import inconsolata_specSK_32 as font32_specSK
import inconsolata_16 as font16
import inconsolata_specSK_22 as font22_specSK


def Tlacidlo(pin):
    sleep_ms(10)
    if pin(): return
    if pin == Pin(37):
        global zmena_rezim
        zmena_rezim = True
    elif pin == Pin(39):
        global zmena_tema
        zmena_tema = True


def Casovac(casovac):
    global zmena_cas
    zmena_cas = True


def localtime(s=None):
    from time import time, mktime, gmtime
    if s == None: s = time()
    rok = gmtime(s)[0]
    letný = list(gmtime(mktime((rok, 3, 31, 2, 0, 0, None, None))))
    letný[2] -= (letný[6] + 1) % 7
    zimný = list(gmtime(mktime((rok, 10, 31, 2, 0, 0, None, None))))
    zimný[2] -= (zimný[6] + 1) % 7
    letný[6:8] = zimný[6:8] = (None, None)
    s += 3600  # UTC+1
    if (mktime(letný) < s < mktime(zimný)):
        s += 3600
    return gmtime(s)


def Text(displej, font, text, x, y, farba, font2=None):
    for i in (0, 1):
        font.PALETTE[i] = farba[i] << 8 & 0xff00 | farba[i] >> 8
        if font2: font2.PALETTE[i] = farba[i] << 8 & 0xff00 | farba[i] >> 8
    for znak in text:
        try:
            displej.bitmap(font, x, y, font.MAP.index(znak))
        except:
            try:
                displej.bitmap(font2, x, y, font2.MAP.index(znak))
            except:
                pass
            else:
                x += font2.WIDTH
        else:
            x += font.WIDTH
    return text


cas = M5Stick.rtc.datetime()
RTC().datetime(cas[:3] + (None,) + cas[3:])

displej = M5Stick.lcd
displej.rotation(3)
displej.init()
displej.fill(0)
M5Stick.pmu.lcd_on()

farby = (
    (color565(191, 54, 12), color565(0, 0, 0)),  # tmavá
    (color565(0, 0, 0), color565(100, 100, 100))  # svetlá
)