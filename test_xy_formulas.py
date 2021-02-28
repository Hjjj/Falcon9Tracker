#TestXYFormulas
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
        self.x1 = px
        self.y1 = py
        self.x2 = tx
        self.y2 = ty

#given 2 points, returns the angle from the pivot to the target
#also returns the distance from pivot to target
def calc_angle_and_dist(two_points):
    #use the points here
    bigY = two_points.y2 - two_points.y1
    bigX = two_points.x2 - two_points.x1
    distance = calculateDist(two_points)
    angle = calculateAngle(bigX, bigY)
    ad = AngleAndDistance(round(angle,2), round(distance,2))
    return ad

#bigX is the diff between two x's
#bigy is the diff between two y's
#given those two values we derive an angle 
#formula:
#bigY = targetY - pivotY
#bigX = targetX - pivotX
#Theta angle in radians = arcTan(bigY/bigX)
#Degrees = radians * 180/pi
def calculateAngle(bigX, bigY):
    #this is the situation where the line is vertical
    if bigX == 0:
        return 90
    #this is the situation where the line is horizontal so the 
    #value is either 0 or 180
    if bigY == 0:
        if(bigX > 0):
            return 180
        else:
            return 0
    
    one_eighty_divided_by_pi = 57.2957795131

    #arctan y/x gives you radians
    atan_val = math.atan(bigY/bigX)

    #radians * 180/pi gives you degrees
    degrees =  atan_val * one_eighty_divided_by_pi
    
    if degrees <= 0:
        return degrees * -1
    else:
        return 180 - degrees

#the classic distance between two points formula from 5th grade
def calculateDist(twopoints):
    xDiff = twopoints.x2 - twopoints.x1
    yDiff = twopoints.y2 - twopoints.y1

    return math.sqrt(xDiff**2 + yDiff**2)


#quick sanity checks
points = TwoPoints(10, -5, -10, -5)
a = calc_angle_and_dist(points)
print("Angle=" + str(a.angle) + " Distance=" + str(a.distance))

points = TwoPoints(10, -5, -8, 0)
a = calc_angle_and_dist(points)
print("Angle=" + str(a.angle) + " Distance=" + str(a.distance))

points = TwoPoints(10, -5, 9.5, 5)
a = calc_angle_and_dist(points)
print("Angle=" + str(a.angle) + " Distance=" + str(a.distance))

points = TwoPoints(10, -5, 10, 5)
a = calc_angle_and_dist(points)
print("Angle=" + str(a.angle) + " Distance=" + str(a.distance))

points = TwoPoints(10, -5, 10.3, 5)
a = calc_angle_and_dist(points)
print("Angle=" + str(a.angle) + " Distance=" + str(a.distance))

points = TwoPoints(10, -5, 11, 4.9)
a = calc_angle_and_dist(points)
print("Angle=" + str(a.angle) + " Distance=" + str(a.distance))

points = TwoPoints(10, -5, 20, -5)
a = calc_angle_and_dist(points)
print("Angle=" + str(a.angle) + " Distance=" + str(a.distance))


