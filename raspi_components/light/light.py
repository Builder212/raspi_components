import RPi.GPIO as GPIO
from time import sleep
from ADCDevice import *

class LED:
    def __init__(self, pin, adc=0, def=0):
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        if adc == 1:
            self.adc = ADCDevice()

            if (adc.detectI2C(0x48)):
                self.adc = PCF8591()
                self.is_dim = True
                self.power = GPIO.PWN(pin, 1000)

                if def == 1:
                    return True
        else:
            self.is_dim = False
            GPIO.output(self.pin, GPIO.LOW)

            if def == 1:
                return False

    def on(self):
        if self.is_dim == True:
            self.power.start(0)
            value = self.adc.analogRead(0)
            self.power.ChangeDutyCycle(value*100/255)
        else:
            GPIO.output(self.pin, GPIO.HIGH)

    def dim_update(self):
        value = self.adc.analogRead(0)
        self.power.ChangeDutyCycle(value*100/255)

    def off(self):
        if self.is_dim == True:
            adc.close()
        else:
            GPIO.output(self.pin, GPIO.LOW)
            GPIO.cleanup()

class RGB_LED:
    def __init__(self, red_pin, green_pin, blue_pin, adc=0, def=0):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(red_pin, GPIO.OUT)
        GPIO.setup(green_pin, GPIO.OUT)
        GPIO.setup(blue_pin, GPIO.OUT)
        if adc == 1:
            self.adc = ADCDevice()

            if (adc.detectI2C(0x48)):
                self.adc = PCF8591()
                self.is_dim = True

                if def == 1:
                    return True
        else:
            self.is_dim = False
            GPIO.output(red_pin, GPIO.OUT)       # read ADC value of 3 potentiometers
            GPIO.output(green_pin, GPIO.OUT)
            GPIO.output(blue_pin, GPIO.OUT)

            if def == 1:
                return False

        self.pwm_red = GPIO.PWM(red_pin, 2000)
        self.pwm_green = GPIO.PWM(green_pin, 2000)
        self.pwm_blue = GPIO.PWM(blue_pin, 2000)

    def on(self, red_val=0, green_val=0, blue_val=0):
        self.pwm_red.start(red_val)
        self.pwm_green.start(green_val)
        self.pwm_blue.start(blue_val)

    def set_color(self, red_val, green_val, blue_val):
        self.pwm_red.ChangeDutyCycle(red_val)
        self.pwm_green.ChangeDutyCycle(green_val)
        self.pwm_blue.ChangeDutyCycle(blue_val)

    def dim_color(self):
        red_val = self.adc.analogRead(0)
        green_val = self.adc.analogRead(1)
        blue_val = self.adc.analogRead(2)
        self.pwm_red.ChangeDutyCycle(value_Red*100/255)
        self.pwm_green.ChangeDutyCycle(value_Green*100/255)
        self.pwm_blue.ChangeDutyCycle(value_Blue*100/255)

    def off(self):
        if self.is_dim == True:
            adc.close()

        self.pwm_red.stop()
        self.pwm_green.stop()
        self.pwm_blue.stop()
        GPIO.cleanup()

if __name__ == '__main__':
    print("Program is starting ... \n")
    type = input("Are you using a normal LED or a RGB LED? (0-LED, 1-RGB LED) ")
    print("\n")

    if type == 0:
        pin = input("What pin is your LED going to be operated from? ")
        print("\n")
        led, dim = LED(pin, 1, 1)

        try:
            if dim == True:
                led.on()
                led.dim_update()
            else:
                led, dim = LED(pin, 0, 1)
                while True:
                    led.on()
                    sleep(5)
                    led.off()
                    sleep(5)
        except KeyboardInterrupt:
            led.off()
            GPIO.cleanup()
            exit()

    elif type == 1:
        from random import randint

        red_pin = input("What pin is your red LED going to be operated from? ")
        print("\n")
        green_pin = input("What pin is your green LED going to be operated from? ")
        print("\n")
        blue_pin = input("What pin is your blue LED going to be operated from? ")
        print("\n")
        led, dim = RGB_LED(red_pin, green_pin, blue_pin, 1, 1)

        try:
            led.on()
            if dim == true:
                while True:
                    led.dim_color()
            else:
                led, dim = RGB_LED(red_pin, green_pin, blue_pin, 0, 1)
                while True:
                    red = random.randit(0, 100)
                    green = random.randit(0, 100)
                    blue = random.randit(0, 100)
                    led.set_color(red, green, blue)
        except:
            led.off()
            GPIO.cleanup()
            exit()
