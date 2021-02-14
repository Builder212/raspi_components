import smbus
from ADC_errors import ADCError

class PCF():
    def __init__(self):
        self.cmd = 0x40
        self.address = 0x48
        try:
            self.bus = smbus.SMBus(1)
        except:
            raise ADCError("Error while initiating the PCF class.")

    def is_connected(self):
        try:
            self.bus.write_byte(self.address, 0)
        except:
            raise ADCError("No ADC found.")

    def close(self):
        self.bus.close()

    def read(self, chn):
        value = self.bus.read_byte_data(self.address, self.cmd+chn)
        return value

    def write(self, value):
        self.bus.write_byte_data(address,cmd,value)
