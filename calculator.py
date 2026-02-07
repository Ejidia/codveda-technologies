from typing import Callable, Dict

# Constants
VALID_OPERATIONS = {'+', '-', '*', '/'}


def add(x: float, y: float) -> float:
    """Add two numbers.
    
    Args:
        x: First number
        y: Second number
        
    Returns:
        Sum of x and y
    """
    return x + y


def subtract(x: float, y: float) -> float:
    """Subtract two numbers.
    
    Args:
        x: First number
        y: Second number
        
    Returns:
        Difference of x and y
    """
    return x - y


def multiply(x: float, y: float) -> float:
    """Multiply two numbers.
    
    Args:
        x: First number
        y: Second number
        
    Returns:
        Product of x and y
    """
    return x * y


def divide(x: float, y: float) -> float:
    """Divide two numbers.
    
    Args:
        x: Numerator
        y: Denominator
        
    Returns:
        Quotient of x divided by y
        
    Raises:
        ValueError: If y is zero
    """
    if y == 0:
        raise ValueError("Division by zero is not allowed")
    return x / y


def get_valid_number(prompt: str, input_func: Callable[[str], str] = input) -> float:
    """Get a valid number from user input.
    
    Args:
        prompt: Message to display to user
        input_func: Function to get input (allows for testing)
        
    Returns:
        Valid float number from user
    """
    while True:
        try:
            number = float(input_func(prompt))
            return number
        except ValueError:
            print("Error: Please enter a valid number.")


def get_valid_operation(input_func: Callable[[str], str] = input) -> str:
    """Get a valid operation from user input.
    
    Args:
        input_func: Function to get input (allows for testing)
        
    Returns:
        Valid operation symbol (+, -, *, /)
    """
    while True:
        operation = input_func("Enter operation (+, -, *, /): ").strip()
        if operation in VALID_OPERATIONS:
            return operation
        print("Error: Please enter a valid operation (+, -, *, /).")


def perform_calculation(num1: float, num2: float, operation: str) -> float:
    """Perform calculation based on operation.
    
    Args:
        num1: First number
        num2: Second number
        operation: Operation symbol (+, -, *, /)
        
    Returns:
        Result of the calculation
        
    Raises:
        ValueError: If operation is invalid or division by zero
    """
    operations_map: Dict[str, Callable[[float, float], float]] = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    
    if operation not in operations_map:
        raise ValueError(f"Invalid operation: {operation}")
    
    return operations_map[operation](num1, num2)


def calculate() -> None:
    """Main calculator function."""
    print("Simple Calculator")
    print("-----------------")
    
    # Get inputs
    num1 = get_valid_number("Enter first number: ")
    num2 = get_valid_number("Enter second number: ")
    operation = get_valid_operation()
    
    # Perform calculation
    try:
        result = perform_calculation(num1, num2, operation)
        print(f"\nResult: {num1} {operation} {num2} = {result}")
    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    calculate()