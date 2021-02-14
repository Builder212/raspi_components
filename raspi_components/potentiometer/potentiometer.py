import time
from ADC import PCF
from ADC_errors import ADCError
from potentiometer_errors import PotentiometerError

class potentiometer:
    def __init__(self):
        self.adc = PCF()
        try:
            self.adc.is_connected()
        except ADCError:
            raise PotentiometerError("Failed to connect to your ADC.")

    def read_value(self):
        value = self.adc.read(0)
        voltage = value / 255.0 * 3.3
        return value, voltage

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
