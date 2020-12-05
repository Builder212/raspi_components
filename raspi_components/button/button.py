import RPi.GPIO as GPIO

class button:
    def __init__(self, pin):
        self.pin = int(pin)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    def is_pressed(self):
        if GPIO.input(self.pin) == GPIO.LOW:
            return True
        else:
            return False

if __name__ == '__main__':
    print ('Program is starting...')
    pin = input("What pin is your LED going to be operated from? ")
    print("\n")
    button = button(pin)

    try:
        while True:
            pressed = button.is_pressed()
            print(pressed)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
