import RPi.GPIO as GPIO
import time, datetime, os

class dht():
    def __init__(self, pin):
        self.pin = int(pin)
        self.bits = [0, 0, 0, 0, 0]
        GPIO.setmode(GPIO.BOARD)
        self.humidity = 0
        self.temperature = 0
        self.dht_wakeup = 0.020
        self.dht_timeout = 0.0001
        self.dht_ok = 0
        self.dht_error_timeout = -2
        self.dht_error_check = -1

    def read_sensor(self, pin): #read and check for errors in the dht data return
        mask = 0x80
        idx = 0
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(self.dht_wakeup)
        GPIO.output(pin, GPIO.HIGH)
        GPIO.setup(pin, GPIO.IN)
        loopCnt = self.dht_timeout
        t = time.time()
        while(GPIO.input(pin) == GPIO.LOW):
                if((time.time() - t) > loopCnt):
                    return self.dht_error_timeout
        t = time.time()
        while(GPIO.input(pin) == GPIO.HIGH):
            if((time.time() - t) > loopCnt):
                return self.dht_error_timeout
        for i in range(0, 40, 1):
            t = time.time()
            while(GPIO.input(pin) == GPIO.LOW):
                if((time.time() - t) > loopCnt):
                    return self.dht_error_timeout
            t = time.time()
            while(GPIO.input(pin) == GPIO.HIGH):
                if((time.time() - t) > loopCnt):
                    return self.dht_error_timeout
                if((time.time() - t) > 0.00005):
                    self.bits[idx] |= mask
            mask >>= 1
            if(mask == 0):
                mask = 0x80
                idx += 1
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
        return self.dht_ok

    def read_dht(self): #process and return humidity and temperature
        read_dht = self.read_sensor(self.pin)
        while (read_dht is not self.dht_ok):
            error_string = ""
            if read_dht == self.dht_error_check:
                error_string = "Checking Error"
            elif read_dht == self.dht_error_timeout:
                error_string = "Timeout Error"
            file_name = "dht_error.txt"
            if os.path.isfile(file_name) == False:
                log = open(file_name, "w")
                time = datetime.datetime.now()
                log.write("Error occured at %s\n" % time)
                log.write(error_string+"\n")
                log.close()
            elif os.path.isfile(file_name) == True:
                log = open(file_name, "a")
                time = datetime.datetime.now()
                log.write("Error occured at %s\n" % time)
                log.write(error_string+"\n")
                log.close()
            else:
                log_file = os.path.isfile(file_name)
                print("Error, bad result given from 'os.path.exsists(%s)', expected True or False, but was given %s\n" %(file_name, log_file))
                read_dht = self.read_sensor(self.pin, dht_wakeup)
        self.humidity = self.bits[0]
        self.temperature = self.bits[2] + self.bits[3]*0.1
        bit_add = self.bits[0] + self.bits[1] + self.bits[2] + self.bits[3]
        sum_check = (bit_add & 0xFF)
        if(self.bits[4] is not sum_check):
            read_dht()
        if read_dht == self.dht_ok:
            return self.humidity, self.temperature

if __name__ == "__main__":
    print("Program is starting... \n")
    pin = input("What pin is your DHT going to be read from? ")
    print("\n")
    dht = dht(pin)

    try:
        while True:
            hum, temp = DHT.read_dht()
            print("Temperature: %d\nHumidity %d" %(temp, hum))
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()

#come back to this, I believe my dht is faulty
