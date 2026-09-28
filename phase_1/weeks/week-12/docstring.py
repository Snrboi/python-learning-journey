def clean_prompt(prompt):
    '''Remove trailing spaces and reduce the string to lowercase'''
    return prompt.strip().lower()

def calculate_token_cost(tokens, price)-> float:
    return tokens * price

def multiply(value: int, amount: int) -> int:
    """Multiply value by amount."""
    return value * amount


result = multiply("AI", 3) # 1. it does not reject ai it only specify that the it is expecting an int but it wont reject string
# 2. the result is AIAIAI