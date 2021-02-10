from time import sleep
from light import LED

def LED_TEST():
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

if __name__ == '__main__':
    pin = input("What pin is your LED going to be operated from? ")
    print("\n")
    LED_TEST.test(pin)
