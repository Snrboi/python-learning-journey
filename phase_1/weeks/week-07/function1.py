# Exercise 1
def show_message():
    print("Welcome to AIOS")
show_message()    

# exercise 2
def greet(name):
    print(f"Hello, {name}!")
greet("Golden")    

# exercise 3
def introduce(name, age, role):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Role: {role}")
introduce(age = 30, name= "jeff", role= "ai")    

# exercise 4
def add(a,b):
    return a + b
result = add(10, 20)
print(result)

# exercise 5
def check_age(age):
    if age >= 18:
        return "Adult"
    return "Minor" 
age = check_age(19)
print(age)

# exercise 6
def show_skills(skills):
    for skill in skills:
        print(skill)
skills = ["Python", "Git", "AI"]
    
show_skills(skills) 
    