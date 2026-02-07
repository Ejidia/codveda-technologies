import unittest
from calculator import add, subtract, multiply, divide, perform_calculation


class TestCalculator(unittest.TestCase):
    """Test cases for the calculator operations."""
    
    def test_addition(self) -> None:
        """Test addition operation."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(10.5, 2.5), 13.0)
    
    def test_subtraction(self) -> None:
        """Test subtraction operation."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(10.5, 2.5), 8.0)
    
    def test_multiplication(self) -> None:
        """Test multiplication operation."""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(1.5, 2.5), 3.75)
    
    def test_division(self) -> None:
        """Test division operation."""
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(-6, 3), -2)
        self.assertEqual(divide(0, 5), 0)
    
    def test_division_by_zero(self) -> None:
        """Test division by zero raises ValueError with correct message."""
        with self.assertRaises(ValueError) as context:
            divide(5, 0)
        self.assertIn("Division by zero", str(context.exception))
    
    def test_perform_calculation_addition(self) -> None:
        """Test perform_calculation with addition."""
        self.assertEqual(perform_calculation(5, 3, '+'), 8)
    
    def test_perform_calculation_subtraction(self) -> None:
        """Test perform_calculation with subtraction."""
        self.assertEqual(perform_calculation(5, 3, '-'), 2)
    
    def test_perform_calculation_multiplication(self) -> None:
        """Test perform_calculation with multiplication."""
        self.assertEqual(perform_calculation(5, 3, '*'), 15)
    
    def test_perform_calculation_division(self) -> None:
        """Test perform_calculation with division."""
        self.assertEqual(perform_calculation(6, 3, '/'), 2)
    
    def test_perform_calculation_invalid_operation(self) -> None:
        """Test perform_calculation with invalid operation."""
        with self.assertRaises(ValueError) as context:
            perform_calculation(5, 3, '%')
        self.assertIn("Invalid operation", str(context.exception))
    
    def test_perform_calculation_division_by_zero(self) -> None:
        """Test perform_calculation handles division by zero."""
        with self.assertRaises(ValueError) as context:
            perform_calculation(5, 0, '/')
        self.assertIn("Division by zero", str(context.exception))

if __name__ == '__main__':
    unittest.main()
