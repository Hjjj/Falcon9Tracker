import xy_formulas

pivotX = 50
pivotY = -50

for x in range(-100, 200):
    points = xy_formulas.TwoPoints(pivotX, pivotY, x, 0)
    print(xy_formulas.angle_of(points), 'degrees, ', xy_formulas.distance_between_points(points), ' km')