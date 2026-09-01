# Exercise 1
square = lambda x: x ** 2

print(square(5))

#Exercise 2
multiply = lambda a, b: a * b

result = multiply(4, 5)

print(result) #The answer is 20. Lambda takes a and b as its parameters and performs the multiplication when the arguments are passed in.

# Exercise 3
numbers = [1, 2, 3, 4, 5]

new_list = list(map(lambda x: x * 2, numbers))

print(new_list)