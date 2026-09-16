available_credit = 100

try:
    credits_request = int(input("How many credits do you want to use? "))

except ValueError:
    print("Credits must be a number.")

else:
    try:
        if credits_request <= 0:
            raise ValueError("Credits must be greater than zero")

        elif credits_request > available_credit:
            raise ValueError("Insufficient AI Credits")

        print(f"Remaining credits: {available_credit - credits_request}")

    except ValueError as e:
        print(e)