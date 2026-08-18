# Exercise 1
skills = {"Python", "Git", "Python", "AI", "Git"}
print(skills) # set only accepts unique values and removes duplicates

# Exercise 2
skills = {"Python", "Git"}
skills.add("Ai")
skills.update([
    "API",
    "SQL",
    "JavaScript"
])
print(skills)

# Exercise 3
python = {"Golden", "Alex", "John"}
ai = {"Golden", "Alex", "Mary"}

everyone = python | ai
both = python & ai
only_py = python - ai
only_ai = ai - python

# exercise 4
# .remove()raises an error if the value passed into it to be removed isnt in the set while .discard() doesnt

# Exercise 5
skills = {"Python", "Git", "AI"}

print(skills[0]) # it raises an error as sets are unordered and there is no index
