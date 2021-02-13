import RPi.GPIO as GPIO
from .buzzer_errors import BuzzerError

class Buzzer:
    """
    This class is made to control an active buzzer via the GPIO on the given pin.
    See the documentation on how to wire an active buzzer to work with this class.
    """
    def __init__(self, pin):
        """
        This initiates the buzzer on the given pin.
        """
        self.pin = int(pin)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)

    def on(self):
        """
        This turns the buzzer on.
        """
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        """
        This turns the buzzer off.
        """
        GPIO.output(self.pin, GPIO.LOW)
