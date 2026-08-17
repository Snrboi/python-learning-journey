user = {
    "name": "Golden",
    "age": 25
}

print(user["email"]) # this would print a key error and .get() would stop it from crashing and returning either none or a specified error message.

users = [
    {"name": "Golden", "role": "AI Engineer"},
    {"name": "Admin", "role": "Administrator"}
]

for user in users:
    print(user["username"]) # this is an invalid key as it isnt inside users


user = {
    "name": "Golden",
    "profile": {
        "age": 25
    }
}

user["profile"]["country"] = "Nigeria" # this is valid as this creates a country key inside profile and Nigeria as its keyword.

print(user)

scores = {
    "Python": 90,
    "Git": 65,
    "APIs": 80
}

for subject, score in scores: # it doesnt specify .items() so there would be an unpacking error
    print(subject, score)


users = {
    "snrboi": {
        "role": "AI Engineer"
    },
    "admin": {
        "role": "Administrator"
    }
}

for username, profile in users.items():
    print(username)
    print(profile["role"])  # yes it is as .items take key and values and username is the key while profile is the value.