import gc

from machine import TouchPad, Pin, SPI
from neopixel import NeoPixel
from gui.core.nanogui import refresh

import fri3d.pinout
from fri3d.buttons import Button
from fri3d.buzzer import Buzzer

import st7789

# pixels
pixels = NeoPixel(Pin(pinout.neopixels, Pin.OUT), 5)

# led
led = Pin(pinout.debug_led, Pin.OUT)

# button
button = Button(pinout.button)

# buzzer
buzzer = Buzzer(pinout.buzzer)

# touch
touch = (TouchPad(Pin(x)) for x in pinout.touch)
for t in touch:
    t.config(300)

# display
# rotation = 0
# madctl = 0x00 ()
# inversion_mode(True)
# color_order = st7789.RGB
# for rotation 0 use offset(0, 0)
# for rotation 1 use offset(0, 0)
# for rotation 2 use offset(0, 0)
# for rotation 3 use offset(0, 0)
display = st7789.ST7789(
        SPI(2, baudrate=40000000, polarity=1),
        240,
        240,
        reset=Pin(32, Pin.OUT),
        cs=Pin(5, Pin.OUT),
        dc=Pin(33, Pin.OUT),
        backlight=Pin(12, Pin.OUT),
        color_order=st7789.RGB,
        inversion=True,
        rotation=0,
        options=0,
        buffer_size=0)

display.init()
display.jpg(f'/jpg/logo.jpg', 0, 0, st7789.SLOW)

# ir
# blaster
# accelero