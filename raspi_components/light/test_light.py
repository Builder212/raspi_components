from time import sleep
from .light import Led

class LedTest:
    def __init__():
        """
        This is a test class. To call this run LedTest.test(pin).
        Do not initate this, as it will do nothing.
        """
        pass

    @classmethod
    def test(cls, pin):
        """
        This will loop turning the LED on and off, and dimming it.
        """
        try:
            led = Led(pin)

            while True:
                led.on(0)
                for x in range(0,100,1):
                    led.dim(x)
                    sleep(.1)
                for x in range(100,0,-1):
                    led.dim(x)
                    sleep(.1)
                led.off()
                sleep(1)
        except KeyboardInterrupt:
            print(" No errors were encountered while this test of your LED was ran.")
        else:
            pass
        finally:
            led.off()
