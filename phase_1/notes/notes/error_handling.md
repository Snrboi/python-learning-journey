# Error Handling in Python

## 1. Bugs vs Exceptions

A bug is a problem in the program's logic or implementation.

Example:

price = 100
discount = 20
final_price = price + discount

The program runs, but the result is logically wrong.

An exception occurs when Python cannot successfully complete an operation.

Example:

age = int("Golden")

Python raises:

ValueError

---

## 2. Common Exceptions

### ValueError
The type of operation is valid, but the supplied value is inappropriate.

Example:

int("hello")

### TypeError
An operation is performed using incompatible types.

Example:

"Age: " + 25

### ZeroDivisionError

10 / 0

### IndexError

numbers = [10, 20]
print(numbers[5])

### KeyError

user = {"name": "Golden"}
print(user["age"])

### FileNotFoundError

Occurs when attempting to access a file that cannot be found.

---

# 3. try / except

`try` contains an operation that may raise an exception.

`except` handles a matching exception.

Example:

try:
    age = int(input("Enter age: "))

except ValueError:
    print("Age must be a number.")

If an exception occurs inside `try`, the remaining statements in that
try block are skipped and Python searches for a matching exception
handler.

---

# 4. Multiple Exception Handlers

try:
    number = float(input("Enter number: "))
    result = 100 / number

except ValueError:
    print("Enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

Different failures can therefore receive different responses.

---

# 5. if/else vs try/except

Use `if/else` for normal program decisions.

Example:

if age >= 18:
    print("Adult")
else:
    print("Minor")

Use `try/except` when an operation may fail by raising an exception.

Example:

try:
    age = int(input("Age: "))
except ValueError:
    print("Invalid age.")

Mental model:

if/else
→ What situation am I in?

try/except
→ Can this operation successfully complete?

---

# 6. try / except / else

`else` executes when the `try` block completes successfully.

try:
    number = int(input("Number: "))

except ValueError:
    print("Invalid number.")

else:
    print(f"Number: {number}")

Mental model:

try succeeds → else
try raises matching exception → except

---

# 7. finally

`finally` executes regardless of whether the operation succeeds or fails.

try:
    number = int(input("Number: "))

except ValueError:
    print("Invalid number.")

finally:
    print("Operation finished.")

`finally` is particularly useful for cleanup operations and resources.

---

# 8. raise

Python can raise exceptions automatically:

10 / 0

But an application can also deliberately raise an exception.

Example:

age = -10

if age < 0:
    raise ValueError("Age cannot be negative.")

This is useful when something is valid Python but violates an
application rule.

Mental model:

if
→ detect the invalid condition

raise
→ declare the condition a failure

except
→ handle that failure

---

# 9. Exception Objects

Exceptions are objects.

Example:

try:
    raise ValueError("Invalid request.")

except ValueError as e:
    print(e)

`e` references the exception object.

Output:

Invalid request.

This allows the program to preserve and inspect information about
the failure.

---

# 10. Exception vs Specific Exceptions

Specific handlers should normally be used when the expected failure
is known.

Example:

except ValueError:
    ...

A broader fallback can be:

except Exception as e:
    print(f"Unexpected error: {e}")

When combining them, specific exceptions should appear before a
broader handler.

Example:

except ValueError:
    ...

except ZeroDivisionError:
    ...

except Exception as e:
    ...

---

# 11. Avoid Silently Swallowing Exceptions

Dangerous pattern:

try:
    run_operation()
except:
    pass

This can hide failures and make debugging difficult.

The application may continue running even though an important
operation failed.

Good error handling is not simply preventing crashes.

Good error handling means:
- understanding what can fail;
- handling expected failures appropriately;
- preserving useful information;
- not hiding unexpected failures.

---

# 12. Application Validation

Python may accept a value even though the application does not.

Example:

requests_used = 120
request_limit = 100

if requests_used >= request_limit:
    raise ValueError("Request limit reached.")

This is an application/business rule rather than a Python language error.

---

# 13. Failure Boundaries

Avoid automatically wrapping an entire large application in one
giant try/except.

Instead, think about where failures can originate.

Example AI pipeline:

User Input
    ↓
Input Validation
    ↓
Document Processing
    ↓
Embedding API
    ↓
Vector Database
    ↓
LLM API
    ↓
Response

Each part can have different failures and may require different
handling.

---

# 14. State Changes and Failure

Be careful about changing application state before an operation that
can still fail.

Example:

available_tokens -= requested_tokens
process_document()

If `process_document()` fails, the tokens may already have been
deducted.

Sometimes the safer sequence is:

validate
→ perform operation
→ confirm success
→ update state

This idea becomes especially important with databases and
transactions.

---

# AI Engineering Thinking

Error handling in AI engineering is not just:

"How do I stop my program from crashing?"

A better question is:

"Where can this system fail, what does each failure mean, and which
part of the system should handle it?"

Examples include:

- invalid user input
- corrupted documents
- failed API requests
- network timeouts
- unavailable AI models
- invalid API keys
- malformed responses
- database failures
- vector database failures
- failed embedding generation

Good AI systems should make failures observable and understandable
rather than silently hiding them.

---

# Core Mental Model

if / elif / else
→ normal program decisions

try
→ attempt an operation that may fail

except
→ handle a matching failure

raise
→ deliberately declare a failure

else
→ run when try succeeds

finally
→ run regardless of success or failure

Exception as e
→ access information about the exception

Specific exceptions
→ handle known failures

Exception
→ broader fallback for ordinary unexpected failures