import RPi.GPIO as GPIO

class button:
    def __init__(self, pin):
        self.pin = int(pin)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def is_pressed(self):
        if GPIO.input(self.pin) == GPIO.LOW:
            return True
        else:
            return False
