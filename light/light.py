import RPi.GPIO as GPIO
from time import sleep

class LED:
    def __init__(self, pin=7):
        self.ledPin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.ledPin, GPIO.OUT)
        GPIO.output(self.ledPin, GPIO.LOW)
        print ('LED using pin%d.'%self.ledPin)

    def on(self):
        GPIO.output(self.ledPin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.ledPin, GPIO.LOW)

if __name__ == '__main__':
    print ('Program is starting ... \n')
    LED = LED()
    try:
        while True:
            LED.on()
            sleep(5)
            LED.off()
            sleep(5)
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        GPIO.cleanup()
