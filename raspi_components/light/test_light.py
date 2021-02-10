from time import sleep
from light import LED

class LedTest:
    @classmethod
    def test(self, pin):
        try:
            led = LED(pin)

            while True:
                led.on()
                sleep(1)
                led.off()
                sleep(1)
        except KeyboardInterrupt:
            print("No errors were encountered while this test of your LED was ran.")
        else:
            pass
        finally:
            led.off()
            exit()
