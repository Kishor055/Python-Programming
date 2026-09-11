"""
04_break.py
===========

Python break Statement

The `break` statement immediately terminates the nearest
enclosing loop.

Syntax:

    for item in iterable:
        if condition:
            break

    while condition:
        if condition:
            break

Use `break` when you need to stop looping as soon as a
specific condition is satisfied.
"""


# ============================================================
# 1. BASIC BREAK
# ============================================================

for number in range(1, 11):

    if number == 5:
        break

    print(number)


# ============================================================
# 2. BREAK IN A WHILE LOOP
# ============================================================

number = 1

while number <= 10:

    if number == 6:
        break

    print(number)

    number += 1


# ============================================================
# 3. STOP AT A SPECIFIC VALUE
# ============================================================

for number in range(1, 21):

    print(number)

    if number == 10:
        break


# ============================================================
# 4. SEARCH FOR AN ELEMENT
# ============================================================

numbers = [10, 20, 30, 40, 50]

target = 30

for number in numbers:

    if number == target:
        print("Found:", target)
        break


# ============================================================
# 5. SEARCH WITH INDEX
# ============================================================

numbers = [10, 20, 30, 40, 50]

target = 40

for index in range(len(numbers)):

    if numbers[index] == target:
        print("Found at index:", index)
        break


# ============================================================
# 6. SEARCH FOR A STRING
# ============================================================

languages = [
    "Python",
    "Java",
    "C++",
    "JavaScript"
]

target = "C++"

for language in languages:

    if language == target:
        print("Found:", language)
        break


# ============================================================
# 7. SEARCH WITH FOR-ELSE
# ============================================================

numbers = [10, 20, 30, 40]

target = 30

for number in numbers:

    if number == target:
        print("Found:", target)
        break

else:
    print("Not found")


# ============================================================
# 8. FOR-ELSE WHEN ELEMENT IS MISSING
# ============================================================

numbers = [10, 20, 30, 40]

target = 100

for number in numbers:

    if number == target:
        print("Found:", target)
        break

else:
    print("Not found")


# ============================================================
# 9. FIND FIRST EVEN NUMBER
# ============================================================

numbers = [11, 13, 17, 24, 30, 42]

for number in numbers:

    if number % 2 == 0:
        print("First even number:", number)
        break


# ============================================================
# 10. FIND FIRST ODD NUMBER
# ============================================================

numbers = [10, 20, 32, 45, 50]

for number in numbers:

    if number % 2 != 0:
        print("First odd number:", number)
        break


# ============================================================
# 11. FIND FIRST NEGATIVE NUMBER
# ============================================================

numbers = [10, 20, 30, -5, 40, -10]

for number in numbers:

    if number < 0:
        print("First negative:", number)
        break


# ============================================================
# 12. FIND FIRST POSITIVE NUMBER
# ============================================================

numbers = [-10, -20, 0, 25, 30]

for number in numbers:

    if number > 0:
        print("First positive:", number)
        break


# ============================================================
# 13. STOP WHEN SUM REACHES A LIMIT
# ============================================================

numbers = [10, 20, 30, 40, 50]

total = 0
limit = 60

for number in numbers:

    total += number

    if total >= limit:
        break

print("Total:", total)


# ============================================================
# 14. STOP WHEN PRODUCT EXCEEDS LIMIT
# ============================================================

numbers = [2, 3, 4, 5, 6]

product = 1
limit = 50

for number in numbers:

    product *= number

    if product > limit:
        break

print("Product:", product)


# ============================================================
# 15. BREAK IN NESTED LOOP
# ============================================================
# `break` terminates only the nearest enclosing loop.


for row in range(3):

    for column in range(5):

        if column == 2:
            break

        print(row, column)


# ============================================================
# 16. BREAK FROM INNER LOOP
# ============================================================

for row in range(1, 4):

    print("Row:", row)

    for column in range(1, 6):

        if column == 3:
            break

        print("Column:", column)


# ============================================================
# 17. BREAK FROM BOTH LOOPS USING A FLAG
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target = 5

found = False

for row in matrix:

    for value in row:

        if value == target:
            found = True
            break

    if found:
        break

print("Found:", found)


