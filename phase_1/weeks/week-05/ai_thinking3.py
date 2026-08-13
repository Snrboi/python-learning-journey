documents = {
    "doc1": {
        "title": "Python Basics",
        "tags": ["python", "programming"],
        "metadata": {
            "author": "Golden",
            "year": 2026
        }
    },
    "doc2": {
        "title": "AI Agents",
        "tags": ["AI", "agents"],
        "metadata": {
            "author": "Golden",
            "year": 2026
        }
    }
}

# 1. This structure is better because it holds a collection of a type of data in one place and having dozens of seperate variables would make it harder to manipulateand keep track of. 
print(documents["doc2"]["title"])
print(documents["doc2"]["metadata"]["author"])
documents["doc2"]["tags"].append("automation")
documents["doc1"]["metadata"]["year"] = 2027
print(documents)