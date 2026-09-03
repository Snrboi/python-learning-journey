def run_operation(operation, a, b):
    return operation(a, b)

result = run_operation(lambda a, b: a + b, 10, 5) # it produces an error as lambda didnt have parameters to work with and 10 + 5 was hardcoded instead of adding the parameters. 

print(result)