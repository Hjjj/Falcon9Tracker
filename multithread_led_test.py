import threading
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#LED_PIN = 18 dimming with PWM
#LED_PIN = 13 blinking
#LED_PIN = 23 blinking

class myThread (threading.Thread):
    def __init__(self, LED_PIN, time_on, time_off):
        threading.Thread.__init__(self)
        self.LED_PIN = LED_PIN
        self.time_on = time_on
        self.time_off = time_off
        ###ghp### added
        self.runit = True
    
    ###ghp### added    
    def stop(self):
        self.runit = False
        
    def run(self):
        print "Starting LED number" + str(self.LED_PIN)
        # Initial state for LEDs:
        ###ghp###: changed: set mode only once
        #GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
        
        #GPIO.output(self.LED_PIN, GPIO.LOW)
        count = 0
        ###ghp### removed exception handling; listen to runit-flag
        #try:
        while (count < 50 and self.runit):
            GPIO.setup(self.LED_PIN, GPIO.OUT) # LED pin set as output
            GPIO.output(self.LED_PIN, GPIO.LOW)
            time.sleep(self.time_off)
            GPIO.setup(self.LED_PIN, GPIO.OUT) # LED pin set as output
            GPIO.output(self.LED_PIN, GPIO.HIGH)
            time.sleep(self.time_on)
            count = count + 1
            ###ghp###: changed: set mode only once
            #GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
            
            GPIO.setup(self.LED_PIN, GPIO.OUT) # LED pin set as output
            GPIO.output(self.LED_PIN, GPIO.LOW)
            ###ghp###: identation unclear, do this in main code only
            #GPIO.cleanup()
            #GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

        #except KeyboardInterrupt: # IF CTRL + C is pressed, exit cleanly:
        #    print "Manual intervention for some reason"

class myThread1 (threading.Thread):
    def __init__(self, LED_PIN, STEP_pos, STEP_neg):
        threading.Thread.__init__(self)
        self.LED_PIN = LED_PIN
        self.STEP_pos = STEP_pos
        self.STEP_neg = STEP_neg
        
        ###ghp### added
        self.runit = True
    
    ###ghp### added    
    def stop(self):
        self.runit = False
        
    def run(self):
        print "Starting dimming LED number" + str(self.LED_PIN)
        # Initial state for LEDs:
        
        ###ghp###: changed: set mode only once
        #GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
       
        GPIO.setup(self.LED_PIN, GPIO.OUT) # LED pin set as output
        GPIO.output(self.LED_PIN, GPIO.LOW)
        p = GPIO.PWM(self.LED_PIN, 50) # channel=12 frequency=50Hz

        count = 0
        p.start(0)
        ###ghp### removed keyboard exception handline; listen to runit-flag
        #try:
        while (count < 6 and self.runit):
            for dc in range(0, 101, self.STEP_pos):
                p.ChangeDutyCycle(dc)
                time.sleep(0.1)
            for dc in range(100, -1, self.STEP_neg):
                p.ChangeDutyCycle(dc)
                time.sleep(0.1)
            count = count + 1

        #except KeyboardInterrupt: # IF CTRL + C is pressed, exit cleanly:
        #    print "Manual intervention for some reason"
        p.stop()
        ###ghp###: cleanup only in main code
        #GPIO.cleanup()

# Create new threads
LED23 = myThread(23,0.1,0.1)
LED13 = myThread(13,1,1)
LED18 = myThread1(18,5,-5) # Dimming LED on GPIO 18

# Execute the threads
LED23.start()
LED13.start()
LED18.start()

###ghp### added
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