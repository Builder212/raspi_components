import RPi.GPIO as GPIO

class arrow():
    arrow_pins={1:33,2:35,3:37,4:36}
    def __init__(self, which):
        self.pin = self.arrow_pins[which]
        GPIO.setup(self.pin,GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def on(self):
        GPIO.output(self.pin,GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin,GPIO.LOW)

if __name__ == "__main__":
    print("Program is starting... \n")

    from time import sleep

    a1 = arrow(1)
    a2 = arrow(2)
    a3 = arrow(3)
    a4 = arrow(4)

    try:
        while True:
            a1.on()
            a2.on()
            a3.on()
            a4.on()
            sleep(3)
            a1.off()
            a2.off()
            a3.off()
            a4.off()
            sleep(3)
    except KeyboardInterrupt:
        GPIO.cleanup()
