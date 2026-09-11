"""
02_while_loop.py
================

Python while Loop

A while loop repeatedly executes a block of code as long as
a condition evaluates to True.

Syntax:

    while condition:
        # code

A while loop is useful when the number of iterations is not
known in advance and execution depends on a condition.
"""


# ============================================================
# 1. BASIC WHILE LOOP
# ============================================================

count = 1

while count <= 5:
    print(count)
    count += 1


# ============================================================
# 2. COUNT FROM 1 TO 10
# ============================================================

number = 1

while number <= 10:
    print(number)
    number += 1


# ============================================================
# 3. COUNTDOWN
# ============================================================

number = 10

while number >= 1:
    print(number)
    number -= 1


# ============================================================
# 4. EVEN NUMBERS
# ============================================================

number = 2

while number <= 10:
    print(number)
    number += 2


# ============================================================
# 5. ODD NUMBERS
# ============================================================

number = 1

while number <= 10:
    print(number)
    number += 2


# ============================================================
# 6. SUM OF NUMBERS
# ============================================================

number = 1
total = 0

while number <= 10:
    total += number
    number += 1

print("Total:", total)


# ============================================================
# 7. PRODUCT OF NUMBERS
# ============================================================

number = 1
product = 1

while number <= 5:
    product *= number
    number += 1

print("Product:", product)


# ============================================================
# 8. MULTIPLICATION TABLE
# ============================================================

number = 5
multiplier = 1

while multiplier <= 10:
    print(
        f"{number} x {multiplier} = "
        f"{number * multiplier}"
    )
    multiplier += 1


# ============================================================
# 9. SQUARES
# ============================================================

number = 1

while number <= 5:
    print(number ** 2)
    number += 1


# ============================================================
# 10. CUBES
# ============================================================

number = 1

while number <= 5:
    print(number ** 3)
    number += 1


# ============================================================
# 11. ITERATE THROUGH A LIST
# ============================================================

languages = ["Python", "Java", "C++", "JavaScript"]

index = 0

while index < len(languages):
    print(languages[index])
    index += 1


# ============================================================
# 12. ITERATE THROUGH A STRING
# ============================================================

text = "Python"

index = 0

while index < len(text):
    print(text[index])
    index += 1


# ============================================================
# 13. REVERSE ITERATION
# ============================================================

numbers = [10, 20, 30, 40, 50]

index = len(numbers) - 1

while index >= 0:
    print(numbers[index])
    index -= 1


# ============================================================
# 14. FIND LIST TOTAL
# ============================================================

numbers = [10, 20, 30, 40, 50]

index = 0
total = 0

while index < len(numbers):
    total += numbers[index]
    index += 1

print("Total:", total)


# ============================================================
# 15. FIND MAXIMUM
# ============================================================

numbers = [10, 50, 30, 90, 20]

index = 0
maximum = numbers[0]

while index < len(numbers):

    if numbers[index] > maximum:
        maximum = numbers[index]

    index += 1

print("Maximum:", maximum)


# ============================================================
# 16. FIND MINIMUM
# ============================================================

numbers = [10, 50, 30, 90, 20]

index = 0
minimum = numbers[0]

while index < len(numbers):

    if numbers[index] < minimum:
        minimum = numbers[index]

    index += 1

print("Minimum:", minimum)


# ============================================================
# 17. COUNT EVEN NUMBERS
# ============================================================

numbers = [10, 15, 22, 31, 40, 55]

index = 0
count = 0

while index < len(numbers):

    if numbers[index] % 2 == 0:
        count += 1

    index += 1

print("Even numbers:", count)


# ============================================================
# 18. COUNT ODD NUMBERS
# ============================================================

numbers = [10, 15, 22, 31, 40, 55]

index = 0
count = 0

while index < len(numbers):

    if numbers[index] % 2 != 0:
        count += 1

    index += 1

print("Odd numbers:", count)


# ============================================================
# 19. FILTER EVEN NUMBERS
# ============================================================

numbers = [10, 15, 22, 31, 40, 55]

index = 0
even_numbers = []

while index < len(numbers):

    if numbers[index] % 2 == 0:
        even_numbers.append(numbers[index])

    index += 1

print(even_numbers)


# ============================================================
# 20. BREAK
# ============================================================
# break immediately terminates the while loop.


number = 1

