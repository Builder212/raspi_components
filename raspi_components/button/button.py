import RPi.GPIO as GPIO
from .button_errors import ButtonError

class Button:
    def __init__(self, pin):
        """
        Initiates the button class on a certain gpio pin.
        """
        try:
            self.pin = int(pin)
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        except:
            raise ButtonError("Error while initating the Button class.")

    def is_pressed(self):
        """
        Checks to see if the defined button is clicked.
        """
        try:
            if GPIO.input(self.pin) == GPIO.LOW:
                return True
            else:
                return False
        except:
            raise ButtonError("Error while checking to see if your definied button was pressed.")
