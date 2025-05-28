import unittest
from add import add

class addition(unittest.TestCase):
    def test_if_entered_numbers_are_string(self):
        self.assertRaises(TypeError,add, "test1", "test2")

    def test_if_both_numbers_are_zero(self):
        result = add(0, 0)
        self.assertEqual(result, 0)

    def test_if_both_numbers_are_complex(self):
        self.assertRaises(TypeError, add, 2+3j, 5+6j)

    def test_if_both_numbers_are_boolean(self):
        self.assertRaises(TypeError, add, True, False)

    def test_if_both_numbers_are_float(self):
        result = add(1.56, 3.45)
        self.assertEqual(type(result), float)