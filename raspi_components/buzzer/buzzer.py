import RPi.GPIO as GPIO
from time import sleep

class buzzer:
    def __init__(self, pin):
        self.pin = int(pin)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)

        self.buzzer = GPIO.PWM(self.pin, 1)

    def on(self, tone):
        self.buzzer.start(tone)

    def change_tone(self, tone):
        self.buzzer.ChangeFrequency(tone)

    def off(self):
        self.buzzer.stop()

if __name__ == '__main__':
    pin = input("What pin is your buzzer going to be read from? ")
    print("\n")
    buzzer = buzzer(pin)

    try:
        while True:
            buzzer.on(50)
            sleep(1)
            buzzer.change_tone(70)
            sleep(.5)
            buzzer.off()
            sleep(3)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
