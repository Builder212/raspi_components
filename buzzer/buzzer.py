import RPi.GPIO as GPIO

class buzzer:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)
    def off(self):
        GPIO.output(self.pin, GPIO.LOW)

if __name__ == '__main__':
    print ('Program is starting...')
    pin = input("What pin is your buzzer going to be read from? ")
    print("\n")
    buzzer = buzzer(pin)
    
    try:
        from time import sleep
        while True:
            buzzer.on()
            sleep(2)
            buzzer.off()
            sleep(3)
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
