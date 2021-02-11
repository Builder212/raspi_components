import RPi.GPIO as GPIO
from .light_errors import LedError

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
            GPIO.setup(self.pin, GPIO.OUT)
            GPIO.output(self.pin, GPIO.LOW)

            self.led_dim = GPIO.PWM(self.pin, 500)
        except:
            raise LedError("Error during the initiation of the LED class.")

    def dim(self, brightness):
        if brightness < 0:
            brightness = 0
        elif brightness > 100:
            brightness = 100
        else:
            pass

        self.led_dim.ChangeDutyCycle(brightness)

    def on(self, brightness=100):
        """
        Turns the defined LED on.
        """
        try:
            self.led_dim.start(brightness)
        except:
            raise LedError("Error while turning the LED on.")

    def off(self):
        """
        Turns the defined LED off.
        """
        try:
            self.led_dim.stop()
        except:
            raise LedError("Error while turning the LED off.")
