import threading
import RPi.GPIO as GPIO
import time


#System Summary - hardware in the system
#First Stage Angle Arm
#First Stage Distance Screw
#First Stage Engine LED

#Second Stage Angle Arm
#Second Stage Distance Screw
#First Stage Engine LED

#Status Screen

#Timeline Data. Space delimited 
#010121020100 001 002 34.56,23.54
#int timestamp  - Jan 1, 2020 2:01 AM       //MMDDYYhhmmss
#int obj id     - 001 'First stage servo'   //the id of an object
#int verb       - 002 'move to coord'       //the id of a verb
#str data       - Angle:34.56 Dist:23.54 km //data the verb needs in whatever format
#crlf

#Threads Needed
#Main Thread

#First Stage Distance Screw 
#Second Stage Distance Screw 

#Screen needs thread? [research]













GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class LEDThread (threading.Thread):

    def __init__(self, loop_ct, LED_PIN, time_on, time_off):
        threading.Thread.__init__(self)
        self.loop_ct = loop_ct
        self.LED_PIN = LED_PIN
        self.time_on = time_on
        self.time_off = time_off
        self.runit = True
        GPIO.setup(self.LED_PIN, GPIO.OUT, initial=GPIO.LOW) 
       
    def stop(self):
        self.runit = False
        
    def run(self):
        print ("Starting LED number" + str(self.LED_PIN))
        
        count = 0

        while (count < self.loop_ct and self.runit):
            GPIO.output(self.LED_PIN, GPIO.LOW)
            time.sleep(self.time_off)

            GPIO.output(self.LED_PIN, GPIO.HIGH)
            time.sleep(self.time_on)
            count = count + 1

        GPIO.output(self.LED_PIN, GPIO.LOW)


class ServoThread (threading.Thread):
    def __init__(self, GPIO_PIN, degrees_from, degrees_to, degrees_step):
        threading.Thread.__init__(self)
        self.GPIO_PIN = GPIO_PIN
        
        self.degrees_from = degrees_from

        if self.degrees_from < 0 or self.degrees_from > 180:
            self.degrees_from = 0

        self.degrees_to = degrees_to

        if self.degrees_to > 180 or self.degrees_to < 0:
            self.degrees_to =  180

        if self.degrees_to - self.degrees_from < 0:
            self.degrees_from = 0
            self.degrees_to = 180

        self.degrees_step = degrees_step

        if self.degrees_step > self.degrees_to - self.degrees_from:
            self.degrees_step = self.degrees_to - self.degrees_from

        if self.degrees_step < 1:
            self.degrees_step = 1


        self.runit = True
        GPIO.setup(self.GPIO_PIN, GPIO.OUT, initial=GPIO.LOW)
        self.pwm_pin = GPIO.PWM(self.GPIO_PIN, 50) #frequency=50Hz
       
    def stop(self):
        self.runit = False
        
    def run(self):
        print("Starting servo thread on pin #" + str(self.GPIO_PIN))
        self.pwm_pin.start(0)
  
        for degrees in range(self.degrees_from, self.degrees_to, self.degrees_step):

            self.set_angle(degrees, self.pwm_pin)
            time.sleep(1)

        self.pwm_pin.ChangeDutyCycle(5)
        time.sleep(2)
        self.pwm_pin.stop()

    def set_angle(self, angle, pwm):
        duty = round(angle / 18 + 2, 2)
        pwm.ChangeDutyCycle(duty)

# Create new threads
LED23 = LEDThread(20, 23, 0.1, 0.1)
LED13 = LEDThread(10, 13, 0.5, 0.5)
LED18 = ServoThread(18, 1, 180, 10) 

# Execute the threads
LED23.start()
LED13.start()
LED18.start()

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt: 
    LED23.stop()
    LED13.stop()
    LED18.stop()
    print("wait for threads to terminate")
    LED23.join( )
    LED13.join( )
    LED18.join( )
    
GPIO.cleanup()   

print("End")