# ============================================================
# 18. FIND POSITION IN MATRIX
# ============================================================

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

target = 60

found = False

for row_index in range(len(matrix)):

    for column_index in range(
        len(matrix[row_index])
    ):

        if matrix[row_index][column_index] == target:

            print(
                "Found at:",
                row_index,
                column_index
            )

            found = True
            break

    if found:
        break


# ============================================================
# 19. BREAK WITH WHILE TRUE
# ============================================================
# `while True` creates a loop that requires an explicit
# termination condition such as `break`.


counter = 1

while True:

    print(counter)

    if counter == 5:
        break

    counter += 1


# ============================================================
# 20. INFINITE LOOP WITH BREAK
# ============================================================

number = 1

while True:

    if number > 5:
        break

    print(number)

    number += 1


# ============================================================
# 21. USER INPUT LOOP
# ============================================================
# Uncomment to run interactively.
#
# while True:
#
#     value = input("Enter 'exit' to stop: ")
#
#     if value.lower() == "exit":
#         break
#
#     print("You entered:", value)


# ============================================================
# 22. STOP WHEN USER ENTERS ZERO
# ============================================================
# Uncomment to run interactively.
#
# while True:
#
#     number = int(input("Enter a number: "))
#
#     if number == 0:
#         break
#
#     print("Number:", number)


# ============================================================
# 23. SUM INPUT UNTIL ZERO
# ============================================================
# Uncomment to run interactively.
#
# total = 0
#
# while True:
#
#     number = int(input("Enter number (0 to stop): "))
#
#     if number == 0:
#         break
#
#     total += number
#
# print("Total:", total)


# ============================================================
# 24. INPUT VALIDATION
# ============================================================
# Uncomment to run interactively.
#
# while True:
#
#     age = int(input("Enter age: "))
#
#     if 0 <= age <= 120:
#         break
#
#     print("Invalid age. Try again.")
#
# print("Valid age:", age)


# ============================================================
# 25. PASSWORD ATTEMPTS
# ============================================================

correct_password = "python123"

passwords = [
    "hello",
    "admin",
    "python123"
]

for password in passwords:

    if password == correct_password:
        print("Login successful")
        break

    print("Incorrect password")


# ============================================================
# 26. MAXIMUM ATTEMPTS
# ============================================================

correct_password = "python123"

attempts = [
    "hello",
    "admin",
    "python123"
]

max_attempts = 3

for attempt in range(max_attempts):

    password = attempts[attempt]

    if password == correct_password:
        print("Login successful")
        break

    print("Incorrect password")


# ============================================================
# 27. RETRY LOGIC
# ============================================================

max_retries = 5

for attempt in range(1, max_retries + 1):

    print("Attempt:", attempt)

    if attempt == 3:
        print("Operation successful")
        break


# ============================================================
# 28. FIND FIRST MATCH
# ============================================================

names = [
    "Rahul",
    "Amit",
    "Kishor",
    "Rohit"
]

for name in names:

    if name == "Kishor":
        print("Match found")
        break


# ============================================================
# 29. FIND FIRST NUMBER GREATER THAN 50
# ============================================================

numbers = [10, 20, 45, 60, 70, 80]

for number in numbers:

    if number > 50:
        print("First number greater than 50:", number)
        break


# ============================================================
# 30. FIND FIRST NUMBER DIVISIBLE BY 7
# ============================================================

for number in range(1, 100):

    if number % 7 == 0:
        print("First multiple of 7:", number)
        break


# ============================================================
# 31. PRIME NUMBER CHECK
# ============================================================

number = 29

if number < 2:

    print("Not prime")

else:

    for divisor in range(2, int(number ** 0.5) + 1):

        if number % divisor == 0:
            print("Not prime")
            break

    else:
        print("Prime")


# ============================================================
# 32. PRIME NUMBER SEARCH
# ============================================================

for number in range(2, 100):

    is_prime = True

    for divisor in range(2, int(number ** 0.5) + 1):

        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print("First prime found:", number)
        break


# ============================================================
# 33. FIND FACTOR
# ============================================================

number = 36

for divisor in range(2, number + 1):

    if number % divisor == 0:
        print("First factor:", divisor)
        break


