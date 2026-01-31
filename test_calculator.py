import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    """Test cases for the calculator operations"""
    
    def test_addition(self):
        """Test addition operation"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(10.5, 2.5), 13.0)
    
    def test_subtraction(self):
        """Test subtraction operation"""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(10.5, 2.5), 8.0)
    
    def test_multiplication(self):
        """Test multiplication operation"""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(1.5, 2.5), 3.75)
    
    def test_division(self):
        """Test division operation"""
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(-6, 3), -2)
        self.assertEqual(divide(0, 5), 0)
    
    def test_division_by_zero(self):
        """Test division by zero raises ValueError"""
        with self.assertRaises(ValueError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()
gi