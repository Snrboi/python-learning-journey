users = [
    {"name": "Golden", "age": 25},
    {"name": "Alex", "age": 30},
    {"name": "John", "age": 22}
]

def get_age(user):
    return user["age"]

result = sorted(users, key=get_age) # The get_age is being alled instead of being passed.

print(result)
