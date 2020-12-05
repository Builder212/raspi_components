import RPi.GPIO as GPIO
from time import sleep

class Adafruit_CharLCD(object):
    # commands
    clear_display = 0x01
    return_home = 0x02
    entry_mode_set = 0x04
    display_control_type = 0x08
    cursor_shift = 0x10
    set_ddramaddr = 0x80

    # flags for display entry mode
    entry_left = 0x02
    entry_shift_increment = 0x01
    entry_shift_decrement = 0x00

    # flags for display on/off control
    display_on = 0x04
    cursor_on = 0x02
    cursor_off = 0x00
    blink_on = 0x01
    blink_off = 0x00

    # flags for display/cursor shift
    display_move = 0x08
    move_right = 0x04
    move_left = 0x00

    # flags for function set
    four_bit_mode = 0x00
    two_line = 0x08
    one_line = 0x00

    def __init__(self, pin_rs=25, pin_e=24, pins_db=[23, 17, 21, 22]):
        GPIO.setwarnings(False)
        self.GPIO = GPIO
        self.pin_rs = pin_rs
        self.pin_e = pin_e
        self.pins_db = pins_db

        self.GPIO.setmode(GPIO.BCM)
        self.GPIO.setup(self.pin_e, GPIO.OUT)
        self.GPIO.setup(self.pin_rs, GPIO.OUT)

        for pin in self.pins_db:
            self.GPIO.setup(pin, GPIO.OUT)

        self.write4bits(0x33)  # initialization
        self.write4bits(0x32)  # initialization
        self.write4bits(0x28)  # 2 line 5x7 matrix
        self.write4bits(0x0C)  # turn cursor off 0x0E to enable cursor
        self.write4bits(0x06)  # shift cursor right

        self.display_control = self.display_on | self.cursor_off | self.blink_off

        self.display_function = self.four_bit_mode | self.one_line | 0x00
        self.display_function |= self.two_line

        # Initialize to default text direction (for romance languages)
        self.display_mode = self.entry_left | self.entry_shift_decrement
        self.write4bits(self.entry_mode_set | self.display_mode)
        self.clear()

    def begin(self, cols, lines):
        if (lines > 1):
            self.numlines = lines
            self.display_function |= self.two_line

    def home(self): # set cursor position to zero
        self.write4bits(self.return_home)
        self.delayMicroseconds(3000)

    def clear(self):
        self.write4bits(self.clear_display)
        self.delayMicroseconds(3000)

    def setCursor(self, col, row):
        self.row_offsets = [0x00, 0x40, 0x14, 0x54]
        if row > self.numlines:
            row = self.numlines - 1
        self.write4bits(self.set_ddramaddr | (col + self.row_offsets[row]))

    def noDisplay(self):
        """ Turn the display off (quickly) """
        self.display_control &= ~self.display_on
        self.write4bits(self.display_control_type | self.display_control)

    def display(self):
        """ Turn the display on (quickly) """
        self.display_control |= self.display_on
        self.write4bits(self.display_control_type | self.display_control)

    def noCursor(self): # Turns the underline cursor off
        self.display_control &= ~self.cursor_on
        self.write4bits(self.display_control_type | self.display_control)

    def cursor(self): # Turns the underline cursor on
        self.display_control |= self.cursor_on
        self.write4bits(self.display_control_type | self.display_control)

    def noBlink(self): # Turn the blinking cursor off
        self.display_control &= ~self.blink_on
        self.write4bits(self.display_control_type | self.display_control)

    def blink(self): # Turn the blinking cursor on
        self.display_control |= self.blink_on
        self.write4bits(self.display_control_type | self.display_control)

    def DisplayLeft(self):
        """ These commands scroll the display without changing the RAM """
        self.write4bits(self.cursor_shift | self.display_move | self.move_left)

    def scrollDisplayRight(self):
        """ These commands scroll the display without changing the RAM """
        self.write4bits(self.cursor_shift | self.display_move | self.move_right)

    def leftToRight(self):
        """ This is for text that flows Left to Right """
        self.display_mode |= self.entry_left
        self.write4bits(self.entry_mode_set | self.display_mode)

    def rightToLeft(self):
        """ This is for text that flows Right to Left """
        self.display_mode &= ~self.entry_left
        self.write4bits(self.entry_mode_set | self.display_mode)

    def autoscroll(self):
        """ This will 'right justify' text from the cursor """
        self.display_mode |= self.entry_shift_increment
        self.write4bits(self.entry_mode_set | self.display_mode)

    def noAutoscroll(self):
        """ This will 'left justify' text from the cursor """
        self.display_mode &= ~self.entry_shift_increment
        self.write4bits(self.entry_mode_set | self.display_mode)

    def write4bits(self, bits, char_mode=False):
        """ Send command to LCD """
        self.delayMicroseconds(1000)
        bits = bin(bits)[2:].zfill(8)
        self.GPIO.output(self.pin_rs, char_mode)
        for pin in self.pins_db:
            self.GPIO.output(pin, False)
        for i in range(4):
            if bits[i] == "1":
                self.GPIO.output(self.pins_db[::-1][i], True)
        self.pulseEnable()
        for pin in self.pins_db:
            self.GPIO.output(pin, False)
        for i in range(4, 8):
            if bits[i] == "1":
                self.GPIO.output(self.pins_db[::-1][i-4], True)
        self.pulseEnable()

    def delayMicroseconds(self, microseconds):
        seconds = microseconds / float(1000000)
        sleep(seconds)

    def pulseEnable(self):
        self.GPIO.output(self.pin_e, False)
        self.delayMicroseconds(1)
        self.GPIO.output(self.pin_e, True)
        self.delayMicroseconds(1)
        self.GPIO.output(self.pin_e, False)
        self.delayMicroseconds(1)

    def message(self, text):
        """ Send string to LCD. Newline wraps to second line"""
        for char in text:
            if char == '\n':
                self.write4bits(0xC0)  # next line
            else:
                self.write4bits(ord(char), True)


if __name__ == '__main__':
    lcd = Adafruit_CharLCD()
    lcd.clear()
    lcd.message("  Adafruit 16x2\n  Standard LCD")