while number <= 10:

    if number == 5:
        break

    print(number)
    number += 1


# ============================================================
# 21. BREAK — SEARCH
# ============================================================

numbers = [10, 20, 30, 40, 50]

target = 30
index = 0

while index < len(numbers):

    if numbers[index] == target:
        print("Found:", target)
        break

    index += 1


# ============================================================
# 22. CONTINUE
# ============================================================
# continue skips the current iteration.


number = 0

while number < 10:

    number += 1

    if number == 5:
        continue

    print(number)


# ============================================================
# 23. PRINT ONLY ODD NUMBERS
# ============================================================

number = 0

while number < 10:

    number += 1

    if number % 2 == 0:
        continue

    print(number)


# ============================================================
# 24. PASS
# ============================================================
# pass does nothing and acts as a placeholder.


number = 1

while number <= 5:
    pass

    # This loop is intentionally incomplete.
    # A real loop must eventually change the condition.


# ============================================================
# 25. WHILE-ELSE
# ============================================================
# else executes when the loop ends normally.
# It does not execute if break terminates the loop.


number = 1

while number <= 5:
    print(number)
    number += 1
else:
    print("Loop completed")


# ============================================================
# 26. WHILE-ELSE WITH BREAK
# ============================================================

number = 1

while number <= 10:

    if number == 5:
        break

    print(number)
    number += 1

else:
    print("Loop completed")


# ============================================================
# 27. SEARCH USING WHILE-ELSE
# ============================================================

numbers = [10, 20, 30, 40]

target = 30
index = 0

while index < len(numbers):

    if numbers[index] == target:
        print("Found:", target)
        break

    index += 1

else:
    print("Not found")


# ============================================================
# 28. SEARCH FOR MISSING VALUE
# ============================================================

numbers = [10, 20, 30, 40]

target = 50
index = 0

while index < len(numbers):

    if numbers[index] == target:
        print("Found:", target)
        break

    index += 1

else:
    print("Not found")


# ============================================================
# 29. INFINITE LOOP
# ============================================================
# An infinite loop continues forever unless interrupted.
#
# Example:
#
# while True:
#     print("Running...")
#
# Use break to provide a controlled exit.


# ============================================================
# 30. CONTROLLED INFINITE LOOP
# ============================================================

counter = 1

while True:

    print(counter)

    if counter == 5:
        break

    counter += 1


# ============================================================
# 31. USER INPUT LOOP
# ============================================================
# Repeatedly accepts input until a condition is met.


# Uncomment to run interactively:
#
# while True:
#     value = input("Enter 'exit' to stop: ")
#
#     if value.lower() == "exit":
#         break
#
#     print("You entered:", value)


# ============================================================
# 32. PASSWORD ATTEMPTS
# ============================================================

correct_password = "python123"

attempts = 0
max_attempts = 3

passwords = [
    "hello",
    "admin",
    "python123"
]

while attempts < max_attempts:

    password = passwords[attempts]

    if password == correct_password:
        print("Login successful")
        break

    print("Incorrect password")

    attempts += 1


# ============================================================
# 33. COUNTDOWN TIMER
# ============================================================

seconds = 5

while seconds > 0:
    print(seconds)
    seconds -= 1

print("Time's up!")


# ============================================================
# 34. FACTORIAL
# ============================================================

number = 5

factorial = 1
current = 1

while current <= number:
    factorial *= current
    current += 1

print("Factorial:", factorial)


# ============================================================
# 35. FIBONACCI SERIES
# ============================================================

terms = 10

first = 0
second = 1
count = 0

while count < terms:

    print(first, end=" ")

    first, second = second, first + second
    count += 1

print()


# ============================================================
# 36. SUM OF DIGITS
# ============================================================

number = 12345

total = 0
value = number

while value > 0:

    digit = value % 10
    total += digit
    value //= 10

print("Sum:", total)


# ============================================================
# 37. COUNT DIGITS
# ============================================================

number = 123456

value = number
count = 0

while value > 0:
    value //= 10
    count += 1

print("Digits:", count)


# ============================================================
# 38. REVERSE A NUMBER
# ============================================================

number = 12345

value = number
reversed_number = 0

while value > 0:

    digit = value % 10
    reversed_number = (
        reversed_number * 10 + digit
    )

    value //= 10

print("Reversed:", reversed_number)


