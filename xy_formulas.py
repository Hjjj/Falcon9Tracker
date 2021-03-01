#XYFormulas and utilities
import math

#Holds one angle in degrees from 0 to 180
#0 represents a target to the far left
#180 represents a target to the far right
#90 represents a target straight up
class AngleAndDistance:
    def __init__(self, angle, distance):
        self.angle = angle
        self.distance = distance

#two x,y points
class TwoPoints:
    def __init__(self, px, py, tx, ty):
        #x1,y1 are pivot point
        self.x1 = px
        self.y1 = py
        #x2y2 are target point
        self.x2 = tx
        self.y2 = ty

#given 2 points, returns the angle from the pivot to the target
#also returns the distance from pivot to target
def angle_and_dist(point_pair):
    distance = distance_between_points(point_pair)
    angle = angle_of(point_pair)

    ad = AngleAndDistance(angle, distance)
    return ad

#pointpair, the two points in 2d space
#given those two values we derive an angle 
#formula:
#point_pair pivot point and target point wrapped in a simple class
#Theta angle in radians = arcTan(bigY/bigX)
#Degrees = radians * 180/pi
def angle_of(point_pair):
    
    if point_pair.x1 == point_pair.x2 and point_pair.y1 == point_pair.y2:
        raise ValueError("Both points are the same. No angle possible.")

    if point_pair.y2 < 0 :
        raise ValueError("Y of target point cannot be below 0.")    
    
    #x1,y1 is pivot point
    #x2,y2 is target point
    x_diff = point_pair.x2 - point_pair.x1
    y_diff = point_pair.y2 - point_pair.y1

    #this is the situation where the line is vertical
    if x_diff == 0:
        return 90

    #this is the situation where the line is horizontal so the 
    #value is either 0 or 180
    if y_diff == 0:
        if(x_diff > 0):
            return 180
        else:
            return 0
    
    one_eighty_divided_by_pi = 57.2957795131

    #arctan y/x gives you radians
    atan_val = math.atan(y_diff/x_diff)

    #radians * 180/pi gives you degrees
    degrees =  round(atan_val * one_eighty_divided_by_pi, 1)
    
    if degrees <= 0:
        return degrees * -1
    else:
        return 180 - degrees

#the classic distance between two points formula from 5th grade
def distance_between_points(point_pair):
    xDiff = point_pair.x2 - point_pair.x1
    yDiff = point_pair.y2 - point_pair.y1

    return round(math.sqrt(xDiff**2 + yDiff**2), 2)