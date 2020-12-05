import RPi.GPIO as GPIO
from time import sleep

class LED:
    def __init__(self, pin):
        self.pin = int(pin)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)

    def test(self):
        try:
            while True:
                led.on()
                sleep(1)
                led.off()
                sleep(1)
        except KeyboardInterrupt:
            led.off()

class RGB_LED:
    def __init__(self, red_pin, green_pin, blue_pin):
        self.red_pin = int(red_pin)
        self.green_pin = int(green_pin)
        self.blue_pin = int(blue_pin)

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.red_pin, GPIO.OUT)
        GPIO.setup(self.green_pin, GPIO.OUT)
        GPIO.setup(self.blue_pin, GPIO.OUT)

        GPIO.output(self.red_pin, GPIO.OUT)
        GPIO.output(self.green_pin, GPIO.OUT)
        GPIO.output(self.blue_pin, GPIO.OUT)

        self.pwm_red = GPIO.PWM(self.red_pin, 2000)
        self.pwm_green = GPIO.PWM(self.green_pin, 2000)
        self.pwm_blue = GPIO.PWM(self.blue_pin, 2000)

    def on(self, red_val=0, green_val=0, blue_val=0):
        self.pwm_red.start(red_val)
        self.pwm_green.start(green_val)
        self.pwm_blue.start(blue_val)

    def set_color(self, red_val, green_val, blue_val):
        self.pwm_red.ChangeDutyCycle(red_val)
        self.pwm_green.ChangeDutyCycle(green_val)
        self.pwm_blue.ChangeDutyCycle(blue_val)

    def off(self):
        GPIO.cleanup()

if __name__ == '__main__':
    print("Program is starting ... \n")
    type = input("Are you using a normal LED or a RGB LED? (0-LED, 1-RGB LED) ")
    print("\n")

    if type == "0":
        pin = input("What pin is your LED going to be operated from? ")
        print("\n")
        led = LED(pin)

        led.test()

    elif type == "1":
        from random import randint

        red_pin = input("What pin is your red LED going to be operated from? ")
        print("\n")
        green_pin = input("What pin is your green LED going to be operated from? ")
        print("\n")
        blue_pin = input("What pin is your blue LED going to be operated from? ")
        print("\n")
        led = RGB_LED(red_pin, green_pin, blue_pin)

        try:
            led.on()
            while True:
                red = random.randit(0, 100)
                green = random.randit(0, 100)
                blue = random.randit(0, 100)
                led.set_color(red, green, blue)
                sleep(5)
        except:
            led.off()
            exit()
