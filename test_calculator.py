import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(-2, -4), 8)
    def test_divide(self):
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)
        self.assertEqual(divide(2, 4), 2)
        self.assertEqual(divide(5, 0), 0)
        self.assertEqual(divide(-2, 4), -2)
        self.assertEqual(divide(-2, -4), 2)
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(3, -4)
        with self.assertRaises(ValueError):
            logarithm(1, 4)
    def test_hypotenuse(self):
        self.assertEqual(hypothenuse(3, 4), 5)
        self.assertEqual(hypothenuse(5, 12), 13)
        self.assertEqual(hypothenuse(0, 6), 6)
    def test_sqrt(self):
        self.assertEqual(square_root(4), 2.0)
        self.assertEqual(square_root(9), 3.0)
        self.assertEqual(square_root(0), 0.0)
if __name__ == "__main__":
    unittest.main()