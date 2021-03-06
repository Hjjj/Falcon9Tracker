import RPi.GPIO as GPIO
import time, sys
from enum import IntEnum

STEP_PIN = 21
DIR_PIN = 20
ENABL_PIN = 16

#160 steps in one revolution at current settings
STEPS_PER_REVOLUTION = 160

#on =0 because pin low enables board
class EnabledState(IntEnum):
    ENABLED = 0 
    DISABLED = 1

class Dir(IntEnum):
    CLOCKWISE = 0
    COUNTER = 1

def init_power_pins():

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(STEP_PIN, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(DIR_PIN, GPIO.OUT, initial=Dir.CLOCKWISE)
    #keep the stepper board off until ready to start
    GPIO.setup(ENABL_PIN, GPIO.OUT, initial=EnabledState.DISABLED)

def shutdown_driver_board():
    GPIO.output(STEP_PIN, GPIO.LOW)
    GPIO.output(DIR_PIN, GPIO.LOW)
    GPIO.output(ENABL_PIN, EnabledState.DISABLED)  

def rotate_n(rotations, speed, dir):

    counter = rotations * STEPS_PER_REVOLUTION
    GPIO.output(DIR_PIN, dir)
    
    while counter >= 0 :
        
        GPIO.output(STEP_PIN, 1)
        time.sleep(speed)
        GPIO.output(STEP_PIN, 0)
        counter = counter - 1

def enable_stepper_board(onoff):
    GPIO.output(ENABL_PIN, onoff)

#MAIN CODE

init_power_pins()
enable_stepper_board(EnabledState.ENABLED)

#.0005 is close to max speed i've found
STEP_DELAY = 0.0008 # 0.0005
#time.sleep(3)

rotate_n(10, STEP_DELAY, Dir.CLOCKWISE)
time.sleep(.5)
rotate_n(1, STEP_DELAY, Dir.COUNTER)
time.sleep(.5)
rotate_n(1, STEP_DELAY, Dir.CLOCKWISE)
time.sleep(.5)
rotate_n(1, STEP_DELAY, Dir.COUNTER)
time.sleep(.5)
rotate_n(1, STEP_DELAY, Dir.CLOCKWISE)
time.sleep(.5)
rotate_n(10, STEP_DELAY, Dir.COUNTER)

time.sleep(1)
enable_stepper_board(EnabledState.DISABLED)

shutdown_driver_board()



