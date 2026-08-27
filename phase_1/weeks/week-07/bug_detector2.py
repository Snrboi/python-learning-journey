count = 0

def increase():
    global count # This is needed so that the global variable can be manipulated inside the function.
    count += 1

increase()

print(count)