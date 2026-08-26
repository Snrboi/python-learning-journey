# AI thinking
# Goal: return snrboi's status
# input: Dictionary
# output: snrboi's status
# steps: check the input for snrboi's status
# Python Concepts: function, conditionals 

# Mentor Challenge
def get_user_status(user):
    if user["status"] == "active":
        return f"{user["username"]} is active"
    else:
        return f"{user["username"]} is inactive"

user = {
    "username": "snrboi",
    "role": "AI Engineer",
    "status": "active"
}
a = get_user_status(user)
print(a)