# Exercises 1
numbers = [40, 10, 30, 20]

result = sorted(numbers) # [10, 20, 30, 40] Numbers doesnt mutate the original object

print(result)

# Exercise 2 
names = ["Golden", "AI", "Python", "Git"]

sorted_names = sorted(names, key=len)

print(sorted_names)

# Exercise 3
users = [
    {"name": "Golden", "age": 25},
    {"name": "Alex", "age": 30},
    {"name": "John", "age": 22}
]

sorted_users = sorted(users, key= lambda user: user["age"])
print(sorted_users)