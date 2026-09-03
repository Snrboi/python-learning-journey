# Exercise 1
numbers = [2, 4, 6]

def square(x):
    return x ** 2

result = list(map(square, numbers))

print(result) # Map applies the square function and takes numbers as its arguments to apply the function to.

# Exercise 2
names = ["golden", "snrboi", "admin"]

result = list(map(lambda name: name.upper(), names))

print(result)

# Exercise 3
numbers = [10, 20, 30, 40]

new = list(map(lambda num: str(num), numbers))

print(new)