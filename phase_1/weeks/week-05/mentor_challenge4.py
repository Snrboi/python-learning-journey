documents = [
    {
        "title": "Python Basics",
        "status": "ready",
        "tags": ["python", "programming"]
    },
    {
        "title": "AI Agents",
        "status": "processing",
        "tags": ["AI", "agents"]
    },
    {
        "title": "Git Guide",
        "status": "ready",
        "tags": ["git", "github"]
    }
]

for document in documents:
    if document["status"] == "ready":
        print(document["title"])

# Ai engineering thinking
# i would store it as a dictionary because it would be a collection of the same kind of data stored in one variable which is easier to manipulate.


aios = {
    "snrboi": {
        "role": "AI Engineer",
        "skills": ["Python", "Git"]
    },
    "admin": {
        "role": "System Administrator",
        "skills": ["Linux", "Security"]
    }
}

for name, profile in aios.items():
    print(name)
    for skill in profile["skills"]:
        print(skill)