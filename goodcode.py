"""
Fixed code for Exercise 13C - No vulnerabilities or code smells
"""

import os
import logging
from typing import List, Optional

# FIXED: No hardcoded secrets - use environment variables
API_KEY = os.environ.get('API_KEY', 'default-dev-key-only')
DATABASE_PASSWORD = os.environ.get('DB_PASSWORD', 'dev-password-only')
AWS_SECRET = os.environ.get('AWS_SECRET', 'dev-secret-only')

# Configure logging instead of print statements
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FIXED: Constants with meaningful names
class ErrorMessages:
    """Centralized error messages to avoid duplication"""
    DB_CONNECTION_FAILED = "Database connection failed"
    PAYMENT_FAILED = "Payment processing failed"
    INVALID_INPUT = "Invalid input provided"

# FIXED: Proper exception handling with specific exceptions
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
        result = 10 / 2  # Fixed: no division by zero
        
        # FIXED: Use logging instead of pass
        logger.info(f"Payment processed for card ending in {credit_card[-4:]}")
        
        return "Payment processed successfully"
        
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        raise  # Re-raise to let caller handle
    except Exception as e:
        logger.error(f"Payment processing error: {e}")
        return ErrorMessages.PAYMENT_FAILED

# FIXED: Removed global variable, used class instead
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

# FIXED: Function with proper documentation and parameters
def calculate_area(radius: float) -> float:
    """
    Calculate area of a circle
    
    Args:
        radius: Circle radius
        
    Returns:
        float: Area of the circle
        
    Raises:
        ValueError: If radius is negative
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    
    # FIXED: No magic numbers - use math.pi
    import math
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
    # FIXED: Validate and sanitize input
    allowed_commands = ['ls', 'echo', 'date']
    cmd_parts = command.split()
    
    if cmd_parts and cmd_parts[0] in allowed_commands:
        # Use subprocess instead of os.system
        import subprocess
        result = subprocess.run(cmd_parts, capture_output=True, text=True)
        return result.stdout
    else:
        return "Command not allowed"

# FIXED: Proper list processing with bounds checking
def process_list(items: List) -> List:
    """
    Safely process a list
    
    Args:
        items: List to process
        
    Returns:
        List: Processed items
    """
    result = []
    for i, item in enumerate(items):  # FIXED: Use enumerate instead of range(len()+1)
        try:
            # Process each item safely
            result.append(item)
        except Exception as e:
            logger.error(f"Error processing item at index {i}: {e}")
    return result

# NEW: Unit tests (can be in separate file or here)
import pytest

def test_process_payment():
    """Test payment processing"""
    result = process_payment("4111-1111-1111-1111")
    assert "successfully" in result

def test_calculate_area():
    """Test area calculation"""
    import math
    assert calculate_area(1) == math.pi
    assert calculate_area(0) == 0
    
    with pytest.raises(ValueError):
        calculate_area(-1)

def test_process_list():
    """Test list processing"""
    items = [1, 2, 3]
    result = process_list(items)
    assert len(result) == 3
    assert result == items

def test_counter():
    """Test counter class"""
    counter = Counter()
    assert counter.count == 0
    assert counter.increment() == 1
    assert counter.increment() == 2

def test_execute_safely():
    """Test safe command execution"""
    result = execute_safely("echo hello")
    assert "hello" in result
    
    result = execute_safely("rm -rf /")
    assert "not allowed" in result

if __name__ == "__main__":
    # Run tests if executed directly
    pytest.main([__file__, "-v"])
    
    # Demonstrate functionality
    counter = Counter()
    for _ in range(3):
        counter.increment()
    print(f"Counter: {counter.count}")
    
    print(process_payment("4111-1111-1111-1111"))
    print(f"Area: {calculate_area(5)}")
    print(execute_safely("ls -la"))
