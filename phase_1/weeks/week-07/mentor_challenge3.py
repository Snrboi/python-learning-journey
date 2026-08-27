# # AI Thinking 
# # Goal: Add a new skill to the users skill list.
# # Input: Dictionary
# # Output: A dicionary with updated skill list.
# # the function mutates the input
# # it doesn't try to assign a new object to the existing global variable it just takes it as an argument and performs a mutation method on it. 

# # Mentor challenge
# user = {
#     "username": "snrboi",
#     "skills": ["Python", "Git"]
# }

# def add_skill(user, skill):
#     user["skills"].append(skill)
#     return user

# a = add_skill(user, "AI")
# print(a)



# prime
def prime(number):
    if number / number == 1:
        if number / 1 == number:
            print("Is Prime")
        else:
            print("Not prime")

prime(4)