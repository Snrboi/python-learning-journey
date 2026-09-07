# Goal: return active users
# Input: list of dictionaries
# Output: active users 
# Steps: go through a list and find the active users
# Python concepts: list(), filter() lambda
users = [
    {"username": "snrboi", "role": "AI Engineer", "status": "active"},
    {"username": "admin", "role": "System Administrator", "status": "inactive"},
    {"username": "developer", "role": "Community Developer", "status": "active"}
]

active_users = list(filter(lambda user: user["status"] == "active", users))
print(active_users)