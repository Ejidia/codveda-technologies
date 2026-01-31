def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers (handle division by zero)"""
    if y == 0:
        raise ValueError("Error: Division by zero is not allowed")
    return x / y

def get_valid_number(prompt):
    """Get a valid number from user input"""
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Error: Please enter a valid number.")
