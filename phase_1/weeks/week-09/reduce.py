from functools import reduce

numbers = [5, 10, 15]

result = reduce(lambda a, b: a + b, numbers)

print(result) # 30 lambda has two parameters a and b and the action is a + b so while reduce runs it keeps adding values in a list till only one value is left.

# Exercise 2
numbers = [2, 3, 4]

multiplied = reduce(lambda a, b: a * b, numbers)

print(multiplied)