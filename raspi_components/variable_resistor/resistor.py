from math import log
from ..ADC.ADC import PCF
from ..ADC.ADC_errors import ADCError
from .resistor_errors import ResistorError

class VariableResistor:
    """
    This class can be used to work with potentiometers, photoresistors,
    and thermistors.
    """
    def __init__(self, chn):
        """
        Initiates the VariableResistor class on the given channel.
        """
        self.channel = chn
        self.adc = PCF()
        try:
            self.adc.is_connected()
        except ADCError:
            raise ResistorError("Failed to connect to your ADC.")

    def read(self):
        """
        Reads the value on the given channel in the initiation.
        """
        value = self.adc.read(self.channel)
        voltage = value / 255.0 * 3.3
        resistance = 10*voltage/(3.3-voltage)
        return value, voltage, resistance

    def temp(self, resistance):
        """
        This is used for the thermistor, to turn the resistance value into temperature
        in farhenheit.
        """
        temp = (1/(1/(273.15 + 25) + math.log(resistance/10)/3950.0)-273.15)*(9/5)+32 # Farhenheit
        return temp

    def close(self):
        """
        Used to close the connection to the ADC.
        """
        self.adc.close()
