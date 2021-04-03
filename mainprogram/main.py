#The main program of the Falcon 9 Tracker
#The main purpose of this file is to:
#Obtain the JSON timeline file from remote service
#Roll through the timeline array, triggering hardware events


#Constants
SERVO_FIRST_STAGE = 0
SERVO_SECOND_STAGE = 1
LED_FIRST_STAGE_ENGINE = 2
LED_SECOND_STAGE_ENGINE = 3
STEPPER_FIRST_STAGE = 4
STEPPER_SECOND_STAGE = 5

VERB_SET_ANGLE = 1
VERB_LED_ON = 2
VERB_LED_OFF = 3
VERB_SET_DISTANCE = 4 #length of arm in mm

initializeHardware()
flight_data = retrieveFlightData()
initializeDisplay(flight_data)
launch_mission(flight_data.timeline)

def initializeHardware():
    #set all positions to begining


def retrieveFlightData():
    #pull flight data from a service and convert from json to py array

def initializeDisplay(flight_data):
    #show initial data to user
    #data from the flightdata object

def launch_mission(timeline):
    #play the timeline






