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
        GPIO.setmode(GPIO.BOARD)
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.output(self.pin, GPIO.LOW)
        GPIO.cleanup()

class RGB_LED:
    def __init__(self, red_pin, green_pin, blue_pin):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(red_pin, GPIO.OUT)
        GPIO.setup(green_pin, GPIO.OUT)
        GPIO.setup(blue_pin, GPIO.OUT)

        GPIO.output(red_pin, GPIO.OUT)
        GPIO.output(green_pin, GPIO.OUT)
        GPIO.output(blue_pin, GPIO.OUT)

        self.pwm_red = GPIO.PWM(int(red_pin), 2000)
        self.pwm_green = GPIO.PWM(int(green_pin), 2000)
        self.pwm_blue = GPIO.PWM(int(blue_pin), 2000)

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

        try:
            while True:
                led.on()
                sleep(5)
                led.off()
                sleep(5)
        except KeyboardInterrupt:
            led.off()
            exit()

    elif type == "1":
        from random import randint

        red_pin = input("What pin is your red LED going to be operated from? ")
        print("\n")
        green_pin = input("What pin is your green LED going to be operated from? ")
        print("\n")
        blue_pin = input("What pin is your blue LED going to be operated from? ")
        print("\n")
        led, dim = RGB_LED(red_pin, green_pin, blue_pin)

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