# ============================================================
# 34. STOP AT A CHARACTER
# ============================================================

text = "Python Programming"

for character in text:

    if character == " ":
        break

    print(character)


# ============================================================
# 35. FIND FIRST VOWEL
# ============================================================

text = "cryptography education"

for character in text:

    if character.lower() in "aeiou":
        print("First vowel:", character)
        break


# ============================================================
# 36. FIND FIRST UPPERCASE CHARACTER
# ============================================================

text = "python Programming"

for character in text:

    if character.isupper():
        print("First uppercase:", character)
        break


# ============================================================
# 37. FIND FIRST DIGIT
# ============================================================

text = "Python123"

for character in text:

    if character.isdigit():
        print("First digit:", character)
        break


# ============================================================
# 38. FIND FIRST SPECIAL CHARACTER
# ============================================================

text = "Python@123"

for character in text:

    if not character.isalnum():
        print("First special character:", character)
        break


# ============================================================
# 39. STOP PROCESSING AT EMPTY STRING
# ============================================================

values = [
    "Python",
    "Java",
    "",
    "C++",
    "Go"
]

for value in values:

    if value == "":
        break

    print(value)


# ============================================================
# 40. PROCESS UNTIL SENTINEL
# ============================================================

values = [10, 20, 30, 0, 40, 50]

for value in values:

    if value == 0:
        break

    print(value)


# ============================================================
# 41. STOP PROCESSING TASKS
# ============================================================

tasks = [
    "Task 1",
    "Task 2",
    "STOP",
    "Task 3",
    "Task 4"
]

for task in tasks:

    if task == "STOP":
        break

    print("Processing:", task)


# ============================================================
# 42. FIND FIRST DUPLICATE
# ============================================================

numbers = [10, 20, 30, 20, 40]

seen = set()

for number in numbers:

    if number in seen:
        print("First duplicate:", number)
        break

    seen.add(number)


# ============================================================
# 43. FIND FIRST DUPLICATE WITHOUT SET
# ============================================================

numbers = [10, 20, 30, 20, 40]

for index in range(len(numbers)):

    for previous in range(index):

        if numbers[index] == numbers[previous]:

            print(
                "First duplicate:",
                numbers[index]
            )

            break

    else:
        continue

    break


# ============================================================
# 44. FIND PAIR WITH TARGET SUM
# ============================================================

numbers = [2, 4, 6, 8, 10]

target = 12

found = False

for first_index in range(len(numbers)):

    for second_index in range(
        first_index + 1,
        len(numbers)
    ):

        if (
            numbers[first_index]
            + numbers[second_index]
            == target
        ):

            print(
                "Pair:",
                numbers[first_index],
                numbers[second_index]
            )

            found = True
            break

    if found:
        break


# ============================================================
# 45. FIND FIRST COMMON ELEMENT
# ============================================================

list_a = [1, 2, 3, 4]
list_b = [5, 6, 3, 7]

found = False

for first in list_a:

    for second in list_b:

        if first == second:

            print("First common element:", first)

            found = True
            break

    if found:
        break


# ============================================================
# 46. SORTING WITH BREAK
# ============================================================
# Bubble sort can use break when no swaps occur.


numbers = [1, 2, 3, 4, 5]

for outer in range(len(numbers)):

    swapped = False

    for inner in range(
        len(numbers) - outer - 1
    ):

        if numbers[inner] > numbers[inner + 1]:

            numbers[inner], numbers[inner + 1] = (
                numbers[inner + 1],
                numbers[inner]
            )

            swapped = True

    if not swapped:
        break

print("Sorted:", numbers)


# ============================================================
# 47. STOP WHEN CONDITION IS MET
# ============================================================

balance = 1000

withdrawals = [
    100,
    200,
    300,
    500,
    100
]

for withdrawal in withdrawals:

    if withdrawal > balance:
        print("Insufficient balance")
        break

    balance -= withdrawal

    print(
        "Withdrawn:",
        withdrawal,
        "Balance:",
        balance
    )


# ============================================================
# 48. PROCESS UNTIL ERROR
# ============================================================

values = [10, 20, 30, -1, 40]

