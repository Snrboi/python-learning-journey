users = {
    "snrboi": {
        "role": "AI Engineer",
        "status": "active"
    },
    "admin": {
        "role": "System Administrator",
        "status": "active"
    }
}

command = input("Enter Username: ").strip().lower()

if command in users:
    print("User found")
    for username, role in users.items():
        print(f"Username: {username}")
        print(f"Role: {role["role"]}")
        print(f"Status: {role["status"]}")
else: 
    print("User not found")   

users["eben"] = {
    "role": "student",
    "status": "active"
}

print(users) # i would need us to take a step back and i want you to teach me looping through nested dictionaries, how it works, its iteration process and how data inside nested dictinaries can be manipulated. every way it can be manipulated. i just need to learn it so i dont advance to the next topic with half knowledge. 