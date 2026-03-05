# This file is only for Exercise 15: simulating bad code practices

# BAD PRACTICE 1: Hardcoded API Key (Security Hotspot)
API_KEY = "12345-ABCDE-SECRET"  # Dummy key for SonarQube scan

# BAD PRACTICE 2: Empty except block (Code Smell)
def unsafe_divide(a, b):
    try:
        return a / b
    except:
        pass  # Empty except block triggers SonarQube code smell

# BAD PRACTICE 3: Unused variable (Code Smell)
def add_numbers_with_issue(a, b):
    unused_variable = a + b  # SonarQube will flag this
    result = a + b
    return result

# BAD PRACTICE 4: Print statements instead of logging
def divide_numbers_with_issue(a, b):
    if b == 0:
        print("Cannot divide by zero")  # Minor code smell
        return None
    return a / b

if __name__ == "__main__":
    print("Addition:", add_numbers_with_issue(10, 5))
    print("Division:", divide_numbers_with_issue(10, 2))
    print("Unsafe division (triggers code smell):", unsafe_divide(10, 0))
