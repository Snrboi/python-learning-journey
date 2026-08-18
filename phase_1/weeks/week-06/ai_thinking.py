# Goal: find the required skills the user already has
# input: 2 lists of skills
# output: skills user has that is required
# steps: compare the two list and return what they have in common.
# Python concepts: sets, print

user_skills = ["Python", "Git", "Python", "APIs"]
required_skills = ["Python", "APIs", "Machine Learning"]

user = set(user_skills)
required = set(required_skills)

required_skill = user & required

print(required_skill)

