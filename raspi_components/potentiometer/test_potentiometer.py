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
        potentiometer = Potentiometer()

        try:
            while True:
                print(potentiometer.read_value(chn))
                sleep(0.1)
        except KeyboardInterrupt:
            potentiometer.close()