# ============================================================
# 39. PALINDROME NUMBER
# ============================================================

number = 1221

original = number
value = number
reversed_number = 0

while value > 0:

    digit = value % 10

    reversed_number = (
        reversed_number * 10 + digit
    )

    value //= 10

if original == reversed_number:
    print("Palindrome")
else:
    print("Not palindrome")


# ============================================================
# 40. SUM UNTIL ZERO
# ============================================================
# Uncomment for interactive use.
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
# 41. VALIDATE POSITIVE NUMBER
# ============================================================
# Uncomment for interactive use.
#
# number = int(input("Enter a positive number: "))
#
# while number <= 0:
#     print("Invalid number.")
#     number = int(input("Enter a positive number: "))
#
# print("Valid number:", number)


# ============================================================
# 42. MENU-DRIVEN PROGRAM
# ============================================================
# Example structure for a menu-driven program.
#
# choice = ""
#
# while choice != "4":
#
#     print("1. Add")
#     print("2. View")
#     print("3. Delete")
#     print("4. Exit")
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
#         print("Delete selected")
#
#     elif choice == "4":
#         print("Exiting...")
#
#     else:
#         print("Invalid choice")


# ============================================================
# 43. RETRY LOGIC
# ============================================================

attempt = 1
max_attempts = 3

while attempt <= max_attempts:

    print("Attempt:", attempt)

    attempt += 1


# ============================================================
# 44. RETRY UNTIL SUCCESS
# ============================================================

attempt = 0
success = False

while attempt < 3:

    attempt += 1

    # Simulated result.
    if attempt == 3:
        success = True

    if success:
        print("Operation successful")
        break

    print("Operation failed")


# ============================================================
# 45. WHILE LOOP WITH CONDITION
# ============================================================

temperature = 30

while temperature < 35:

    print(
        "Temperature:",
        temperature
    )

    temperature += 1


# ============================================================
# 46. PROCESS ITEMS UNTIL EMPTY
# ============================================================

tasks = [
    "Learn Python",
    "Practice Loops",
    "Build Project"
]

while tasks:

    task = tasks.pop()

    print("Processing:", task)


# ============================================================
# 47. STACK USING WHILE LOOP
# ============================================================

stack = [
    "First",
    "Second",
    "Third"
]

while stack:

    item = stack.pop()

    print("Popped:", item)


# ============================================================
# 48. QUEUE-LIKE PROCESSING
# ============================================================

queue = [
    "Person 1",
    "Person 2",
    "Person 3"
]

while queue:

    person = queue.pop(0)

    print("Processing:", person)


# ============================================================
# 49. NESTED WHILE LOOP
# ============================================================

row = 1

while row <= 3:

    column = 1

    while column <= 3:

        print(row, column)

        column += 1

    row += 1


# ============================================================
# 50. STAR PATTERN
# ============================================================

row = 1

while row <= 5:

    column = 1

    while column <= row:

        print("*", end=" ")

        column += 1

    print()

    row += 1


# ============================================================
# 51. NUMBER PATTERN
# ============================================================

row = 1

while row <= 5:

    column = 1

    while column <= row:

        print(row, end=" ")

        column += 1

    print()

    row += 1


# ============================================================
# 52. MULTIPLICATION TABLES
# ============================================================

number = 1

while number <= 5:

    multiplier = 1

    while multiplier <= 10:

        print(
            f"{number} x {multiplier} = "
            f"{number * multiplier}"
        )

        multiplier += 1

    print()

    number += 1


# ============================================================
# 53. MATRIX ITERATION
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row = 0

while row < len(matrix):

    column = 0

    while column < len(matrix[row]):

        print(matrix[row][column])

        column += 1

    row += 1


# ============================================================
# 54. PRINT MATRIX
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row = 0

while row < len(matrix):

    column = 0

    while column < len(matrix[row]):

        print(matrix[row][column], end=" ")

        column += 1

    print()

    row += 1


# ============================================================
# 55. SEARCH MATRIX
# ============================================================

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

target = 50

row = 0
found = False

while row < len(matrix):

    column = 0

    while column < len(matrix[row]):

        if matrix[row][column] == target:
            found = True
            break

        column += 1

    if found:
        break

    row += 1

print("Found:", found)


# ============================================================
# 56. GREATEST COMMON DIVISOR
# ============================================================
# Euclidean algorithm using a while loop.


