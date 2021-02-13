import RPi.GPIO as GPIO
from .light_errors import RGBLedError

class RGBLed:
    """
    This class is used to control a RGB LED via the GPIO.
    Please make sure you have 220 Ohm resistors between the 3 gpio pins
    and the LED.
    """

    def __init__(self, red_pin, green_pin, blue_pin):
        """
        This initiates the pins needed to work with the RGB LED.
        """
        try:
            self.red_pin = int(red_pin)
            self.green_pin = int(green_pin)
            self.blue_pin = int(blue_pin)

            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(self.red_pin, GPIO.OUT)
            GPIO.setup(self.green_pin, GPIO.OUT)
            GPIO.setup(self.blue_pin, GPIO.OUT)

            GPIO.output(self.red_pin, GPIO.OUT)
            GPIO.output(self.green_pin, GPIO.OUT)
            GPIO.output(self.blue_pin, GPIO.OUT)

            self.pwm_red = GPIO.PWM(self.red_pin, 2000)
            self.pwm_green = GPIO.PWM(self.green_pin, 2000)
            self.pwm_blue = GPIO.PWM(self.blue_pin, 2000)
        except:
            raise RGBLedError("Error during the initiation of the RGB_LED class.")

    def on(self, red_val=0, green_val=0, blue_val=0):
        """
        This will turn on the RGB LED. To change the default color, change red_val,
        green_val, and blue_val when calling the function.
        """
        try:
            self.pwm_red.start(red_val)
            self.pwm_green.start(green_val)
            self.pwm_blue.start(blue_val)
        except:
            raise RGBLedError("Error while turning the RGB LED on.")

    def set_color(self, red_val, green_val, blue_val):
        """
        This will set the color of the RGB LED.
        Keep in mind that this uses the RGB color scale.
        """
        try:
            self.pwm_red.ChangeDutyCycle(red_val)
            self.pwm_green.ChangeDutyCycle(green_val)
            self.pwm_blue.ChangeDutyCycle(blue_val)
        except:
            raise RGBLedError("Error while changing the color of the RGB LED.")

    def off(self):
        """
        This will turn the RGB LED off.
        """
        try:
            self.pwm_red.stop()
            self.pwm_green.stop()
            self.pwm_blue.stop()
        except:
            raise RGBLedError("Error while turning the RGB LED off.")
