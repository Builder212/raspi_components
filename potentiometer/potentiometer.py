import time
from ADCDevice import *

class potentiometer:
    def __init__(self):
        self.adc = ADCDevice()
        if (self.adc.detectI2C(0x48)):
            self.adc = PCF8591()

    def read_value(self):
        value = self.adc.analogRead(0)
        voltage = value / 255.0 * 3.3
        return voltage

    def destroy():
        self.adc.close()

if __name__ == '__main__':
    print('Program is starting ... ')
    potentiometer = potentiometer()

    try:
        while True:
            print(potentiometer.read_value())
    except KeyboardInterrupt:
        potentiometer.destroy()