for value in values:

    if value < 0:
        print("Invalid value:", value)
        break

    print("Processing:", value)


# ============================================================
# 49. BREAK WITH ENUMERATE
# ============================================================

languages = [
    "Python",
    "Java",
    "C++",
    "Go"
]

for index, language in enumerate(languages):

    if language == "C++":
        print("Found at index:", index)
        break


# ============================================================
# 50. BREAK WITH DICTIONARY
# ============================================================

students = {
    "Kishor": 90,
    "Rahul": 75,
    "Amit": 85
}

for name, marks in students.items():

    if marks >= 90:
        print(
            "First student with 90+:",
            name
        )
        break


# ============================================================
# 51. BREAK WHEN CONDITION BECOMES FALSE
# ============================================================

number = 1

while True:

    if number > 5:
        break

    print(number)

    number += 1


# ============================================================
# 52. COUNTDOWN USING BREAK
# ============================================================

number = 10

while True:

    print(number)

    number -= 1

    if number == 0:
        break


# ============================================================
# 53. STOP AT MULTIPLE OF 10
# ============================================================

number = 1

while True:

    print(number)

    if number % 10 == 0:
        break

    number += 1


# ============================================================
# 54. BREAK AFTER N ITERATIONS
# ============================================================

counter = 0

while True:

    counter += 1

    print("Iteration:", counter)

    if counter == 5:
        break


# ============================================================
# 55. BREAK AFTER PROCESSING N ITEMS
# ============================================================

items = [
    "Item 1",
    "Item 2",
    "Item 3",
    "Item 4",
    "Item 5"
]

limit = 3

for index, item in enumerate(items):

    if index == limit:
        break

    print("Processing:", item)


# ============================================================
# 56. BREAK FROM MENU LOOP
# ============================================================
# Uncomment to run interactively.
#
# while True:
#
#     print("\n1. Add")
#     print("2. View")
#     print("3. Exit")
#
#     choice = input("Choose: ")
#
#     if choice == "1":
#         print("Add selected")
#
#     elif choice == "2":
#         print("View selected")
#
#     elif choice == "3":
#         print("Exiting...")
#         break
#
#     else:
#         print("Invalid choice")


# ============================================================
# 57. BREAK IN EXCEPTION HANDLING
# ============================================================
# Uncomment to run interactively.
#
# while True:
#
#     try:
#         number = int(
#             input("Enter an integer: ")
#         )
#         break
#
#     except ValueError:
#         print("Invalid input. Try again.")
#
# print("Valid number:", number)


# ============================================================
# 58. BREAK AFTER SUCCESSFUL OPERATION
# ============================================================

operations = [
    False,
    False,
    True,
    False
]

for success in operations:

    print("Trying operation...")

    if success:
        print("Operation succeeded")
        break


# ============================================================
# 59. FIND FIRST VALID RECORD
# ============================================================

records = [
    {"name": "A", "age": -1},
    {"name": "B", "age": 0},
    {"name": "C", "age": 25},
    {"name": "D", "age": 30}
]

for record in records:

    if record["age"] > 0:
        print("First valid record:", record)
        break


# ============================================================
# 60. STOP WHEN SCORE REACHES TARGET
# ============================================================

scores = [10, 20, 15, 30, 40]

target = 50
total = 0

for score in scores:

    total += score

    if total >= target:
        print("Target reached:", total)
        break


# ============================================================
# 61. BREAK WITH RANGE
# ============================================================

for number in range(100):

    if number == 10:
        break

    print(number)


# ============================================================
# 62. BREAK WITH REVERSED RANGE
# ============================================================

for number in range(20, 0, -1):

    if number == 10:
        break

    print(number)


# ============================================================
# 63. BREAK WITH ZIP
# ============================================================

names = ["Kishor", "Rahul", "Amit"]
marks = [90, 75, 85]

for name, mark in zip(names, marks):

    if mark >= 85:
        print(
            name,
            mark
        )
        break


# ============================================================
# 64. BREAK WITH NESTED WHILE LOOPS
# ============================================================

row = 1

while row <= 3:

    column = 1

    while column <= 5:

        if column == 3:
            break

        print(
            row,
            column
        )

        column += 1

    row += 1


