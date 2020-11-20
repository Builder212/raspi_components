import RPi.GPIO as GPIO
from ADCDevice import *

class photresistor:
    def __init__(self):
        self.adc = ADCDevice()
        if(self.adc.detectI2C(0x48)):
            self.adc = PCF8591()

    def read_value(self):
        value = self.adc.analogRead(0)
        return value

    def destroy(self):
        self.adc.close()
        GPIO.cleanup()

if __name__ == '__main__':
    print ('Program is starting ... ')
    photoresistor = photresistor()

    try:
        while True:
            print(photoresistor.read_value())
    except KeyboardInterrupt:
        photoresistor.destroy()
