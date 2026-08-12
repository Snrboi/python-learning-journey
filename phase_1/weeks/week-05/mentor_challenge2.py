company = {
    "name": "AIOS Labs",
    "departments": [
        {
            "name": "Engineering",
            "employees": ["Alice", "Bob"]
        },
        {
            "name": "Research",
            "employees": ["John", "Mary"]
        }
    ]
}

print(company["departments"][1]["employees"][0]) #John
# python goes through dictionary company,checks for the key departments which is a list, checks the index 1, which is a dictionary and bring out the key employees which is a list and prints out index 0  