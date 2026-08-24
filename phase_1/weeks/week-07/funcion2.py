# Exercise 1
def display_user(name, age, role):
    return name, age, role

a = display_user("Golden", 25, "Ai")
print(a)

# Exercise 2
b = display_user(role= "Ai", name= "Emeto", age= 25)
print(b)

# Exercise 3
def create_user(name, role= "User"):
    return name, role

a = create_user("Golden")
print(a) # this prints Golden and the default argument of user
b = create_user("Golden", "AI Engineer")
print(b) #this prints Golden and overrides the default argument of user with AI Engineer

#exercise 4
def multiply(a, b):
    return a * b

a = multiply(2, 2)
print(a)

# Exercise 5
def check_number(number):
    if number > 0:
        return "Positive"
    elif number == 0:
        return "Zero"
    else:
        return "Negative"

q = check_number(0)
print(q)

# Exercise 6
users = ["admin", "developer", "snrboi", "guest"]

def find_user(users, username):
    for user in users:
        if user == username:
            return "User found"
        else:
            return "User not found"

a = find_user(users, "admin")
print(a)

def find_user(users, username):
    if username in users:
        return "User found"
    else:
        return "User not found"

b = find_user(users, "admin")
print(b)
# tought of the first one when i initially saw the question after i was done i realized it could be shorter so i did the second.