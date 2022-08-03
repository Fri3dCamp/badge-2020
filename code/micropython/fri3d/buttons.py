import machine


# -- fri3d.button.on_press(lambda: print("Hello World"))
class Button:
    def __init__(self, pin):
        self.pin = machine.Pin(pin, machine.Pin.IN)

    def on_press(self, callback):
        """
        Invoke the callback when the button is pressed.
        :param callback:    the function to call when the button is pressed
        """
        self.pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=callback)

    def on_release(self, callback):
        """
        Invoke the callback when the button is released.
        :param callback:    the function to call when the button is released
        """
        self.pin.irq(trigger=machine.Pin.IRQ_RISING, handler=callback)