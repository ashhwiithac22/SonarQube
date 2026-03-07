# BAD CODE - Contains vulnerabilities and code smells for Exercise 13B

import base64
import os

# VULNERABILITY 1: Hardcoded API Key (Critical)
API_KEY = "sk_live_1234567890abcdefghijklmnopqrstuvwxyz"
SECRET_KEY = "prod_secret_key_78901234567890"

# VULNERABILITY 2: Hardcoded Password
DATABASE_PASSWORD = "admin123"
AWS_SECRET = "AKIAIOSFODNN7EXAMPLE"

def process_payment(credit_card):
    """Process payment with hardcoded credentials"""
    
    # VULNERABILITY 3: Hardcoded Credit Card (PCI violation)
    test_credit_card = "4111-1111-1111-1111"
    
    # CODE SMELL 1: Empty catch block
    try:
        result = 10 / 0  # This will cause an error
    except:
        pass  # Empty except - hides errors!
    
    # CODE SMELL 2: Unused variable
    unused_variable = "This is never used"
    
    # CODE SMELL 3: Function too long/complex
    if True:
        if True:
            if True:
                if True:
                    if True:
                        # Deep nesting is bad!
                        print("Too many nested ifs")
    
    # CODE SMELL 4: Duplicated string literals
    error1 = "Database connection failed"
    error2 = "Database connection failed"  # Duplicate!
    error3 = "Database connection failed"  # Duplicate!
    
    # VULNERABILITY 4: Weak encryption (hardcoded key)
    encoded = base64.b64encode(b"sensitive_data")
    
    # BUG: Potential null pointer/exception
    data = None
    # This will cause AttributeError
    # print(data.length)  # Uncomment to cause runtime error
    
    return "Payment processed"

# CODE SMELL 5: Global variable modification
counter = 0
def increment():
    global counter
    counter += 1
    # Should return something

# CODE SMELL 6: Function without docstring
def bad_function(a,b,c,d,e,f,g):
    return a+b+c+d+e+f+g  # Too many parameters!

# VULNERABILITY 5: Command injection risk
user_input = "test; rm -rf /"
os.system("echo " + user_input)  # DANGEROUS!

# CODE SMELL 7: Magic numbers
def calculate(value):
    return value * 3.14159 * 42 * 7.5  # What do these numbers mean?

# BUG: Off-by-one error
def process_list(items):
    for i in range(len(items) + 1):  # Will cause IndexError
        print(items[i])

if __name__ == "__main__":
    process_payment("test")
    print("Application started with multiple vulnerabilities!")
