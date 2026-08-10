# Exercise 1
players = ["palmer", "jackson", "caicedo", "neto", "gittens"]

print(players[-1:-3:-1])
# A. palmer
# B. gittens
# c. jackson, caicedo, neto
# d. palmer, jackson, caicedo
# e. caicedo, neto, gittens
# f. palmer, caicedo, gittens
# g. gittens, neto, caicedo, jackson, palmer

# Exercise 2
modules = ["profile", "calculator", "settings"]
modules.append("github")
modules.insert(1, "Ai Assistant")
modules[2] = "developer tools"
modules.remove("settings")
removed_module = modules.pop()
print(modules)
print(removed_module)

# Exercise 3
teams = ["Chelsea"]

teams.append(["Arsenal", "Liverpool"])

print(teams)

teams = ["Chelsea"]

teams.extend(["Arsenal", "Liverpool"])

print(teams)

# append adds a new object to the list  while extend to my understanding concatenates the new list with the old


# Exercise 4
users = ["snrboi", "admin", "developer", "guest"]

print("admin" in users)
print("hacker" not in users)
print(users.index("developer"))
print(users.count("admin"))

# exercise 5
players = ["Palmer", "Jackson"]

backup = players

backup.append("Caicedo")

print(players)
print(backup)

# the both print the same because they both carry the same object and any change made to one is the same as making to the other.

# Exercise 6
players = ["Palmer", "Jackson"]

backup = players.copy()

backup.append("Caicedo")

print(players) # this prints ['Palmer', 'Jackson']
print(backup) # this prints ['Palmer', 'Jackson', 'Caicedo']
# the difference is copy made a duplicate copy sort of a clone of players in the variable backup and  it can be manipulated as its own object

# Exercise 7
teams = [
    ["Palmer", "Jackson"],
    ["Caicedo", "Neto"],
    ["Gittens", "James"]
]
# A. ['Palmer', 'Jackson']
# B. Caicedo
# C. James
# D.
for team in teams:
    for players in team:
        print(players)

# Exercise 8
profile = ["Golden", 25, "Nigeria"]
name, age, country = profile
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Country: {country}")

# exercise 9
numbers = [10, 20, 30, 40, 50]
first, *middle, last = numbers
print(middle)

# exercise 10
modules = ["Python", "Git", "APIs", "Databases"]
for item in modules:
    print(f"Loading {item}...")

# exercise 11
modules = ["Python", "Git", "APIs", "Databases"]
for index, item in enumerate(modules, start=1):
    print(f"{index}. {item}")

# exercise 12
numbers = [1, 2, 3, 4, 5]
squared = [number ** 2 for number in numbers]

print(squared)

# exercise 13
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even = [number for number in numbers if number % 2 == 0]

print(even)

# exercise 14
scores = [75, 40, 90, 60, 85]
scores.sort()
print(scores)
descending = sorted(scores, reverse= True)
print(descending)

# exercise 15
scores = [80, 90, 75, 60, 85]
highest = any(score >= 90 for score in scores)
general = all(score >= 50 for score in scores)

print(highest)
print(general)