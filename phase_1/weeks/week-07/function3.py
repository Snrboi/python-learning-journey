# exercise 1
name = "Golden"

def greet():
    name = "AIOS"
    print(name)

greet() # when this runs using LEGB the inner name AIOS is what prints.
print(name) # Golden prints because strings are immutable and inside the function the variable name references a different object.

# Exercise 2
role = "AI Engineer"

def show_role():
    print(role)

show_role() # When this runs, using LEGB python doesnt see an assigned local or enclosing variable so it checks for a global variable role which is available and uses it.

# exercise 3
age = 25

def change_age(age):
    age = 30

change_age(age)

print(age) # this prints 25 as integers are immutable and age variable inside the function is pointing to a different object and doesnt change the global age variable

# exercise 4
skills = ["Python", "Git"]

def add_skill(skills):
    skills.append("AI")

add_skill(skills)

print(skills) # The outside skills list changes as lists are mutable so once the function is called it mutates the original list.

# exercise 5
skills = ["Python", "Git"]

def change(skills):
    skills = ["AI"]

change(skills)

print(skills) # this prints the original skills list as the functions is trying to completely change it not mutate it.

# Exercise 6
user = {
    "name": "admin",
    "role": "AI Engineering"
}

def promote(user):
    user["role"] = "Senior AI Engineering"
    return user

print(user)
a = promote(user)
print(a)