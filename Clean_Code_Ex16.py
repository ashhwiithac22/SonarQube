# Clean_Code_Ex16.py
# Exercise 16 - Fixed Code

import logging

# Setup proper logging
logging.basicConfig(level=logging.INFO)

# BAD PRACTICE FIXED: Removed hardcoded API key
API_KEY = None  # Keep keys secret or use environment variables

# Fix Empty except block
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logging.warning("Division by zero attempted!")
        return None

# Fix unused variable
def add_numbers(a, b):
    result = a + b
    return result

# Replace print statements with logging
def divide_numbers(a, b):
    if b == 0:
        logging.warning("Cannot divide by zero")
        return None
    return a / b

if __name__ == "__main__":
    logging.info("Addition: %s", add_numbers(10, 5))
    logging.info("Division: %s", divide_numbers(10, 2))
    logging.info("Safe division: %s", safe_divide(10, 0))
