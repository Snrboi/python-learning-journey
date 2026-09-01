def greet():
    print("Hello")

def execute(action):
    action()

execute(greet) # execute is supposed to recieve an object not a called function
