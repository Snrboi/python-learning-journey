available_tokens = 5000
try:
    requested_token = int(input("How many tokens does your document require? "))
except ValueError:
    print("Token count must be a number.")
else:
    try:
        if requested_token <= 0:
            raise ValueError("Token count must be greater than zero.")
        elif requested_token > available_tokens:
            raise ValueError("Insufficient tokens.")

        available_tokens -= requested_token
        processing_time = 1000 / requested_token
        print("Document processed successfully.")
        print(f"Remaining tokens: {available_tokens}")
        print(f"Processing time: {processing_time}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Unexpected error: {e}")
finally:
    print("Processing session ended.")