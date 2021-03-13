import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)
servo0 = kit.servo[0]

servo0.actuation_range = 180
servo0.set_pulse_width_range(700, 2610)

servo0.angle = 180
time.sleep(1)
servo0.angle = 0
time.sleep(1)
servo0.angle = 90

for x in range(180,0, -5):
    servo0.angle = (x)
    time.sleep(0.1)

time.sleep(1)
servo0.angle = 90

""" fraction = 0.0
while fraction < 1.0:
    servo0.fraction = fraction
    fraction += 0.01
    time.sleep(0.01) """


