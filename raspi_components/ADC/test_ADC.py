from .ADC import PCF
from time import sleep

class ADCTest:
    def __init__():
        """
        This is the test class for the ADC. To use this,
        run ADCTest.test().
        """
        pass

    @classmethod
    def test(self):
        """
        This tests whether the adc can be connected too. It will
        print either success or failure.
        """
        adc = PCF()
        try:
            adc.is_connected()
        except:
            print("Failure to connect to the ADC.")
        else:
            print("Success.")
