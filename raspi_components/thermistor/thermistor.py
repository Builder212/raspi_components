import RPi.GPIO as GPIO
import math
from ADCDevice import *

class thermistor:
    def __init__(self):
        self.adc = ADCDevice()
        if(self.adc.detectI2C(0x48)):
            self.adc = PCF8591()

    def read_thermistor(self):
        value = self.adc.analogRead(0)
        voltage = value/255.0*3.3
        resistance_value = 10*voltage/(3.3-voltage)
        temp_kelvin = 1/(1/(273.15+25)+math.log(resistance_value/10)/3950.0)
        temp_celcius = temp_kelvin-273.15
        return voltage, temp_celcius

    def destroy():
        adc.close()
        GPIO.cleanup()

if __name__ == '__main__':
    print ('Program is starting ... ')
    thermistor = thermistor()

    try:
        while True:
            print(thermistor.read_thermo())
    except KeyboardInterrupt:
        thermistor.destroy()
