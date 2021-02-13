from .rgb_light import RGBLed
from time import sleep
from random import randint

class RGBLedTest:
    def __init__():
        """
        This is a test function to see if you have properly setup
        your RGB LED. It will randomly change colors every second
        until you stop it.
        """
        pass

    @classmethod
    def test(self, rpin, gpin, bpin):
        """
        This will turn the RGB LED on, and then randomly select a color to set the
        RGB LED to.
        """
        try:
            led = RGBLed(rpin, gpin, bpin)
            led.on()

            while True:
                red = randint(0, 100)
                green = randint(0, 100)
                blue = randint(0, 100)
                led.set_color(red, green, blue)
                sleep(1)
        except KeyboardInterrupt:
            print(" No errors were raised while this program ran.")
        else:
            pass
        finally:
            led.off()
