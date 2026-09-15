from functools import reduce

numbers = [5, 10, 15, 20]

added = reduce(lambda a, b: a + b, numbers)

print(added)

# exercise 2

numbers = [2, 3, 4, 5]

multiplied = reduce(lambda a, b: a * b, numbers)

print(multiplied)

# exercise 3

scores = [72, 91, 68, 88, 95, 79]

highest = reduce(lambda a, b:a if a > b else b, scores)

print(highest)
