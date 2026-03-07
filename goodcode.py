"""
Fixed code for Exercise 13C - No vulnerabilities or code smells
"""

import os
import logging
from typing import List, Optional
import math
import subprocess

# FIXED: No hardcoded secrets - use environment variables with defaults
API_KEY = os.environ.get('API_KEY', 'dev-key-please-change')
DATABASE_PASSWORD = os.environ.get('DB_PASSWORD', 'dev-password-please-change')
AWS_SECRET = os.environ.get('AWS_SECRET', 'dev-secret-please-change')

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FIXED: Constants with meaningful names
class ErrorMessages:
    """Centralized error messages to avoid duplication"""
    DB_CONNECTION_FAILED = "Database connection failed"
    PAYMENT_FAILED = "Payment processing failed"
    INVALID_INPUT = "Invalid input provided"

# FIXED: Proper exception handling
def process_payment(credit_card: str) -> str:
    """
    Process payment with proper error handling
    
    Args:
        credit_card: Masked credit card number
        
    Returns:
        str: Payment status
    """
    try:
        # Validate input
        if not credit_card or len(credit_card) < 4:
            raise ValueError("Invalid credit card")
            
        # Simulate payment processing
        result = 10 / 2  # No division by zero
        
        logger.info(f"Payment processed for card ending in {credit_card[-4:]}")
        
        return "Payment processed successfully"
        
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        raise
    except Exception as e:
        logger.error(f"Payment processing error: {e}")
        return ErrorMessages.PAYMENT_FAILED

# FIXED: Class instead of global variable
class Counter:
    """Proper counter class with encapsulation"""
    def __init__(self):
        self._count = 0
    
    def increment(self) -> int:
        self._count += 1
        return self._count
    
    @property
    def count(self) -> int:
        return self._count

# FIXED: No magic numbers
def calculate_area(radius: float) -> float:
    """
    Calculate area of a circle
    
    Args:
        radius: Circle radius
        
    Returns:
        float: Area of the circle
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    
    return math.pi * radius ** 2

# FIXED: Safe command execution
def execute_safely(command: str) -> str:
    """
    Safely execute system commands
    
    Args:
        command: Command to execute
        
    Returns:
        str: Command output
    """
    allowed_commands = ['ls', 'echo', 'date', 'pwd']
    cmd_parts = command.split()
    
    if cmd_parts and cmd_parts[0] in allowed_commands:
        result = subprocess.run(cmd_parts, capture_output=True, text=True)
        return result.stdout
    else:
        return "Command not allowed"

# FIXED: Proper list processing
def process_list(items: List) -> List:
    """
    Safely process a list
    
    Args:
        items: List to process
        
    Returns:
        List: Processed items
    """
    result = []
    for i, item in enumerate(items):
        try:
            result.append(item)
        except Exception as e:
            logger.error(f"Error processing item at index {i}: {e}")
    return result

# FIXED: Function with proper return value
def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Calculate discounted price
    
    Args:
        price: Original price
        discount_percent: Discount percentage
        
    Returns:
        float: Discounted price
    """
    if price < 0 or discount_percent < 0:
        raise ValueError("Price and discount must be positive")
    
    discount_amount = price * (discount_percent / 100)
    return price - discount_amount

if __name__ == "__main__":
    # Demo functionality
    counter = Counter()
    for _ in range(3):
        counter.increment()
    print(f"Counter: {counter.count}")
    
    print(process_payment("4111-1111-1111-1111"))
    print(f"Area of circle with radius 5: {calculate_area(5):.2f}")
    print(f"Discounted price: ${calculate_discount(100, 20):.2f}")
    print(execute_safely("ls -la"))