a = 48
b = 18

while b != 0:
    a, b = b, a % b

print("GCD:", a)


# ============================================================
# 57. LEAST COMMON MULTIPLE
# ============================================================

a = 12
b = 18

original_a = a
original_b = b

while b != 0:
    a, b = b, a % b

gcd = a

lcm = abs(
    original_a * original_b
) // gcd

print("LCM:", lcm)


# ============================================================
# 58. PRIME NUMBER CHECK
# ============================================================

number = 29

if number < 2:

    print("Not prime")

else:

    divisor = 2

    while divisor <= int(number ** 0.5):

        if number % divisor == 0:
            print("Not prime")
            break

        divisor += 1

    else:
        print("Prime")


# ============================================================
# 59. ARMSTRONG NUMBER
# ============================================================

number = 153

original = number
digits = len(str(number))

total = 0
value = number

while value > 0:

    digit = value % 10
    total += digit ** digits
    value //= 10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")


# ============================================================
# 60. FIBONACCI SEARCH
# ============================================================

target = 34

first = 0
second = 1

found = False

while first <= target:

    if first == target:
        found = True
        break

    first, second = second, first + second

print("Found:", found)


# ============================================================
# 61. LOOP THROUGH RANGE MANUALLY
# ============================================================

start = 1
stop = 5

while start <= stop:

    print(start)

    start += 1


# ============================================================
# 62. CUSTOM STEP
# ============================================================

number = 0

while number <= 20:

    print(number)

    number += 5


# ============================================================
# 63. NEGATIVE STEP
# ============================================================

number = 20

while number >= 0:

    print(number)

    number -= 5


# ============================================================
# 64. SKIP MULTIPLES OF 3
# ============================================================

number = 0

while number < 20:

    number += 1

    if number % 3 == 0:
        continue

    print(number)


# ============================================================
# 65. PRINT MULTIPLES OF 3
# ============================================================

number = 1

while number <= 30:

    if number % 3 == 0:
        print(number)

    number += 1


# ============================================================
# 66. COUNT NUMBERS DIVISIBLE BY 5
# ============================================================

number = 1
count = 0

while number <= 100:

    if number % 5 == 0:
        count += 1

    number += 1

print("Count:", count)


# ============================================================
# 67. SUM OF EVEN NUMBERS
# ============================================================

number = 2
total = 0

while number <= 100:

    total += number

    number += 2

print("Sum:", total)


# ============================================================
# 68. SUM OF ODD NUMBERS
# ============================================================

number = 1
total = 0

while number <= 100:

    total += number

    number += 2

print("Sum:", total)


# ============================================================
# 69. POWER CALCULATION
# ============================================================

base = 2
exponent = 5

result = 1
count = 0

while count < exponent:

    result *= base

    count += 1

print("Result:", result)


# ============================================================
# 70. MANUAL STRING SEARCH
# ============================================================

text = "Python Programming"
target = "Programming"

index = 0
found = False

while index <= len(text) - len(target):

    if text[index:index + len(target)] == target:
        found = True
        break

    index += 1

print("Found:", found)


# ============================================================
# 71. REVERSE A STRING USING WHILE
# ============================================================

text = "Python"

index = len(text) - 1
reversed_text = ""

while index >= 0:

    reversed_text += text[index]

    index -= 1

print(reversed_text)


# ============================================================
# 72. COUNT CHARACTER OCCURRENCES
# ============================================================

text = "programming"
target = "g"

index = 0
count = 0

while index < len(text):

    if text[index] == target:
        count += 1

    index += 1

print("Occurrences:", count)


# ============================================================
# 73. REMOVE SPACES
# ============================================================

text = "Python Programming Language"

index = 0
result = ""

while index < len(text):

    if text[index] != " ":
        result += text[index]

    index += 1

print(result)


# ============================================================
# 74. INPUT VALIDATION LOOP
# ============================================================
# Uncomment to run interactively.
#
# age = int(input("Enter your age: "))
#
# while age < 0 or age > 120:
#     print("Invalid age.")
#     age = int(input("Enter your age: "))
#
# print("Valid age:", age)


