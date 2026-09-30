import json

details = '''
{
"name": "Golden",
"career": "AI Engineer",
"active": true,
"skills": ["Python", "Git", "RAG"],
"experience": null
}
'''

developer = json.loads(details)

print(developer["career"])

new_json = json.dumps(developer, indent=2)

print(new_json)

# exercise 2
ai_model = {
    "name": "MyModel",
    "active": True,
    "max_tokens": 5000,
    "tools": ["search", "calculator"],
    "error": None
}

models = json.dumps(ai_model, indent=4)

print(type(models))
print(models)

# exercise 3

developer = {
    "name": "Golden",
    "active": True
}

with open("developer.json", "w", encoding="utf-8") as file:
    json.dump(developer, file, indent=4)


# exercise 4
try:
    with open("/home/dell/python-learning-journey/phase_1/weeks/week-12/settings.json", "r", encoding="utf-8") as file:
        det = json.load(file)
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("Invalid JSON Format")
else:
    print(det[0]["model"])
    print(det[0]["stream"])

# exercise 5
try:
    with open("users.json", "r", encoding="utf-8") as file:
        users = json.load(file)
except FileNotFoundError:
    print("FIle Not Found")
except json.JSONDecodeError:
    print("Invalid JSON Format")
else:
    new_user = {"name": "Grace", "active": True}
    users.append(new_user)
    with open("users.json", "w", encoding="utf-8") as file:
        json.dump(users, file)