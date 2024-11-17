import unittest
from math_operations import add, subtract, multiply, divide

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-5, -5), 0)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertRaises(ValueError, divide, 10, 0)  # Test exception for divide by zero

# Run the tests when the script is executed
if __name__ == "__main__":
    unittest.main()
