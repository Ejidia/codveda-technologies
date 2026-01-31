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

def get_valid_operation():
    """Get a valid operation from user input"""
    operations = ['+', '-', '*', '/']
    while True:
        operation = input("Enter operation (+, -, *, /): ").strip()
        if operation in operations:
            return operation
        print("Error: Please enter a valid operation (+, -, *, /).")

def calculate():
    """Main calculator function"""
    print("Simple Calculator")
    print("-----------------")
    
    # Get inputs
    num1 = get_valid_number("Enter first number: ")
    num2 = get_valid_number("Enter second number: ")
    operation = get_valid_operation()
    
    # Perform calculation
    try:
        if operation == '+':
            result = add(num1, num2)
            print(f"\nResult: {num1} + {num2} = {result}")
        elif operation == '-':
            result = subtract(num1, num2)
            print(f"\nResult: {num1} - {num2} = {result}")
        elif operation == '*':
            result = multiply(num1, num2)
            print(f"\nResult: {num1} * {num2} = {result}")
        elif operation == '/':
            result = divide(num1, num2)
            print(f"\nResult: {num1} / {num2} = {result}")
    except ValueError as e:
        print(f"\n{e}")

if __name__ == "__main__":
    calculate()