# ============================================================
# 75. MENU LOOP
# ============================================================
# Uncomment to run interactively.
#
# while True:
#
#     print("\n1. Add")
#     print("2. View")
#     print("3. Exit")
#
#     choice = input("Enter choice: ")
#
#     if choice == "1":
#         print("Add selected")
#
#     elif choice == "2":
#         print("View selected")
#
#     elif choice == "3":
#         print("Goodbye!")
#         break
#
#     else:
#         print("Invalid choice")


# ============================================================
# 76. SENTINEL-CONTROLLED LOOP
# ============================================================
# A sentinel is a special value that signals termination.


values = [10, 20, 30, 0]

index = 0
total = 0

while index < len(values):

    value = values[index]

    if value == 0:
        break

    total += value
    index += 1

print("Total:", total)


# ============================================================
# 77. PROCESS UNTIL CONDITION
# ============================================================

number = 1

while number ** 2 < 100:

    print(number)

    number += 1


# ============================================================
# 78. LOGICAL CONDITIONS
# ============================================================

number = 1

while number <= 20 and number % 2 == 1:

    print(number)

    number += 2


# ============================================================
# 79. MULTIPLE CONDITIONS
# ============================================================

number = 1

while number <= 100:

    if number % 3 == 0 and number % 5 == 0:
        print(number)

    number += 1


# ============================================================
# 80. WHILE LOOP WITH FUNCTION
# ============================================================

def square(number):
    return number ** 2


number = 1

while number <= 5:

    print(square(number))

    number += 1


# ============================================================
# 81. PRACTICAL EXAMPLE — SHOPPING CART
# ============================================================

cart = [
    {"name": "Laptop", "price": 50000},
    {"name": "Mouse", "price": 1000},
    {"name": "Keyboard", "price": 2000}
]

index = 0
total = 0

while index < len(cart):

    total += cart[index]["price"]

    index += 1

print("Cart total:", total)


# ============================================================
# 82. PRACTICAL EXAMPLE — STUDENT REPORT
# ============================================================

students = [
    {"name": "Kishor", "marks": 90},
    {"name": "Rahul", "marks": 75},
    {"name": "Amit", "marks": 35}
]

index = 0

while index < len(students):

    student = students[index]

    if student["marks"] >= 40:
        status = "Pass"
    else:
        status = "Fail"

    print(
        student["name"],
        student["marks"],
        status
    )

    index += 1


# ============================================================
# 83. PRACTICAL EXAMPLE — TASK PROCESSING
# ============================================================

tasks = [
    "Learn Python",
    "Practice Loops",
    "Build Project"
]

while tasks:

    task = tasks.pop(0)

    print("Completed:", task)


# ============================================================
# 84. PRACTICAL EXAMPLE — QUEUE PROCESSING
# ============================================================

queue = [
    "Request 1",
    "Request 2",
    "Request 3"
]

while queue:

    request = queue.pop(0)

    print("Processing:", request)


# ============================================================
# 85. PRACTICAL EXAMPLE — RETRY OPERATION
# ============================================================

max_retries = 3
retry = 0

while retry < max_retries:

    retry += 1

    print(
        f"Attempt {retry}"
    )

    if retry == 3:
        print("Success")
        break


# ============================================================
# 86. PRACTICAL EXAMPLE — DOWNLOAD PROGRESS
# ============================================================

progress = 0

while progress < 100:

    progress += 20

    print(
        f"Download progress: {progress}%"
    )


# ============================================================
# 87. PRACTICAL EXAMPLE — BALANCE REDUCTION
# ============================================================

balance = 1000
withdrawal = 100

while balance >= withdrawal:

    balance -= withdrawal

    print(
        "Withdrawal:",
        withdrawal,
        "Balance:",
        balance
    )


# ============================================================
# 88. PRACTICAL EXAMPLE — BATCH PROCESSING
# ============================================================

items = list(range(1, 11))

batch_size = 3

while items:

    batch = items[:batch_size]

    del items[:batch_size]

    print("Processing batch:", batch)


# ============================================================
# 89. PRACTICAL EXAMPLE — PAGINATION
# ============================================================

records = [
    "Record 1",
    "Record 2",
    "Record 3",
    "Record 4",
    "Record 5"
]

page_size = 2
index = 0

while index < len(records):

    page = records[
        index:index + page_size
    ]

    print("Page:", page)

    index += page_size


# ============================================================
# 90. PRACTICAL EXAMPLE — FIND FIRST MATCH
# ============================================================

