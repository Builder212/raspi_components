from .potentiometer import Potentiometer
from time import sleep

class PotentiometerTest:
    def __init__():
        """
        """
        pass

    @classmethod
    def test(self, chn):
        """
        """
        potentiometer = Potentiometer(chn)

        try:
            while True:
                value, voltage = potentiometer.read_value()
                print('Value: {}, Voltage: {}'.format(value, round(voltage, 1)))
                sleep(0.1)
        except KeyboardInterrupt:
            potentiometer.close()
