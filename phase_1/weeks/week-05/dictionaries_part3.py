# Exercise 1
user = {
    "username": "snrboi",
    "age": 25
}
user.update({
    "age": 26,
    "country": "Nigeria",
    "role": "AI Engineer"
})
print(user)

# Exercise 2
settings = {
    "theme": "dark",
    "language": "English",
    "notifications": True
}
settings.clear()
print(settings)

# Exercise 3
user = {
    "name": "Golden",
    "age": 25
}

backup = user


backup["age"] = 30

print(user)
print(backup) # They produce the same result as both user and backup point to the same object.

# exercise 4
user = {
    "name": "Golden",
    "age": 25
}

backup = user.copy()

backup["age"] = 30

print(user)
print(backup) # here the backup up has cloned user and has its own version so user would print "age" as 25 while backup would print "age" as 30

# Exercise 5
user = {
    "name": "Golden",
    "profile": {
        "age": 25
    }
}

backup = user.copy()

backup["profile"]["age"] = 30

print(user)
print(backup) # Here age prints 30 for both because copy() only affects the outer dictionary while backup and user still points to the inner dictionary

# Exercise 6
user = {
    "username": "snrboi"
}
user.setdefault("country", "Nigeria")
user.setdefault("role", "AI Engineer")

print(user)

# Exercise 7
user = {
    "username": "snrboi",
    "age": 25,
    "role": "AI Engineer"
}
removed_age = user.pop("age")
print(removed_age)
print(user)

# Exercise 8
user = {
    "name": "Golden",
    "age": 25,
    "country": "Nigeria"
}
removed = user.popitem()
print(removed)
print(user)
key, value = removed

# Exercise 9
numbers = range(1,11)

squared = {
    number: number ** 2
    for number in numbers
}

print(squared)

# Exercise 10
scores = {
    "Python": 90,
    "Git": 75,
    "JavaScript": 45,
    "APIs": 85
}

new_scores = {
    item: score
    for item, score in scores.items()
    if score >= 70
}
print(new_scores)

# Exercise 11
user = {
    "name": "Golden",
    "age": 25
}

keys = user.keys()
values = user.values()
items = user.items()

user["country"] = "Nigeria"
print(keys)
print(values)
print(items) # they print out like they are in an inbuilt method e.g dict_keys()seems like a method for terminal 
# Exercise 12
#  All except C are valid as lists are mutable and dictionary keys should be immutable.
