# # Exercise 1
# try:
#     input_1 = float(input("Enter number: "))
#     operator = input("Enter operator (x or /): ")
#     input_2 = float(input("Enter number: "))

#     if operator == "x":
#         print(f"{input_1} x {input_2} = {input_1 * input_2}")
#     elif operator == "/":
#         print(f"{input_1} / {input_2} = {input_1 / input_2}")
#     else:
#         print("Invalid Operation")
# except ValueError:
#     print("Please enter valid numbers.")
# except ZeroDivisionError:
#     print("Cannot divide by 0")

# # exercise 2
# try:
#     number = int("25")
#     print("A")

# except ValueError:
#     print("B")

# else:
#     print("C")

# print("D")

# Exercise 3
try:
    requests_used = 120
    request_limit = 100
    if requests_used >= request_limit:
        raise ValueError("Limit exceeded")
except ValueError as e:
    print(e)
else:
    print("Operation Successful")
finally:
    print("Session finished")