from .resistor import VariableResistor
from time import sleep

class ResistorTest:
    def __init__():
        """
        This is the test class for the VariableResistor class.
        To use this, run ResistorTest.test(channel).
        """
        pass

    @classmethod
    def test(self, chn):
        """
        This will return the value, voltage, and resistance in a loop.
        """
        resistor = VariableResistor(chn)

        try:
            while True:
                value, voltage, resistance = resistor.read()
                print('Value: {}, Voltage: {}, Resistance: {}'.format(value, round(voltage, 1), round(resistance, 1)))
                sleep(0.1)
        except KeyboardInterrupt:
            resistor.close()
