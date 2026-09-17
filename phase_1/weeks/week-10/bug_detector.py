# bug 1
try:
    age = int(input("Enter your age: "))

except ValueError: # This should be ValueError instead
    print("Age must be a number.")

# bug 2
try:
    number = int(input("Enter number: "))
    result = 100 / number

except ValueError: # this handles the hello error
    print("Please enter a valid number.") # this should come first as it immediately catches wrong input

except ZeroDivisionError: # this handles the 0 error
    print("You cannot divide by zero.")# this should come next as it catches and reveals a specific problem in the code

except Exception as e: # this is better here because it catches every other potential errors and logs it as e now if its at the top value and zerodivison error becomes needless as python reads from top to bottom.
    print(f"Something went wrong: {e}")

# bug 3
try:
    credits = int(input("Credits: "))
    remaining = 100 / credits

except:
    pass # while the code works if there is an eventual error there is no way to catch it which is a bad enginnering design

print("Program completed successfully.") # this line is even worse as the operation could fail and the program would print a success message making it harder to trace where the problem is coming from

# bug 4
try:
    requests_used = 150
    request_limit = 100

    if requests_used >= request_limit:
        raise ValueError("Request limit exceeded") # this needs raise so this conditon can be sent to the except block for it to belogged as an error as this error is not a natural python error 

    print("AI request accepted.")

except ValueError as e:
    print(e)

# bug 5
try:
    print("A")

    number = int("20")

    if number > 10:
        raise ValueError("B")

    print("C")

except ValueError as e:
    print(e)

else:
    print("D")

finally:
    print("E")

print("F")
# when this runs its prints A,B,E,F. C is is not printed as there is an error above it in the try block and D is not printed either as the try block didnt end naturally.