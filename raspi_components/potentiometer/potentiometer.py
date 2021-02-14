import time
from ..ADC.ADC import PCF
from ..ADC.ADC_errors import ADCError
from .potentiometer_errors import PotentiometerError

class Potentiometer:
    def __init__(self, chn):
        self.channel = chn
        self.adc = PCF()
        try:
            self.adc.is_connected()
        except ADCError:
            raise PotentiometerError("Failed to connect to your ADC.")

    def read_value(self):
        value = self.adc.read(self.channel)
        voltage = value / 255.0 * 3.3
        return value, voltage

    def close(self):
        self.adc.close()