# ============================================================
# 65. BREAK FROM MATRIX SEARCH
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target = 7

found = False

for row in matrix:

    for value in row:

        if value == target:
            found = True
            break

    if found:
        break

print("Found:", found)


# ============================================================
# 66. BREAK WITH FLAG
# ============================================================

numbers = [10, 20, 30, 40]

target = 30
found = False

for number in numbers:

    if number == target:

        found = True

        break

if found:
    print("Target found")
else:
    print("Target not found")


# ============================================================
# 67. FIRST NUMBER GREATER THAN AVERAGE
# ============================================================

numbers = [10, 20, 30, 40, 50]

average = sum(numbers) / len(numbers)

for number in numbers:

    if number > average:

        print(
            "First number above average:",
            number
        )

        break


# ============================================================
# 68. STOP WHEN STRING LENGTH REACHES LIMIT
# ============================================================

words = [
    "Python",
    "Programming",
    "Language"
]

limit = 8

for word in words:

    if len(word) >= limit:
        print(
            "First long word:",
            word
        )
        break


# ============================================================
# 69. STOP AT FIRST MATCHING PREFIX
# ============================================================

names = [
    "Rahul",
    "Amit",
    "Kishor",
    "Kiran"
]

for name in names:

    if name.startswith("Ki"):
        print(
            "First matching name:",
            name
        )
        break


# ============================================================
# 70. STOP AT FIRST PALINDROME
# ============================================================

words = [
    "python",
    "hello",
    "level",
    "world"
]

for word in words:

    if word == word[::-1]:
        print(
            "First palindrome:",
            word
        )
        break


# ============================================================
# 71. STOP AT FIRST ARMSTRONG NUMBER
# ============================================================

for number in range(100, 1000):

    digits = str(number)
    total = 0

    for digit in digits:
        total += int(digit) ** 3

    if total == number:
        print(
            "First Armstrong number:",
            number
        )
        break


# ============================================================
# 72. BREAK IN SEARCH ALGORITHM
# ============================================================

numbers = [3, 7, 12, 18, 25, 31]

target = 18

for index, number in enumerate(numbers):

    if number == target:

        print(
            "Target index:",
            index
        )

        break


# ============================================================
# 73. BREAK VS CONTINUE
# ============================================================

numbers = range(1, 6)

for number in numbers:

    if number == 3:
        break

    print(number)

# Output:
# 1
# 2


for number in numbers:

    if number == 3:
        continue

    print(number)

# Output:
# 1
# 2
# 4
# 5


# ============================================================
# 74. BREAK VS PASS
# ============================================================

for number in range(1, 6):

    if number == 3:
        pass

    print(number)

# `pass` does not stop the loop.


for number in range(1, 6):

    if number == 3:
        break

    print(number)

# `break` stops the loop.


# ============================================================
# 75. COMMON MISTAKE — BREAK OUTSIDE LOOP
# ============================================================

"""
Incorrect:

    if condition:
        break

`break` can only be used inside a loop.

Valid:

    for number in numbers:
        if number == 10:
            break
"""


# ============================================================
# 76. COMMON MISTAKE — EXPECTING BREAK TO EXIT ALL LOOPS
# ============================================================

"""
Example:

    for row in range(3):

        for column in range(3):

            if column == 1:
                break

`break` exits only the inner loop.

The outer loop continues.

To stop both loops, use a flag:

    found = False

    for row in matrix:

        for value in row:

            if condition:
                found = True
                break

        if found:
            break
"""


# ============================================================
# 77. COMMON MISTAKE — UNREACHABLE CODE
# ============================================================

"""
Example:

    for number in numbers:

        break

        print(number)

The print statement can never execute because `break`
terminates the loop before reaching it.
"""


# ============================================================
# 78. COMMON MISTAKE — BREAK TOO EARLY
# ============================================================

numbers = [10, 20, 30, 40]

for number in numbers:

    if number > 10:
        break

    print(number)

# The loop stops at 20.
# Only 10 is printed.


# ============================================================
# 79. PROFESSIONAL SEARCH PATTERN
# ============================================================

numbers = [10, 20, 30, 40, 50]

target = 30

