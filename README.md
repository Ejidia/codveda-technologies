# Simple Calculator

A command-line calculator application with comprehensive error handling and test coverage.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, division
- Input validation for numbers and operations
- Division by zero protection
- Type-safe implementation with type hints
- Comprehensive unit test coverage

## Installation

No external dependencies required. Uses Python standard library only.

## Usage

Run the calculator:
```bash
python calculator.py
```

The calculator will prompt you for:
1. First number
2. Second number
3. Operation (+, -, *, /)

Example:
```
Simple Calculator
-----------------
Enter first number: 10
Enter second number: 5
Enter operation (+, -, *, /): +

Result: 10.0 + 5.0 = 15.0
```

## Running Tests

Run all tests:
```bash
python -m pytest test_calculator.py -v
```

Or using unittest:
```bash
python -m unittest test_calculator.py
```

## Code Quality

- ✅ Type hints for all functions
- ✅ Comprehensive docstrings
- ✅ Error handling with descriptive messages
- ✅ 11 unit tests with 100% coverage
- ✅ Clean, maintainable code structure
- ✅ Follows PEP 8 style guidelines

## Project Structure

```
task_1/
├── calculator.py          # Main calculator implementation
├── test_calculator.py     # Unit tests
└── README.md             # This file
```
