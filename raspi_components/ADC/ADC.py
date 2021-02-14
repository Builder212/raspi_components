import smbus
from .ADC_errors import ADCError

class PCF():
    """
    This class is used to work with the PCF8591 module, an ADC.
    """
    def __init__(self):
        """
        This initiates the ADC.
        """
        self.cmd = 0x40
        self.address = 0x48
        try:
            self.bus = smbus.SMBus(1)
        except:
            raise ADCError("Error while initiating the PCF class.")

    def is_connected(self):
        """
        This tests to see if the connection was successful or not.
        """
        try:
            self.bus.write_byte(self.address, 0)
        except:
            raise ADCError("No ADC found.")

    def close(self):
        """
        This closes the ADC.
        """
        self.bus.close()

    def read(self, chn):
        """
        This reads the value from the specified channel on the ADC.
        """
        value = self.bus.read_byte_data(self.address, self.cmd+chn)
        return value

    def write(self, chn, value):
        """
        This writes a value to the specified channel on the ADC.
        """
        self.bus.write_byte_data(self.address, self.cmd+chn, value)
