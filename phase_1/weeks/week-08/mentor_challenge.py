# Goal: Perform Calculations
# Input: intergers
# Output:calculated value
# Steps: take the inputed integers and calculate them
# Python concepts: functions, higher order functions


def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def run_operation(operation, a, b):
    return operation(a, b) 

result1 = run_operation(add, 10, 5)
result2 = run_operation(multiply, 10, 5)

print(result1)
print(result2)