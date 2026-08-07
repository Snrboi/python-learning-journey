## Weekly summary
- Below is all i did for the week as i couldnt do a daily logs because i had to take my time with loops.

 # Python Learning Journey — Loops

## Sprint 6 — Loop Mastery

Loops are programming structures that allow a program to repeatedly execute a block of code. The repetition can continue for a specific number of iterations, through a collection of data, or while a condition remains true.

---

## 1. `while` Loops

A `while` loop repeatedly executes code as long as its condition evaluates to `True`.

### Basic structure

```python
initialization

while condition:
    work
    update
```

### Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```text
1
2
3
4
5
```

### Four important components

1. **Initialization** — establishes the starting value.
2. **Condition** — determines whether the loop should continue.
3. **Work** — the task performed during each iteration.
4. **Update** — changes the state so the loop can eventually terminate.

### Important distinction

A `while` loop is **not automatically an infinite loop**.

It becomes infinite when its condition never becomes `False` and there is no `break`.

---

# 2. `for` Loops

A `for` loop is commonly used to iterate through an iterable or a known collection of items.

### Example

```python
students = ["John", "Mary", "David"]

for student in students:
    print(student)
```

Python automatically moves from one item to the next.

Unlike a typical `while` loop, you normally do not need to manually initialize and update a counter.

---

# 3. `while` vs `for`

### Use `while` when:

* Repetition depends on a condition.
* The number of iterations may be unknown.
* The loop should continue until something happens.

Example:

```python
while command != "exit":
    command = input("Enter command: ")
```

### Use `for` when:

* Iterating through a collection.
* Processing a known sequence.
* The endpoint is determined by the iterable.

Example:

```python
for student in students:
    process(student)
```

### Mental model

> `while` → "Keep going while this condition is true."

> `for` → "Go through these items."

---

# 4. `break`

`break` immediately terminates the loop.

```python
while True:
    password = input("Password: ")

    if password == "python123":
        print("Access Granted")
        break
```

Once `break` executes, Python leaves the loop completely.

### Mental model

```text
Loop
 ↓
Condition met?
 ↓
BREAK
 ↓
Leave loop
```

---

# 5. `continue`

`continue` skips the rest of the current iteration and moves to the next iteration.

Example:

```python
for number in range(1, 6):
    if number == 3:
        continue

    print(number)
```

Output:

```text
1
2
4
5
```

`continue` does **not** terminate the loop.

---

## Important `while` loop warning

This can create an infinite loop:

```python
count = 1

while count <= 5:
    if count == 3:
        continue

    print(count)
    count += 1
```

When `count` reaches 3, `continue` executes before `count += 1`.

Therefore:

```text
count = 3
↓
continue
↓
count is still 3
↓
condition is still True
↓
continue
↓
...
```

To fix it:

```python
if count == 3:
    count += 1
    continue
```

---

# 6. `pass`

`pass` is a placeholder statement.

It tells Python to do nothing at that point and continue executing normally.

Example:

```python
if settings_ready:
    pass
```

`pass` does **not**:

* stop a loop
* skip an iteration
* terminate a program
* execute a future block automatically

It simply provides a valid statement where code may be added later.

---

# 7. Loop `else`

Python allows an `else` block to be attached to a `for` or `while` loop.

The loop's `else` executes when the loop finishes **normally**, without being interrupted by `break`.

Example:

```python
for number in range(3):
    print(number)
else:
    print("Loop completed")
```

The `else` runs.

But:

```python
for number in range(3):
    if number == 1:
        break
else:
    print("Loop completed")
```

The `else` does not run because `break` interrupted the loop.

### Mental model

```text
Loop finishes naturally
        ↓
      else

break occurs
        ↓
     no else
```

`continue` does not prevent the `else` from running because `continue` does not terminate the loop.

---

# 8. Nested Loops

A nested loop is a loop inside another loop.

Example:

```python
classroom = 1

while classroom <= 2:
    print(f"Classroom {classroom}")

    student = 1

    while student <= 3:
        print(f"Student {student}")
        student += 1

    classroom += 1
```

Output:

```text
Classroom 1
Student 1
Student 2
Student 3
Classroom 2
Student 1
Student 2
Student 3
```

The **outer loop** controls the larger group.

The **inner loop** completes all of its iterations for every iteration of the outer loop.

### Important rule

In a nested `while` loop, the inner loop's counter usually needs to be reset inside the outer loop.

```python
while department <= 2:
    employee = 1

    while employee <= 3:
        ...
```

Otherwise, the inner loop may already be finished when the outer loop starts its next iteration.

---

# 9. `range()`

`range()` generates a sequence of numbers commonly used with `for` loops.

The basic form is:

```python
range(start, stop, step)
```

### Start

Where counting begins.

### Stop

Where counting stops.

The stop value is **excluded**.

### Step

How much the value changes each iteration.

---

## Examples

```python
range(5)
```

produces:

```text
0, 1, 2, 3, 4
```

Because the default start is `0` and default step is `1`.

---

```python
range(2, 7)
```

produces:

```text
2, 3, 4, 5, 6
```

---

```python
range(2, 11, 2)
```

produces:

```text
2, 4, 6, 8, 10
```

---

```python
range(10, 2, -2)
```

produces:

```text
10, 8, 6, 4
```

The `2` is excluded.

### Mental model

```text
range(start, stop, step)
       ↓      ↓      ↓
     begin   stop   movement
