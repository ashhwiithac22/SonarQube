# Sample Python code for SonarQube analysis

def add_numbers(a, b):
    result = a + b
    return result


def divide_numbers(a, b):
    if b == 0:
        print("Cannot divide by zero")
        return None
    return a / b


if __name__ == "__main__":
    print("Addition:", add_numbers(10, 5))
    print("Division:", divide_numbers(10, 2))
