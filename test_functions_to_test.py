import unittest
from functions_to_test import Calculator


class TestForCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(Calculator.divide(10, 5), 2)
        self.assertRaises(ValueError, Calculator.divide, 10, 0)
