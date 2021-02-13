from .buzzer import Buzzer
from time import sleep

class BuzzerTest:
    def __init__():
        """
        This is a test class for Buzzer. To call this run BuzzerTest.test(pin).
        Initating this does nothing.
        """
        pass

    @classmethod
    def test(self, pin):
        """
        This will turn the buzzer on for one second. If this works you will hear a beep.
        """
        buzzer = Buzzer(pin)

        try:
            buzzer.on()
            sleep(1)
            buzzer.off()
        except KeyboardInterrupt:
            buzzer.off()
        finally:
            buzzer.off()
