from machine import Pin, SPI
from neopixel import NeoPixel

import fri3d.pinout


class Fri3d:
    def __init__(self):
        self._buzzer = None
        self._button = None
        self._touch = None
        self._display = None
        self._pixels = NeoPixel(Pin(pinout.neopixels, Pin.OUT), 5)

    def pixels(self):
        return self._pixels

    def buzzer(self):
        if not self._buzzer:
            from fri3d.buzzer import Buzzer
            self._buzzer = Buzzer(pinout.buzzer)

        return self._buzzer

    def button(self):
        if not self._button:
            from fri3d.buttons import Button
            self._button = Button(pinout.button)

        return self._button

    def touch(self):
        if not self._touch:
            from machine import TouchPad
            from fri3d.touch import NiftyTouch
            self._touch = [NiftyTouch(TouchPad(Pin(x)), idx, self.pixels()) for idx, x in enumerate(pinout.touch)]

        return self._touch

    def display(self):
        if not self._display:
            import st7789
            self._display = st7789.ST7789(
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

            self._display.init()
            self._display.jpg(f'/jpg/logo.jpg', 0, 0, st7789.FAST)

        return self._display


BADGE = Fri3d()
