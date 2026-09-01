def run_operation(operation, a, b):
    return operation(a, b)

result = run_operation(lambda: 10 + 5, 10, 5)

print(result)