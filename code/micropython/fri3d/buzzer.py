import machine


class Buzzer:
    def __init__(self, pin):
        """
        Create a new Buzzer instance
        @param pin: 	the machine.Pin on which the servo is connected
        """
        self.pwm = machine.PWM(machine.Pin(pin), freq=3000, duty_ns=0)

    def off(self):
        """
        Disable the output of the buzzer
        """
        self.pwm.duty(0)

    def set(self, freq, duty=200):
        """
        Set the frequency
        @param freq:     the frequency to set
        """
        self.pwm.freq(freq)
        self.pwm.duty_ns(200)