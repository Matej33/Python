from st7789 import ST7789, color565
from time import sleep, ticks_us, ticks_diff
from math import sqrt
import M5Stick
import machine


def Triangle(a):
    v = round(sqrt(0.75 * a * a) / 2)
    a = round(a / 2)
    return ((0, -v), (a, v), (-a, v))


def Rays(a):
    l = a
    return ((0, 0 - l), (0, 0), (0 + l, 0), (0, 0), (0, 0 + l), (0, 0), (0 - l, 0), (0, 0))


def Chimney(a, b, c):
    v = round(sqrt(0.75 * c * c) / 2)
    ax = a
    ay = b - v
    bx = round(a - c / 2)
    by = b + v

    leftDownChimneyX = round(bx + (ax - bx) / 3)
    leftDownChimneyY = round(ay + ((by - ay) / 3) * 2)
    leftUpChimneyX = round(bx + (ax - bx) / 3)
    leftUpChimneyY = ay
    rightDownChimneyX = round(bx + ((ax - bx) / 3) * 2)
    rightDownChimneyY = round(ay + (by - ay) / 3)
    rightUpChimneyX = round(bx + ((ax - bx) / 3) * 2)
    rightUpChimneyY = ay
    return ((leftDownChimneyX, leftDownChimneyY), (leftUpChimneyX, leftUpChimneyY), (rightUpChimneyX, rightUpChimneyY),
            (rightDownChimneyX, rightDownChimneyY))

machine.freq(240_000_000) #160M / 240M
valueOfBaudrate = 20_000_000  #26.6_M / 40M / 80M
spi = SPI(1, baudrate=valueOfBaudrate,
          sck=Pin(13),
          mosi=Pin(15),
          miso=None
          )

#print(spi)
display = ST7789(spi, 135, 240,
                 dc=Pin(23, Pin.OUT),
                 reset=Pin(18, Pin.OUT),
                 cs=Pin(5, Pin.OUT)
                 )

display.init()
display.rotation(3)
M5Stick.pmu.lcd_on()

button = Signal(37, Pin.IN, invert=True)
colors = (color565(64, 64, 255), color565(192, 192, 0))

maxFPSColors = 0
maxFPSImage = 0

while not button():
    t1 = ticks_us()
    for f in colors:
        display.fill(f)
    t = ticks_diff(ticks_us(), t1)
    if maxFPSColors < (1_000_000 / t * len(colors)):
        maxFPSColors = (1_000_000 / t * len(colors))
    print("{:.2f} fps ".format(1_000_000 / t * len(colors)), end="\r")

display.fill(color565(0, 0, 0))
sleep(1)

while not button():
    t1 = ticks_us()
    # obloha a travnik
    display.fill_rect(0, 0, 67, 240, color565(101, 193, 230))
    display.fill_rect(0, 68, 67, 240, color565(34, 163, 43))
    # slnko
    display.fill_circle(30, 30, 10, color565(255, 251, 33))
    # lúče
    display.polygon(Rays(20), 30, 30, color565(255, 251, 33))
    display.polygon(Rays(20), 30, 30, color565(255, 251, 33), 3.14 / 5, 0, 0)
    display.polygon(Rays(20), 30, 30, color565(255, 251, 33), 3.14 / 3, 0, 0)

    # domček
    display.fill_rect(105, 81, 31, 31, color565(161, 122, 32))
    display.fill_polygon(Triangle(36), 120, 65, color565(161, 31, 44))
    # okno
    display.rect(123, 86, 11, 11, color565(0, 0, 0))
    display.rect(124, 87, 9, 9, color565(0, 0, 0))
    display.fill_rect(125, 88, 7, 7, color565(200, 200, 200))
    display.hline(125, 91, 7, color565(0, 0, 0))
    display.vline(128, 88, 7, color565(0, 0, 0))
    # dvere
    display.fill_rect(110, 95, 10, 17, color565(74, 60, 46))
    display.fill_circle(118, 103, 1, color565(26, 25, 24))
    # komín
    display.fill_polygon(Chimney(120, 65, 36), 0, 0, color565(100, 100, 100))

    # oblaky/dym z komina
    for i in range(3):
        z = 180 + i * 10
        display.fill_circle(z, 20, 10, color565(200, 200, 200))
    for i in range(3):
        z = 120 + i * 10
        display.fill_circle(z, 30, 10, color565(200, 200, 200))

    # strom kmen + 3x koruna
    display.fill_rect(200, 92, 11, 20, color565(82, 62, 40))
    for i in range(3):
        y = 79 - i * 14
        display.fill_polygon(Triangle(30), 205, y, color565(36, 87, 45))

    # auto
    for i in range(2):
        z = 30 + i * 30
        display.fill_circle(z, 110, 7, color565(20, 20, 20))
    display.fill_polygon(((20, 107), (20, 95), (35, 95), (40, 85), (50, 85), (60, 95), (70, 95), (75, 107)), 0, 0,
                         color565(255, 40, 0))
    t = ticks_diff(ticks_us(), t1)
    if maxFPSImage < (1_000_000 / t):
        maxFPSImage = (1_000_000 / t)
    print("{:.2f} fps ".format(1_000_000 / t), end="\r")

M5Stick.pmu.lcd_off()
display.sleep_mode(True)
print("CPU freq {:.2f} MHz\nSPI freq {:.2f} MHz\nFPS 1. part: {:.2f} fps \nFPS 2. part: {:.2f} fps \n".format((machine.freq() / 1000000), (valueOfBaudrate / 1000000), (maxFPSColors), (maxFPSImage)))



