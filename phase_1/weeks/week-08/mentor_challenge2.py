# Goal: double the values of numbers in a list.
# Input: list of numbers
# Output: list of doubled numbers
# Steps: go through the list and double every number inside it
# Python concepts: functions, list(), map, return
def apply_operation(operation, numbers):

    return list(map(operation, numbers))

numbers = [1, 2, 3, 4, 5]

double = lambda x: x * 2

result = apply_operation(double, numbers)

print(result)