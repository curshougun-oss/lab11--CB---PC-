
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-2, 3), 1)

    def test_subtract(self):
        self.assertEqual(subtract(2, 3), -1)
        self.assertEqual(subtract(-2, 3), -5)
        self.assertEqual(subtract(-2, -3), 1)

    ######### Partner 1
    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(5, 0), 0)
        self.assertEqual(mul(-2, 3), -6)
        self.assertEqual(mul(-2, -4), 8)

    def test_divide(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
        self.assertEqual(div(2, 4), 2)
        self.assertEqual(div(5, 0), 0)
        self.assertEqual(div(-2, 4), -2)
        self.assertEqual(div(-2, -4), 2)

    ######### Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertEqual(logarithm(10, 100), 2)
        self.assertEqual(logarithm(2, 64), 6)
        self.assertEqual(logarithm(10, 10000000), 7)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(-8, 6)

    ######### Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(3, -4)
        with self.assertRaises(ValueError):
            logarithm(1, 4)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(0, 6), 6)

    def test_sqrt(self):
        self.assertEqual(square_root(4), 2.0)
        self.assertEqual(square_root(9), 3.0)
        self.assertEqual(square_root(0), 0.0)

# Do not touch this
if __name__ == "__main__":
    unittest.main()