# Exercise 1
user = {
    "username": "snrboi",
    "skills": ["Python", "Git", "JavaScript"]
}
print(user["skills"])
print(user["skills"][0])
print(user["skills"][-1])
user["skills"][1] = "Github"
print(user["skills"])

# Exercise 2
users = [
    {
        "username": "snrboi",
        "role": "AI Engineer"
    },
    {
        "username": "admin",
        "role": "System Administrator"
    },
    {
        "username": "developer",
        "role": "Community Developer"
    }
]
print(users[0]["username"])
print(users[1]["role"])
print(users[2]["role"])

# Exercise 3
for user in users:
    for key, value in user.items():
        print(f"{key}: {value}")

# Exercise 4
user = {
    "username": "snrboi",
    "profile": {
        "age": 25,
        "country": "Nigeria",
        "role": "AI Engineer"
    }
}
for key, value in user["profile"].items():
    print(f"{key}: {value}")

# Exercise 5
user["profile"]["age"] = 26
user["profile"]["role"] = "AI Software Engineer"
user["profile"]["state"] = "Rivers"
print(user)

# Exercise 6
teams = [
    ["Palmer", "Jackson"],
    ["Caicedo", "Neto"],
    ["Gittens", "James"]
]

for index, team in enumerate(teams, start= 1):
    print(f"Team {index}")
    for player in team:
        print(player)

# Exercise 7
users = [
    {
        "username": "snrboi",
        "skills": ["Python", "Git"]
    },
    {
        "username": "admin",
        "skills": ["Linux", "Security"]
    }
]
for user in users:
    print (user["username"])
    for skill in user["skills"]:
        print(skill)

# exercise 8
for user in users:
    print (user["username"])
    for skill in user["skills"]:
        print(skill)