numbers = [10, 20, 35, 40, 50]

index = 0
target = 35

while index < len(numbers):

    if numbers[index] == target:
        print(
            "First match at:",
            index
        )
        break

    index += 1


# ============================================================
# 91. PRACTICAL EXAMPLE — FIND FIRST EVEN NUMBER
# ============================================================

numbers = [11, 13, 17, 22, 25, 30]

index = 0

while index < len(numbers):

    if numbers[index] % 2 == 0:
        print(
            "First even:",
            numbers[index]
        )
        break

    index += 1


# ============================================================
# 92. PRACTICAL EXAMPLE — REMOVE NEGATIVE VALUES
# ============================================================

numbers = [10, -5, 20, -3, 30]

index = 0

while index < len(numbers):

    if numbers[index] < 0:
        numbers.pop(index)
    else:
        index += 1

print(numbers)


# ============================================================
# 93. PRACTICAL EXAMPLE — CLEAN EMPTY VALUES
# ============================================================

values = [
    "Python",
    "",
    "Java",
    "",
    "C++"
]

index = 0

while index < len(values):

    if values[index] == "":
        values.pop(index)
    else:
        index += 1

print(values)


# ============================================================
# 94. PRACTICAL EXAMPLE — MANUAL LIST COPY
# ============================================================

original = [10, 20, 30, 40]

copy_list = []

index = 0

while index < len(original):

    copy_list.append(original[index])

    index += 1

print(copy_list)


# ============================================================
# 95. PRACTICAL EXAMPLE — MANUAL LIST REVERSE
# ============================================================

numbers = [10, 20, 30, 40]

reversed_numbers = []

index = len(numbers) - 1

while index >= 0:

    reversed_numbers.append(
        numbers[index]
    )

    index -= 1

print(reversed_numbers)


# ============================================================
# 96. COMMON MISTAKE — FORGETTING UPDATE
# ============================================================

"""
Incorrect:

    number = 1

    while number <= 5:
        print(number)

The value of `number` never changes,
so the condition remains True forever.

Correct:

    number = 1

    while number <= 5:
        print(number)
        number += 1
"""


# ============================================================
# 97. COMMON MISTAKE — WRONG CONDITION
# ============================================================

"""
Be careful with the loop condition.

Example:

    number = 10

    while number <= 5:
        print(number)
        number += 1

The loop executes zero times because the condition
is False before the first iteration.
"""


# ============================================================
# 98. COMMON MISTAKE — MODIFYING THE WRONG VARIABLE
# ============================================================

"""
Incorrect:

    count = 1
    number = 10

    while count <= 5:
        print(number)
        number += 1

The condition depends on `count`, but `count` is never updated.

Always make sure the variables controlling the condition
can eventually make the condition False.
"""


# ============================================================
# 99. WHILE VS FOR
# ============================================================

"""
Use a for loop when:

    - You are iterating over a known iterable.
    - You want to process every item.
    - The number of iterations is naturally determined
      by the iterable.

Example:

    for number in numbers:
        print(number)


Use a while loop when:

    - Repetition depends on a condition.
    - The number of iterations is not known beforehand.
    - You need a sentinel-controlled loop.
    - You are implementing retry or validation logic.

Example:

    while condition:
        ...
"""


# ============================================================
# 100. PROFESSIONAL NOTES
# ============================================================

"""
PROFESSIONAL NOTES
------------------

1. A while loop executes while its condition is True.

2. The condition is checked before every iteration.

3. A while loop may execute zero times if its initial
   condition is False.

4. Always ensure that the loop can eventually terminate.

5. Update the variables that control the condition.

6. Use break for an immediate exit.

7. Use continue to skip the current iteration.

8. Use pass as a placeholder.

9. A while-else block executes else when the loop finishes
   without break.

10. while True with break is useful for event-driven,
    menu-driven, and input-controlled loops.

11. Be careful with infinite loops.

12. Use while loops for:
        - input validation
        - retry logic
        - countdowns
        - sentinel-controlled processing
        - queues/stacks
        - condition-based repetition

13. Use a for loop when direct iteration over an iterable
    provides clearer code.

14. Avoid unnecessarily complicated while loops.

15. Keep loop termination conditions explicit and readable.
"""


# ============================================================
# END OF WHILE LOOP
# ============================================================

print("\nWhile loop demonstration completed successfully!")
