# Objective: Fix Bugs, Code Smells, and improve coverage

import logging

# Configure logging instead of using print statements
logging.basicConfig(level=logging.INFO)

# BAD PRACTICE FIX: API_KEY should ideally come from environment variable
API_KEY = "12345-ABCDE-SECRET"  # Dummy key for demo

# FIX: Handle exceptions specifically
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logging.error("Division by zero attempted")
        return None

# FIX: Removed unused variable
def add_numbers(a, b):
    return a + b

# FIX: Logging instead of print
def divide_numbers(a, b):
    if b == 0:
        logging.warning("Cannot divide by zero")
        return None
    return a / b

if __name__ == "__main__":
    logging.info("Addition: %s", add_numbers(10, 5))
    logging.info("Division: %s", divide_numbers(10, 2))
    logging.info("Safe division: %s", safe_divide(10, 0))
