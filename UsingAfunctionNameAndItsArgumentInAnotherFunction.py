def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1 / num2

def multiply(num1, num2):
    return num1 * num2

def do_operation(operation, num1, num2):
    return operation(num1, num2)

print(do_operation(add, 1, 2))