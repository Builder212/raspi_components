from .button import Button
from time import sleep

class ButtonTest:
    def __init__():
        """
        This is a test class for Button. To call this run ButtonTest.test(pin).
        Initating this does nothing.
        """
        pass

    @classmethod
    def test(self, pin):
        """
        This will run through a loop, checking if the defined button was pressed
        every second. It will print True if it is, otherwise it will pring False.
        """
        button = Button(pin)

        try:
            while True:
                pressed = button.is_pressed()
                print(pressed)
                sleep(1)
        except KeyboardInterrupt:
            pass
