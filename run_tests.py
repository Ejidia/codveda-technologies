import unittest
from test_calculator import TestCalculator

def run_all_tests():
    """Run all calculator tests and display results"""
    print("Running Calculator Tests...")
    print("==========================")
    
    # Create a test suite
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    
    # Run tests
    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)
    
    print("\n==========================")
    print(f"Tests Run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success: {result.wasSuccessful()}")
    print("==========================")
    
    if result.wasSuccessful():
        print("\n All tests passed!")
    else:
        print("\n Tests failed!")
    
    return result

if __name__ == "__main__":
    run_all_tests()