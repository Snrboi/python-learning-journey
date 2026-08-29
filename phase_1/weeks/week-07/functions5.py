# Exercise 1
def get_data():
    return "Golden", 25, "Nigeria" # Tuple

# Exercise 2
def get_data():
    return "Golden", 25, "Nigeria"

name, age, country = get_data()
print(name)
print(age)
print(country)

# exercise 3
def add(a, b):
    print(a + b)

result = add(10, 20)

print(result) # it prints none

# exercise 4
def add(a, b):
    return a + b

result = add(10, 20)

print(result)

# exercise 5
def test():
    print("Start")
    return "Finished"
    print("End")

result = test()
print(result) # only finished gets printed as only finished was returned and the function ended before the print("End")

# exercise 6
def get_user():
    return {
    "username": "snrboi",
    "age": 25,
    "role": "AI Engineer",
    "skills": ["Python", "Git", "AI"]
}

a = get_user()["username"]
b = get_user()["role"]
print(a, b)