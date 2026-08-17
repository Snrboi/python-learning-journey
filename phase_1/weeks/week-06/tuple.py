# Exercise 1
skills = ("python", "git", "javascript")
print(skills[0])
print(skills[-1])
print(len(skills))

# Exercise 2
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4]) # 20, 30, 40
print(numbers[::-1]) # 50, 40, 30, 20, 10

# Exercise 3
profile = ("Golden", 25, "Nigeria")

name, age, country = profile
print(name)
print(age)
print(country)

# Exercise 4
number = (10) # if this is to be considered a tuple it would have comma after 10

# Exercise 5
coordinates = (6, 10)
# i would use a tuple as tuples are immutable and python wont allow the coordinates to be altered

# Mini project
users = (
    ("snrboi", "AI Engineer"),
    ("admin", "System Administrator"),
    ("developer", "Community Developer")
)

# Goal: Display users (username & role)
# input: Nested Tuples
# output: username and role
# steps: Look through users and display its contents
# python concepts: loops, print()
for name, role in users:
    print(f"Username: {name}")
    print(f"Role: {role}")