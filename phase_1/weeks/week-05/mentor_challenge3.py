aios = {
    "user": {
        "name": "Golden",
        "skills": ["Python", "Git"],
        "settings": {
            "theme": "dark",
            "notifications": True
        }
    }
}
# 1. Git
# 2. Dark
aios["user"]["skills"].append("Javascript")
aios["user"]["settings"]["theme"] = "light"
aios["user"]["country"] = "Nigeria"
print(aios)

