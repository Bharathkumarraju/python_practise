import unittest
from area_of_cirle import area_of_circle
from math import pi

class cirlcleArea(unittest.TestCase):

    def test_radius_is_zero(self):
        result = area_of_circle(0)
        self.assertEqual(0,result)

    def test_radius_is_negative(self):
#        result = area_of_circle(-1)
        self.assertRaises(ValueError, area_of_circle, -1)

    def test_radius_is_one(self):
        result = area_of_circle(1)
        self.assertAlmostEqual(pi, result)

    def test_radius_is_string(self):
        self.assertRaises(TypeError, area_of_circle, "TESTING")

    def test_if_radius_greaterthan_one(self):
        result = area_of_circle(12)
        self.assertEqual(result, pi*12*12)

    def test_if_radius_is_complex(self):
        self.assertRaises(TypeError, area_of_circle, 2+5j)

    def test_if_radius_is_boolean(self):
        self.assertRaises(TypeError, area_of_circle, True)

