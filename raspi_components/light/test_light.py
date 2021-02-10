from time import sleep
from light import LED

class LedTest:
    def __init__():
        """
        This is a test class. To call this run LedTest.test(pin).
        Do not initate this, as it will do nothing.
        """
        pass

    @classmethod
    def test(cls, pin):
        try:
            led = LED(pin)

            while True:
                led.on()
                sleep(1)
                led.off()
                sleep(1)
        except KeyboardInterrupt:
            print(" No errors were encountered while this test of your LED was ran.")
        else:
            pass
        finally:
            led.off()
