import RPi.GPIO as GPIO
import time

class servo:
    def __init__(self, pin=12):
        self.offset_duty = 0.5
        self.min_duty = 2.5+self.offset_duty
        self.max_duty = 12.5+self.offset_duty
        self.pin = pin

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

        p = GPIO.PWM(self.pin, 50)
        p.start(0)

    def map(self, value, fromLow, fromHigh, toLow, toHigh):
        return (toHigh-toLow)*(value-fromLow)/(fromHigh-fromLow)+toLow

    def servoWrite(self, angle):
        if(angle<0):
            angle = 0
        elif(angle > 180):
            angle = 180
            p.ChangeDutyCycle(self.map(angle, 0, 180, self.min_duty, self.max_duty))

if __name__ == '__main__':
    print ('Program is starting...')
    servo = servo()
    try:
        servo.servoWrite(180)
    except KeyboardInterrupt:
        GPIO.cleanup()
