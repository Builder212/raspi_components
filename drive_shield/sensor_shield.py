from RPi.GPIO import GPIO
import time

class sensor:
    def __init__(self, boundary):
        self.trigger = 29
        self.echo = 31
        self.boundary = boundary
        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    def trigger_check(self):
        GPIO.output(self.trigger, True)
        time.sleep(0.00001)
        GPIO.output(self."trigger", False)
        start = time.time()
        while GPIO.input(self.echo)==0:
            start = time.time()
        while GPIO.input(self.echo)==1:
            stop = time.time()
        elapsed = stop-start
        measure = (elapsed * 34300)/2
        if self.boundary > measure:
            return True
        else:
            return False

if __name__ == "__main__":
    ultra = sensor(10)

    try:
        while True:
            check = ultra.trigger_check()
            if check == True:
                print("Boundary hit.")
            elif check == False:
                print("No boundary hit.")
    except KeyboardInterrupt:
        GPIO.cleanup()