for index, number in enumerate(numbers):

    if number == target:
        print(
            f"Found {target} at index {index}"
        )
        break

else:
    print(
        f"{target} was not found"
    )


# ============================================================
# 80. PROFESSIONAL BREAK PATTERN
# ============================================================

"""
Use `break` when:

    - The desired item has been found.
    - A successful operation has completed.
    - A termination/sentinel value is reached.
    - A limit has been reached.
    - An invalid state is detected.
    - An interactive loop needs to exit.
    - Further processing is unnecessary.

Good example:

    for item in items:
        if is_target(item):
            result = item
            break

This avoids processing unnecessary items.
"""


# ============================================================
# 81. PERFORMANCE BENEFIT
# ============================================================

"""
Without break:

    for number in numbers:
        if number == target:
            print("Found")

The loop continues checking all remaining elements.

With break:

    for number in numbers:
        if number == target:
            print("Found")
            break

The loop stops immediately after finding the target.

For large collections, early termination can reduce
unnecessary work.
"""


# ============================================================
# 82. BREAK AND FOR-ELSE
# ============================================================

"""
The `else` block of a loop runs only when the loop
finishes normally.

If `break` executes, the loop's `else` block is skipped.

Example:

    for number in numbers:

        if number == target:
            break

    else:
        print("Target not found")

This is a clean pattern for searching.
"""


# ============================================================
# 83. BREAK AND WHILE-ELSE
# ============================================================

number = 1

while number <= 10:

    if number == 5:
        break

    print(number)

    number += 1

else:
    print("Loop completed normally")

# The else block does not execute because break was used.


# ============================================================
# 84. REAL-WORLD EXAMPLE — QUEUE PROCESSING
# ============================================================

queue = [
    "Request 1",
    "Request 2",
    "STOP",
    "Request 3"
]

for request in queue:

    if request == "STOP":
        break

    print("Processing:", request)


# ============================================================
# 85. REAL-WORLD EXAMPLE — TRANSACTION LIMIT
# ============================================================

transactions = [100, 200, 150, 300, 250]

limit = 500
total = 0

for transaction in transactions:

    if total + transaction > limit:
        print("Transaction limit reached")
        break

    total += transaction

print("Processed total:", total)


# ============================================================
# 86. REAL-WORLD EXAMPLE — FIRST VALID SERVER
# ============================================================

servers = [
    {"name": "Server A", "available": False},
    {"name": "Server B", "available": False},
    {"name": "Server C", "available": True},
    {"name": "Server D", "available": True}
]

for server in servers:

    if server["available"]:

        print(
            "Using:",
            server["name"]
        )

        break


# ============================================================
# 87. REAL-WORLD EXAMPLE — FIRST PASSING STUDENT
# ============================================================

students = [
    {"name": "Amit", "marks": 30},
    {"name": "Rahul", "marks": 35},
    {"name": "Kishor", "marks": 75}
]

for student in students:

    if student["marks"] >= 40:

        print(
            "First passing student:",
            student["name"]
        )

        break


# ============================================================
# 88. REAL-WORLD EXAMPLE — FIRST AVAILABLE PRODUCT
# ============================================================

products = [
    {"name": "Laptop", "stock": 0},
    {"name": "Mouse", "stock": 0},
    {"name": "Keyboard", "stock": 10},
    {"name": "Monitor", "stock": 5}
]

for product in products:

    if product["stock"] > 0:

        print(
            "Available product:",
            product["name"]
        )

        break


# ============================================================
# 89. REAL-WORLD EXAMPLE — STOP ON ERROR
# ============================================================

operations = [
    "success",
    "success",
    "error",
    "success"
]

for operation in operations:

    if operation == "error":

        print("Error encountered")

        break

    print("Operation successful")


# ============================================================
# 90. REAL-WORLD EXAMPLE — FILE-LIKE PROCESSING
# ============================================================

lines = [
    "Python",
    "Programming",
    "STOP",
    "Language"
]

for line in lines:

    if line == "STOP":
        break

    print("Reading:", line)


# ============================================================
# 91. REAL-WORLD EXAMPLE — SEARCH FIRST MATCH
# ============================================================

