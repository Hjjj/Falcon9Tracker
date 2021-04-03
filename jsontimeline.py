#this file tests out a way to serialize and deserialize a timeline object to JSON
#in the future the timelines will be provided by a service in json form and this
#file tests how to handle them

import jsonpickle
from datetime import time, date, datetime

#this uses jsonpickle lib which is great at serializing and deserializing to JSON from native python
#https://jsonpickle.github.io/
#https://pynative.com/make-python-class-json-serializable/

#Timeline Data. Space delimited 
#010121020100 001 002 34.56,23.54
#int timestamp  - Jan 1, 2020 2:01 AM       //MMDDYYhhmmss
#int obj id     - 001 'First stage servo'   //the id of an object
#int verb       - 002 'move to coord'       //the id of a verb
#str data       - Angle:34.56 Dist:23.54 km //data the verb needs in whatever format
#crlf

#the timeline is an array of TimelineEvent objects.
#the main program will roll through the timeline and produce an action for each tick of the clock where there
# is an associated TimelineEvent.
#Fields:
#time - a time object, midnite 00:00:00 is the beginning of the timeline
#noun - the unique id of a servo, stepper motor, an led etc. 
#verb - the unique id of an action on the noun such as 'step fwd', 'turn on' etc
#verb_params - commands related to the verb, for example if the following was set on a timeline object:
# time is 00:00:15
# noun is servo 3
# verb is moveto
# verb_params is 120
# comment is "Servo swing to 120 degrees"
# The meaning of the above is that at 15 seconds into the timeline, servo 3 should be moved to 120 degrees.  


class TimelineEvent:

    def __init__(self, time, noun, verb, verb_params, comment):
        self.time = time
        self.noun = noun
        self.verb = verb
        self.verb_params = verb_params 
        self.comment = comment

    

class Launch:

    def __init__(self, launch_datetime, name, comments, timeline=None):
        self.launch_datetime = launch_datetime
        self.name = name
        self.comments = comments
        
        if(timeline is None):
            self.timeline = []
        else:
            self.timeline = timeline    

    def timeline_insert(self, timeline_event):        
        self.timeline.append(timeline_event)


#sample:
# mission_data = {
#     "t_minus__zero" : datetime.datetime.now(),
#     "launch_name" : "RSO 3",
#     "launch_details" : "3rd flight of booster 211",
#     "timeline" : [
#         (datetime.time(0,0,0), 1, 67, "on"),
#         (datetime.time(0,0,0), 1, 2, "34.56,23.54"),
#         (datetime.time(0,0,0), 2, 2, "34.56,23.54"),
#         (datetime.time(0,0,2), 1, 2, "34.59,23.54"),
#         (datetime.time(0,0,10), 2, 2, "34.80,23.54"),
#         (datetime.time(0,0,16), 1, 2, "34.70,23.53"),
#         (datetime.time(0,0,17), 2, 2, "34.46,23.54"),
#         (datetime.time(0,0,20), 1, 2, "34.56,23.54"),
#         (datetime.time(0,0,28), 8, 8, "off"),
#         (datetime.time(0,0,30), 13, 55, "87.34"),
#         (datetime.time(0,0,35), 1, 2, "34.56,23.54")
#     ]
# }

launch = Launch(datetime(year=2020, month=1, day=31, hour=13, minute=14, second=31), "Hal001 Flight", "just a test flight")

#evt = TimelineEvent(time(hour=0, minute=0, second=0), 111, 222, "1,2,3,4", "test event")
tim = time(hour=0, minute=0, second=0)

launch.timeline_insert(TimelineEvent(tim, 111, 222, "1,2,3,4", "test event"))
launch.timeline_insert(TimelineEvent(tim, 222, 666, "1,2,3,4", "test event"))
launch.timeline_insert(TimelineEvent(tim, 333, 333, "1,2,3,4", "test event"))
launch.timeline_insert(TimelineEvent(tim, 444, 999, "1,2,3,4", "test event"))
launch.timeline_insert(TimelineEvent(tim, 555, 111, "1,2,3,4", "test event"))
launch.timeline_insert(TimelineEvent(tim, 666, 333, "1,2,3,4", "test event"))
launch.timeline_insert(TimelineEvent(tim, 777, 555, "1,2,3,4", "test event"))
launch.timeline_insert(TimelineEvent(tim, 888, 888, "1,2,3,4", "test event"))
launch.timeline_insert(TimelineEvent(tim, 999, 111, "1,2,3,4", "test event"))
launch.timeline_insert(TimelineEvent(tim, 000, 222, "1,2,3,4", "test event"))


launch_pickle_encoded = jsonpickle.encode(launch, unpicklable=True)
print("Encoded string:")
print(launch_pickle_encoded)

launch_pickle_decoded = jsonpickle.decode(launch_pickle_encoded)
print("Decoded string:")
print("launch.name = " + launch.name + " and launch_pickle_decoded.name= " + launch_pickle_decoded['name'])

