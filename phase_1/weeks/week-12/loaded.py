import json

try: 
    with open("/home/dell/python-learning-journey/phase_1/weeks/week-12/example.json", "r", encoding="utf-8") as file:
        data = json.load(file)
except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("Invalid Json file")
else:
    print(data["assistant"]["name"])
    print(data["assistant"]["settings"]["max_tokens"])
    print(data["tools"][0]["name"])
    print(data["tools"][1]["enabled"])

# exercise 2
# bug detector

user = {
    "name": "Golden",
    "skills": {"Python", "Git", "RAG"}
}
user["skills"] = list(user["skills"])

json_data = json.dumps(user)

print(json_data)
