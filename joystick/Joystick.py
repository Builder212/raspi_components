import RPi.GPIO as GPIO
from ADCDevice import *

class joystick:
    def __init__(self, pin):
        self.pin = pin
        self.adc = ADCDevice()
        if(self.adc.detectI2C(0x48)):
            self.adc = PCF8591()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)

    def read_joystick(self):
        z = GPIO.input(self.pin)
        y = adc.analogRead(0)
        x = adc.analogRead(1)
        return x, y, z

    def destroy():
        self.adc.close()
        GPIO.cleanup()

if __name__ == '__main__':
    print('Program is starting ... ')
    pin = input("What pin is your joystick connected too? ")
    print("\n")
    joystick = joystick()

    try:
        while True:
            print(joystick.read_joystick())
    except KeyboardInterrupt:
        joystick.destroy()
