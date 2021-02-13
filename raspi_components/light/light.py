import RPi.GPIO as GPIO
from .light_errors import LedError

class Led:
    """
    This is a class used to control LED's directly connected to the GPIO via a pin given.
    See the documentation for an example of how to wire the LED.
    """
    def __init__(self, pin):
        """
        This initates the LED on the given pin, setting it into the output mode,
        making sure it is off, and setting the PWM up so that the LED can be dimmed.
        """
        try:
            self.pin = int(pin)

            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(self.pin, GPIO.OUT)
            GPIO.output(self.pin, GPIO.LOW)

            self.led_dim = GPIO.PWM(self.pin, 500)
        except:
            raise LedError("Error during the initiation of the LED class.")

    def on(self, brightness=100):
        """
        Turns the defined LED on, the brightness is set by default to 100%.
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

    def dim(self, brightness):
        """
        Dims the definied LED. Keep in mind, that if you don't first turn the
        LED on this will error out.
        """
        if brightness < 0:
            brightness = 0
        elif brightness > 100:
            brightness = 100
        else:
            pass

        try:
            self.led_dim.ChangeDutyCycle(brightness)
        except:
            raise LedError("Error while dimming the LED. Make sure you have turned the LED on.")
