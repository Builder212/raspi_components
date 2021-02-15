from .joystick import Joystick
from time import sleep

class JoystickTest:
    def __init__():
        """
        This is the test class for the Joystick class.
        To use this, run JoystickTest.test(xChannel, yChannel, zPin).
        """
        pass

    @classmethod
    def test(self, chn):
        """
        This will print the value of x, y, and z in a loop.
        """
        joystick = Joystick(1, 0, 12)

        try:
            while True:
                x, y, z = joystick.read()
                print('x: {}, y: {}, z: {}'.format(x,y,z)
                sleep(0.1)
        except KeyboardInterrupt:
            joystick.close()
