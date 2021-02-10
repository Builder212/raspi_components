from button import Button

class ButtonTest:
    def __init__():
        pass

    @classmethod
    def test(pin):
        button = Button(pin)

        try:
            while True:
                pressed = button.is_pressed()
                print(pressed)
        except KeyboardInterrupt:
            GPIO.cleanup()
