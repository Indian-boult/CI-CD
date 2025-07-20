"""
Unit tests for the calculator module.

This demonstrates how testing is integrated into CI/CD pipelines.
"""

import unittest
from calculator import add, subtract, multiply, divide, power


class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""

    def test_add(self):
        """Test addition function."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        """Test subtraction function."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 1), 0)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self):
        """Test multiplication function."""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        """Test division function."""
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(-6, 2), -3)

        # Test division by zero
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_power(self):
        """Test power function."""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(2, -1), 0.5)


if __name__ == "__main__":
    unittest.main()
