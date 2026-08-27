def show_user(**details):
    for key, value in details.items(): # .items() is needed to unpack key and value
        print(key, value)

show_user(
    name="Golden",
    role="AI Engineer"
)