users = [
    {"name": "Amit", "active": False},
    {"name": "Rahul", "active": False},
    {"name": "Kishor", "active": True},
    {"name": "Rohit", "active": True}
]

for user in users:

    if user["active"]:

        print(
            "First active user:",
            user["name"]
        )

        break


# ============================================================
# 92. REAL-WORLD EXAMPLE — STOP AFTER SUCCESS
# ============================================================

results = [
    False,
    False,
    False,
    True,
    True
]

for result in results:

    if result:

        print("Success found")

        break


# ============================================================
# 93. REAL-WORLD EXAMPLE — BATCH LIMIT
# ============================================================

items = [
    "Item 1",
    "Item 2",
    "Item 3",
    "Item 4",
    "Item 5"
]

batch_limit = 3

count = 0

for item in items:

    if count == batch_limit:
        break

    print("Processing:", item)

    count += 1


# ============================================================
# 94. REAL-WORLD EXAMPLE — STOP AT INVALID DATA
# ============================================================

data = [10, 20, 30, 40, -1, 50]

for value in data:

    if value < 0:

        print(
            "Invalid value encountered:",
            value
        )

        break

    print("Valid:", value)


# ============================================================
# 95. REAL-WORLD EXAMPLE — STOP WHEN TARGET FOUND
# ============================================================

inventory = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor"
]

requested_item = "Keyboard"

for item in inventory:

    if item == requested_item:

        print(
            "Item available:",
            item
        )

        break


# ============================================================
# 96. KEY RULES
# ============================================================

"""
KEY RULES
---------

1. `break` immediately terminates the nearest loop.

2. `break` works with:
       - for loops
       - while loops

3. `break` does not terminate surrounding code.

4. In nested loops, `break` exits only the nearest loop.

5. Use a flag when an inner loop needs to stop an outer loop.

6. A loop's `else` block does not execute if `break` occurs.

7. `break` is useful for early termination.

8. Avoid unnecessary `break` statements when a normal loop
   condition provides clearer control flow.

9. Use `break` for explicit termination conditions.

10. Keep the reason for breaking the loop easy to understand.
"""


# ============================================================
# 97. BREAK VS NORMAL LOOP TERMINATION
# ============================================================

"""
Normal termination:

    for number in range(5):
        print(number)

The loop naturally ends after all values are processed.

Early termination:

    for number in range(100):
        if number == 5:
            break
        print(number)

The loop ends before processing all values.
"""


# ============================================================
# 98. BREAK VS CONTINUE VS PASS
# ============================================================

"""
break
-----
Stops the entire nearest loop.

continue
--------
Skips the current iteration and continues with the next one.

pass
----
Does nothing and continues normal execution.

Example:

    for number in range(5):

        if number == 2:
            break

    # Loop stops completely.


    for number in range(5):

        if number == 2:
            continue

        # 2 is skipped.


    for number in range(5):

        if number == 2:
            pass

        # Nothing special happens.
"""


# ============================================================
# 99. BEST PRACTICE
# ============================================================

"""
BEST PRACTICE
-------------

Prefer:

    for item in items:

        if condition(item):
            result = item
            break

over unnecessarily complicated loop conditions when
the purpose is simply to stop after finding a result.

For nested loops, make the exit behavior explicit:

    found = False

    for row in matrix:

        for value in row:

            if value == target:
                found = True
                break

        if found:
            break
"""


# ============================================================
# 100. SUMMARY
# ============================================================

"""
SUMMARY
-------

break is one of Python's fundamental loop-control statements.

It is primarily used for:

    - Early termination
    - Searching
    - Validation
    - Retry logic
    - Sentinel-controlled loops
    - Interactive menus
    - Error handling
    - Limit enforcement
    - Matrix searching
    - Avoiding unnecessary iterations

Core syntax:

    for item in iterable:
        if condition:
            break

    while condition:
        if condition:
            break

Remember:

    break
        -> Exit the nearest loop immediately.

    continue
        -> Skip the current iteration.

    pass
        -> Do nothing.

Understanding the difference between these three statements
is essential for writing clear Python control flow.
"""


# ============================================================
# END OF BREAK
# ============================================================

print("\nBreak statement demonstration completed successfully!")