```

---

# 10. Strings Are Iterables

A string can be looped through character by character.

```python
for letter in "AIOS":
    print(letter)
```

Output:

```text
A
I
O
S
```

Python automatically provides one character to the loop variable during each iteration.

---

# 11. `len()`

`len()` returns the number of items in an object.

For a string:

```python
name = "Golden"

len(name)
```

returns:

```text
6
```

For a list:

```python
students = ["John", "Mary", "David"]

len(students)
```

returns:

```text
3
```

---

# 12. Indexing

Python uses zero-based indexing.

Example:

```python
word = "PYTHON"
```

The characters are stored conceptually as:

```text
Character: P  Y  T  H  O  N
Index:     0  1  2  3  4  5
```

Therefore:

```python
word[0]
```

returns:

```text
P
```

and:

```python
word[5]
```

returns:

```text
N
```

### Important relationship

```text
last index = length - 1
```

If the length is `6`, the final index is `5`.

---

# 13. `range(len())`

When both the index and the item are needed, one approach is:

```python
name = "Golden"

for i in range(len(name)):
    print(i, name[i])
```

Output:

```text
0 G
1 o
2 l
3 d
4 e
5 n
```

Here:

* `i` contains the index.
* `name[i]` retrieves the character at that index.

---

# 14. `enumerate()`

`enumerate()` provides both the index and the item during iteration.

Instead of:

```python
for i in range(len(name)):
    print(i, name[i])
```

we can write:

```python
for index, letter in enumerate(name):
    print(index, letter)
```

Output:

```text
0 G
1 o
2 l
3 d
4 e
5 n
```

This is generally cleaner and more Pythonic when both the index and item are needed.

---

## `enumerate(start=1)`

By default, `enumerate()` starts counting from `0`.

We can change the displayed counter:

```python
menu = ["Calculator", "Profile", "Settings"]

for index, item in enumerate(menu, start=1):
    print(index, item)
```

Output:

```text
1 Calculator
2 Profile
3 Settings
```

Important:

`start=1` changes the counter produced by `enumerate()`. It does not change Python's underlying zero-based indexing.

---

# 15. Choosing the Right Loop Pattern

### Need only the items?

```python
for item in iterable:
```

### Need the index and item?

```python
for index, item in enumerate(iterable):
```

### Specifically need to work with indexes?

```python
for i in range(len(iterable)):
```

### Need to repeat until a condition changes?

```python
while condition:
```

---

# 16. Common Loop Bugs

## Forgetting the update

```python
count = 1

while count <= 5:
    print(count)
```

The condition never changes, creating an infinite loop.

---

## Using `continue` before updating

```python
if count == 3:
    continue

count += 1
```

If `count` equals 3, the update never happens.

---

## Incorrect loop variable

```python
students = ["John", "Mary"]

for student in students:
    print(students)
```

This prints the entire list repeatedly.

The intended code is:

```python
for student in students:
    print(student)
```

---

## Confusing singular and collection variables

```python
students = ["John", "Mary", "David"]

for student in students:
    ...
```

Mental model:

```text
students → collection
student  → one item
```

---

# 17. AIOS Application

Loops became an important part of the Developer OS project.

The AIOS main menu uses a `while` loop to keep the system running:

```python
logged_in = True

while logged_in:
    ...
```

The menu can continue appearing until the user chooses Exit.

The menu itself can be displayed using `enumerate()`:

```python
menu = ["profile", "calculator", "settings", "exit"]

for index, value in enumerate(menu, start=1):
    print(f"{index}: {value.title()}")
```

This demonstrates how loops can control actual program flow rather than simply counting numbers.

---

# 18. Loop Mastery Assessment

A comprehensive assessment was completed covering:

* `while` loops
* `for` loops
* `range()`
* `break`
* `continue`
* `pass`
* loop `else`
* nested loops
* strings as iterables
* `len()`
* indexing
* `range(len())`
* `enumerate()`
* loop selection
* debugging
* AIOS control flow

### Result

**76/80 — 95%**

The assessment demonstrated strong understanding of loop concepts and practical application.

### Minor areas identified for improvement

1. A `while` loop is not inherently infinite; it becomes infinite only when its termination condition is never reached.
2. `range()` follows the exact step specified.
3. Singular and collection variable names should be distinguished clearly:

   ```python
   students = [...]
   for student in students:
   ```
4. When using a loop variable, make sure the variable itself—not the entire collection—is referenced.

---

# Sprint 6 Loop Mastery Status

**COMPLETED ✅**

The foundational loop concepts are now understood well enough to move forward.

Next major Python topic:

# Lists

Lists will build directly on the loop knowledge developed in this sprint because lists are one of Python's most important collections and are frequently processed using `for` loops, `while` loops, indexing, `len()`, and `enumerate()`.
