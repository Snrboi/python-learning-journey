def create_greeting(name):

    def greet():
        return f"Hello {name}"

    return greet


golden_greeting = create_greeting("Golden")

print(golden_greeting()) # this prints Hello Golden and the closure remembers the inner function variable return {name}

# exercise 2
def create_multiplier(number):

    def multiply(value):
        return value * number

    return multiply


double = create_multiplier(2)
five_times = create_multiplier(5)

print(double(6)) 
print(five_times(6)) # it doesnt start using five automatically because create multiplier was called and assigned inside double also seperately from five times


# exercise 3
def create_prefix(prefix):

    def prefix_message(message):
        return f"{prefix}: {message}"
    return prefix_message

error = create_prefix("ERROR")
warning = create_prefix("WARNING")

print(error("File missing"))
print(warning("Token limit approaching"))