import RPi.GPIO as GPIO
from error import LedError

class LED:
    def __init__(self, pin):
        try:
            self.pin = int(pin)
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)
            GPIO.setup(self.pin, GPIO.OUT)
            GPIO.output(self.pin, GPIO.LOW)
        except:
            raise LedError("Error during the initiation of the LED class.\nPlease make sure you have given a valid pin number.")

    def on(self):
        try:
            GPIO.output(self.pin, GPIO.HIGH)
        except:
            raise LedError("Error while turning the LED on.")

    def off(self):
        try:
            GPIO.output(self.pin, GPIO.LOW)
        except:
            raise LedError("Error while turning the LED off.")
