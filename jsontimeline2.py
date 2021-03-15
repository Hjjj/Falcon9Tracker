import json 
from datetime import time, date, datetime

#Timeline Data. Space delimited 
#010121020100 001 002 34.56,23.54
#int timestamp  - Jan 1, 2020 2:01 AM       //MMDDYYhhmmss
#int obj id     - 001 'First stage servo'   //the id of an object
#int verb       - 002 'move to coord'       //the id of a verb
#str data       - Angle:34.56 Dist:23.54 km //data the verb needs in whatever format
#crlf

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

#def myconverter(o):
#    if isinstance(o, datetime.datetime):
#       return o.__str__()

# convert into JSON:
#y = json.dumps(mission_data, default = myconverter)

# the result is a JSON string:
#print(y)

launch = Launch(datetime(year=2020, month=1, day=31, hour=13, minute=14, second=31), "Hal001 Flight", "just a test flight")

#evt = TimelineEvent(time(hour=0, minute=0, second=0), 111, 222, "1,2,3,4", "test event")
tim = time(hour=0, minute=0, second=0)

launch.timeline_insert(TimelineEvent(tim, 111, 222, "1,2,3,4", "test event"))

y = json.dumps(launch)

# the result is a JSON string:
print(y)

