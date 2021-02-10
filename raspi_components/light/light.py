import RPi.GPIO as GPIO
from error import LedError

class LED:
    def __init__(self, pin):
        """
        This is a class used to control LED's directly connect to the GPIO via a pin given.
        Make sure that you are using a 220 Ohm resistor between the gpio pin and the led,
        and that you complete the circuit to the ground.
        """
        try:
            self.pin = int(pin)
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(self.pin, GPIO.OUT)
            GPIO.output(self.pin, GPIO.LOW)
        except:
            raise LedError("Error during the initiation of the LED class.")

    def on(self):
        """
        Turns the defined LED on.
        """
        try:
            GPIO.output(self.pin, GPIO.HIGH)
        except:
            raise LedError("Error while turning the LED on.")

    def off(self):
        """
        Turns the defined LED off.
        """
        try:
            GPIO.output(self.pin, GPIO.LOW)
        except:
            raise LedError("Error while turning the LED off.")
