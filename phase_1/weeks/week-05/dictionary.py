# Exercise 1
students = {
    "name": "Golden", 
    "age": 25,
    "country": "Nigeria",
    "program": "Python"
}
print(students["name"])
print(students["age"])
print(students["country"])
print(students["program"])

# Exercise 2
user = {
    "username": "snrboi",
    "age": 25
}
user["country"] = "Nigeria"
user["role"] = "Lead AI Engineer"
user["age"] = 26
user["role"] = "AI Engineer"

# Exercise 3
user = {
    "name": "Golden",
    "age": 25
}

user["age"] = 26
user["country"] = "Nigeria"

print(user) # This would print {'name': 'Golden, 'age': '26', 'country': 'Nigeria'}

# Exercise 4
user = {
    "username": "snrboi",
    "age": 25
}
#print(user["email"]) crashes the program with a key error message while print(user.get("email")) would print none or a selected message for handling invalid inputs.

print(user.get("email", "Email not available"))

# Exercise 5
profile = {
    "name": "Golden",
    "age": 25,
    "country": "Nigeria"
}
if "name" in profile:
    print("name exists")

if "email" not in profile:
    print("email doesnt exist")

if "Golden" in profile:
    print("key found")
else:
    print("key not available")

if "age" in profile:
    print("key found")
else:
    print("key not available")

# Exercise 6
settings = {
    "theme": "dark",
    "language": "English",
    "notifications": True
}

settings.pop("language")
print(settings)

del settings["notifications"]
print(settings)

settings.popitem()
print(settings)

# Exercise 7
profile = {
    "name": "Golden",
    "age": 25,
    "role": "AI Engineer"
}

print(profile.keys())
print(profile.values())
print(profile.items())

# Exercise 8
profile = {
    "name": "Golden",
    "age": 25,
    "country": "Nigeria"
}

for key, value in profile.items():
    print(key, value)