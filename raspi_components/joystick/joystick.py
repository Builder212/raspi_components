import RPi.GPIO as GPIO
from ..ADC.ADC import PCF
from ..ADC.ADC_errors import ADCError

class Joystick:
    """
    This class is used to get the values from a joystick.
    """
    def __init__(self, xchn, ychn, zpin):
        """
        Initiates the Joystick class on the given two channels and one pin.
        """
        self.xChannel = xchn
        self.yChannel = ychn
        self.zPin = zpin

        self.adc = PCF()

        try:
            self.adc.is_connected()
        except ADCError:
            raise JoystickError("Failed to connect to your ADC.")

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.zPin, GPIO.IN, GPIO.PUD_UP)

    def read(self):
        """
        Reads the values of the x, y, and z axis of the joystick.
        """
        x = self.adc.read(self.xChannel)
        y = self.adc.read(self.yChannel)
        z = GPIO.input(self.zPin)
        return x, y, z

    def close(self):
        """
        closes the connection with the adc.
        """
        self.adc.close()
