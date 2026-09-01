#  Exercise 1
# With greet python takes the function as an object an object that can be assigned or placed in lists or dictionaries with greet() python calls the function and runs it.

# Exercise 2
def greet():
    print("Hello")

action = greet

action() #This prints "hello" as object greet has been assigned to action

# Exercise 3
def greet():
    print("Hello")

def execute(action):
    action()

execute(greet)

# Exercise 4
def add():
    print("Adding...")

def delete():
    print("Deleting...")

new = [add, delete]

for item in new:
    item()

# Exercise 5
def profile():
    print("Loading Profile")

def calculator():
    print("Loading Calculator")

def settings():
    print("Loading Settings")

new_menu = {
    "1": profile,
    "2": calculator,
    "3": settings
}
choice = "3"
new_menu[choice]()