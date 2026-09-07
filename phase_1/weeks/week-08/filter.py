# Exercise 1
numbers = [10, 15, 20, 25, 30, 35]
filtered =list(filter(lambda even: even % 2 == 0, numbers))
print(filtered)

# Exercise 2
def is_active(user):
    if user["status"] == "active":
        return user

users = [
    {"username": "snrboi", "status": "active"},
    {"username": "admin", "status": "inactive"},
    {"username": "developer", "status": "active"},
    {"username": "guest", "status": "inactive"}
]

active_users = list(filter(is_active, users))
print(active_users)

# Exercise 3
scores = [45, 80, 65, 90, 55, 75]

new_scores = list(filter(lambda new: new > 70, scores))