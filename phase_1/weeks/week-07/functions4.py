# Exercise 1
def show_items(*items):
    print(items)

show_items("Python", "Git", "AI") # tuple

# Exercise 2
def add_numbers(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

# Exercise 3
def create_user(**details):
    print(details) # This prints a dictionary

create_user(
    name="Golden",
    age=25,
    role="AI Engineer"
)

# Exercise 4
def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

show_profile(
    name="Golden",
    age=25,
    country="Nigeria",
    role="AI Engineer"
)

# Exercise 5
numbers = [10, 20, 30]

def add(a, b, c):
    return a + b + c

add(*numbers)

# Exercise 6
user = {
    "name": "Golden",
    "age": 25,
    "role": "AI Engineer"
}

def display_user(name, age, role):
    print(name)
    print(age)
    print(role)

display_user(**user)