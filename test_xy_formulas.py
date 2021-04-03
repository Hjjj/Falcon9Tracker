#Unit tests of the custom-written xy_formulas library. 

import unittest
import xy_formulas

class TestXyFormulas(unittest.TestCase):

    #ANGLES

    def test_Fortyfive_angles(self):
        point_pair = xy_formulas.TwoPoints(0,0,10,10)
        self.assertEqual(xy_formulas.angle_of(point_pair), 135)

        point_pair = xy_formulas.TwoPoints(0,0,-10,10)
        self.assertEqual(xy_formulas.angle_of(point_pair), 45)

    def test_angles_flat(self):
        #left flat
        point_pair = xy_formulas.TwoPoints(0,0,-10,0)
        self.assertEqual(xy_formulas.angle_of(point_pair), 0)
        #right flat
        point_pair = xy_formulas.TwoPoints(0,0, 10,0)
        self.assertEqual(xy_formulas.angle_of(point_pair), 180)

    def test_vertical(self):
        point_pair = xy_formulas.TwoPoints(1,0, 1,20)
        self.assertEqual(xy_formulas.angle_of(point_pair), 90)        

    def test_same_point(self):
        point_pair = xy_formulas.TwoPoints(1,1, 1,1)
        with self.assertRaises(ValueError):
            xy_formulas.angle_of(point_pair)

    def test_invalid_region_below_horizon(self):
        point_pair = xy_formulas.TwoPoints(0,0,0,-10)
        with self.assertRaises(ValueError):
            xy_formulas.angle_of(point_pair)

    def test_invalid_region_below_horizon2(self):
        point_pair = xy_formulas.TwoPoints(-5,7, -10,-1)
        with self.assertRaises(ValueError):
            xy_formulas.angle_of(point_pair)

    ##Distance

    def test_distance_flat(self):
        point_pair = xy_formulas.TwoPoints(1,1,11,1) 
        self.assertEqual(xy_formulas.distance_between_points(point_pair), 10)

        point_pair = xy_formulas.TwoPoints(1,1,-11,1) 
        self.assertEqual(xy_formulas.distance_between_points(point_pair), 12)     

    def test_distance_zero(self):
        point_pair = xy_formulas.TwoPoints(1,1,1,1)
        self.assertEqual(xy_formulas.distance_between_points(point_pair), 0)

    def test_distance_sixes(self):
        point_pair = xy_formulas.TwoPoints(6,0,0,6)
        self.assertEqual(xy_formulas.distance_between_points(point_pair), 8.49)       

        point_pair = xy_formulas.TwoPoints(0,6,6,0)
        self.assertEqual(xy_formulas.distance_between_points(point_pair), 8.49)  

    ##Angle AND Dist Function

    def test_a_and_d(self):
        point_pair = xy_formulas.TwoPoints(0,0,10,10)
        ad = xy_formulas.angle_and_dist(point_pair)
        self.assertEqual(ad.distance, 14.14)
        self.assertEqual(ad.angle, 135)

if __name__ == '__main__':
    unittest.main()

