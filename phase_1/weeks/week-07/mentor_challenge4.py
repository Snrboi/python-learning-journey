# Goal: Display a users profile
# Input: strings, tuples and dictionary
# Output: full user profile display
# Steps: collect inputs, go through and display them
# Python concepts: functions, for loop, print

def create_profile(username, *skills, **details):
    print(f"Username: {username}")
    print("Skills:")
    for skill in skills:
        print(f"- {skill}")
    print()
    print("Additional Details:")
    for key, detail in details.items():
        print(f"{key}: {detail}")

create_profile(
    "snrboi",
    "Python",
    "Git",
    "AI",
    age=25,
    role="AI Engineer",
    country="Nigeria"
)