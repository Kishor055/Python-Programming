"""
04-Loops/05_continue.py
=======================

Python continue Statement

The `continue` statement skips the remaining code in the
current loop iteration and moves directly to the next iteration.

Syntax:

    for item in iterable:
        if condition:
            continue

    while condition:
        if condition:
            continue

Key difference:

    break
        -> Stops the loop completely.

    continue
        -> Skips only the current iteration.

    pass
        -> Does nothing.
"""


# ============================================================
# 1. BASIC CONTINUE
# ============================================================

for number in range(1, 6):

    if number == 3:
        continue

    print(number)


# ============================================================
# 2. SKIP EVEN NUMBERS
# ============================================================

for number in range(1, 11):

    if number % 2 == 0:
        continue

    print(number)


# ============================================================
# 3. SKIP ODD NUMBERS
# ============================================================

for number in range(1, 11):

    if number % 2 != 0:
        continue

    print(number)


# ============================================================
# 4. PRINT ONLY POSITIVE NUMBERS
# ============================================================

numbers = [10, -5, 20, -10, 30, -2]

for number in numbers:

    if number < 0:
        continue

    print(number)


# ============================================================
# 5. SKIP ZERO
# ============================================================

numbers = [10, 0, 20, 0, 30]

for number in numbers:

    if number == 0:
        continue

    print(number)


# ============================================================
# 6. SKIP NEGATIVE NUMBERS
# ============================================================

numbers = [10, -20, 30, -40, 50]

for number in numbers:

    if number < 0:
        continue

    print("Positive:", number)


# ============================================================
# 7. SKIP NUMBERS GREATER THAN 50
# ============================================================

numbers = [10, 20, 60, 30, 80, 40]

for number in numbers:

    if number > 50:
        continue

    print(number)


# ============================================================
# 8. SKIP MULTIPLES OF 3
# ============================================================

for number in range(1, 21):

    if number % 3 == 0:
        continue

    print(number)


# ============================================================
# 9. SKIP MULTIPLES OF 5
# ============================================================

for number in range(1, 21):

    if number % 5 == 0:
        continue

    print(number)


# ============================================================
# 10. SKIP MULTIPLES OF 3 AND 5
# ============================================================

for number in range(1, 31):

    if number % 3 == 0 or number % 5 == 0:
        continue

    print(number)


# ============================================================
# 11. CONTINUE WITH STRINGS
# ============================================================

languages = [
    "Python",
    "Java",
    "C++",
    "JavaScript"
]

for language in languages:

    if language == "Java":
        continue

    print(language)


# ============================================================
# 12. SKIP EMPTY STRINGS
# ============================================================

values = [
    "Python",
    "",
    "Java",
    "",
    "C++"
]

for value in values:

    if value == "":
        continue

    print(value)


# ============================================================
# 13. SKIP WHITESPACE STRINGS
# ============================================================

values = [
    "Python",
    "   ",
    "Java",
    "",
    "C++"
]

for value in values:

    if not value.strip():
        continue

    print(value)


# ============================================================
# 14. SKIP WORDS SHORTER THAN 5 CHARACTERS
# ============================================================

words = [
    "Python",
    "Java",
    "C",
    "Programming",
    "Code"
]

for word in words:

    if len(word) < 5:
        continue

    print(word)


# ============================================================
# 15. SKIP WORDS LONGER THAN 5 CHARACTERS
# ============================================================

words = [
    "Python",
    "Java",
    "Code",
    "Programming",
    "Hello"
]

for word in words:

    if len(word) > 5:
        continue

    print(word)


# ============================================================
# 16. SKIP NON-ALPHANUMERIC VALUES
# ============================================================

values = [
    "Python",
    "123",
    "Python123",
    "Hello!"
]

for value in values:

    if not value.isalnum():
        continue

    print(value)


# ============================================================
# 17. SKIP NON-NUMERIC STRINGS
# ============================================================

values = [
    "10",
    "Python",
    "20",
    "Java",
    "30"
]

for value in values:

    if not value.isdigit():
        continue

    print(value)


# ============================================================
# 18. SKIP UPPERCASE WORDS
# ============================================================

words = [
    "python",
    "JAVA",
    "hello",
    "WORLD"
]

for word in words:

    if word.isupper():
        continue

    print(word)


# ============================================================
# 19. SKIP LOWERCASE WORDS
# ============================================================

words = [
    "python",
    "JAVA",
    "hello",
    "WORLD"
]

for word in words:

    if word.islower():
        continue

    print(word)


# ============================================================
# 20. SKIP WORDS STARTING WITH "P"
# ============================================================

words = [
    "Python",
    "Java",
    "Programming",
    "C++",
    "Perl"
]

for word in words:

    if word.startswith("P"):
        continue

    print(word)


# ============================================================
# 21. SKIP WORDS ENDING WITH "ING"
# ============================================================

words = [
    "Python",
    "Programming",
    "Coding",
    "Java",
    "Testing"
]

for word in words:

    if word.endswith("ing"):
        continue

    print(word)


# ============================================================
# 22. CONTINUE WITH ENUMERATE
# ============================================================

names = [
    "Amit",
    "Rahul",
    "Kishor",
    "Rohit"
]

for index, name in enumerate(names):

    if index == 2:
        continue

    print(index, name)


# ============================================================
# 23. SKIP SPECIFIC INDEX
# ============================================================

numbers = [10, 20, 30, 40, 50]

for index in range(len(numbers)):

    if index == 2:
        continue

    print(numbers[index])


# ============================================================
# 24. CONTINUE WITH DICTIONARY
# ============================================================

students = {
    "Amit": 75,
    "Rahul": 35,
    "Kishor": 90,
    "Rohit": 30
}

for name, marks in students.items():

    if marks < 40:
        continue

    print(name, marks)


# ============================================================
# 25. SKIP FAILING STUDENTS
# ============================================================

students = [
    {"name": "Amit", "marks": 75},
    {"name": "Rahul", "marks": 35},
    {"name": "Kishor", "marks": 90},
    {"name": "Rohit", "marks": 30}
]

for student in students:

    if student["marks"] < 40:
        continue

    print(
        student["name"],
        "Passed"
    )


# ============================================================
# 26. SKIP OUT-OF-STOCK PRODUCTS
# ============================================================

products = [
    {"name": "Laptop", "stock": 5},
    {"name": "Mouse", "stock": 0},
    {"name": "Keyboard", "stock": 10},
    {"name": "Monitor", "stock": 0}
]

for product in products:

    if product["stock"] == 0:
        continue

    print(
        "Available:",
        product["name"]
    )


# ============================================================
# 27. SKIP INACTIVE USERS
# ============================================================

users = [
    {"name": "Amit", "active": True},
    {"name": "Rahul", "active": False},
    {"name": "Kishor", "active": True}
]

for user in users:

    if not user["active"]:
        continue

    print(
        "Active user:",
        user["name"]
    )


# ============================================================
# 28. SKIP INVALID RECORDS
# ============================================================

records = [
    {"name": "A", "age": 25},
    {"name": "", "age": 30},
    {"name": "C", "age": -5},
    {"name": "D", "age": 40}
]

for record in records:

    if not record["name"]:
        continue

    if record["age"] < 0:
        continue

    print(record)


# ============================================================
# 29. MULTIPLE CONTINUE CONDITIONS
# ============================================================

numbers = range(1, 21)

for number in numbers:

    if number % 2 == 0:
        continue

    if number % 3 == 0:
        continue

    print(number)


# ============================================================
# 30. CONTINUE WITH AND CONDITION
# ============================================================

numbers = range(1, 31)

for number in numbers:

    if number % 2 == 0 and number % 3 == 0:
        continue

    print(number)


# ============================================================
# 31. CONTINUE WITH OR CONDITION
# ============================================================

numbers = range(1, 31)

for number in numbers:

    if number % 2 == 0 or number % 5 == 0:
        continue

    print(number)


# ============================================================
# 32. SKIP NUMBERS IN A RANGE
# ============================================================

for number in range(1, 21):

    if 5 <= number <= 10:
        continue

    print(number)


# ============================================================
# 33. SKIP OUTSIDE A RANGE
# ============================================================

for number in range(1, 21):

    if number < 5 or number > 10:
        continue

    print(number)


# ============================================================
# 34. CONTINUE WITH NESTED LOOP
# ============================================================

for row in range(1, 4):

    for column in range(1, 6):

        if column == 3:
            continue

        print(row, column)


# ============================================================
# 35. CONTINUE AFFECTS ONLY THE INNER LOOP
# ============================================================

for row in range(1, 4):

    print("Row:", row)

    for column in range(1, 5):

        if column == 2:
            continue

        print("Column:", column)


# ============================================================
# 36. SKIP EVEN COLUMNS
# ============================================================

for row in range(1, 4):

    for column in range(1, 6):

        if column % 2 == 0:
            continue

        print(
            "Row:",
            row,
            "Column:",
            column
        )


# ============================================================
# 37. SKIP DIAGONAL ELEMENTS
# ============================================================

for row in range(5):

    for column in range(5):

        if row == column:
            continue

        print(row, column)


# ============================================================
# 38. SKIP MATRIX VALUES
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:

    for value in row:

        if value == 5:
            continue

        print(value)


# ============================================================
# 39. SKIP ZERO VALUES IN MATRIX
# ============================================================

matrix = [
    [1, 0, 3],
    [0, 5, 6],
    [7, 8, 0]
]

for row in matrix:

    for value in row:

        if value == 0:
            continue

        print(value)


# ============================================================
# 40. CONTINUE IN WHILE LOOP
# ============================================================

number = 0

while number < 10:

    number += 1

    if number == 5:
        continue

    print(number)


# ============================================================
# 41. IMPORTANT: UPDATE BEFORE CONTINUE
# ============================================================
# In a while loop, make sure the loop-control variable
# is updated before `continue`.
#
# Otherwise, the condition may never become false.


number = 0

while number < 10:

    number += 1

    if number % 2 == 0:
        continue

    print(number)


# ============================================================
# 42. SKIP EVEN NUMBERS IN WHILE LOOP
# ============================================================

number = 0

while number < 10:

    number += 1

    if number % 2 == 0:
        continue

    print(number)


# ============================================================
# 43. SKIP NEGATIVE VALUES IN WHILE LOOP
# ============================================================

numbers = [-10, -5, 10, 20, 30]

index = 0

while index < len(numbers):

    number = numbers[index]

    index += 1

    if number < 0:
        continue

    print(number)


# ============================================================
# 44. SKIP ZERO IN WHILE LOOP
# ============================================================

numbers = [10, 0, 20, 0, 30]

index = 0

while index < len(numbers):

    number = numbers[index]

    index += 1

    if number == 0:
        continue

    print(number)


# ============================================================
# 45. CONTINUE WITH USER INPUT
# ============================================================
# Uncomment to run interactively.
#
# while True:
#
#     value = input("Enter value: ")
#
#     if value == "":
#         continue
#
#     print("You entered:", value)


# ============================================================
# 46. SKIP INVALID INPUT
# ============================================================
# Uncomment to run interactively.
#
# values = ["10", "20", "abc", "30"]
#
# for value in values:
#
#     if not value.isdigit():
#         continue
#
#     number = int(value)
#     print(number)


# ============================================================
# 47. SKIP INVALID AGES
# ============================================================

ages = [20, -5, 30, 150, 25]

for age in ages:

    if age < 0 or age > 120:
        continue

    print("Valid age:", age)


# ============================================================
# 48. SKIP INVALID SCORES
# ============================================================

scores = [90, 75, -10, 110, 85]

for score in scores:

    if score < 0 or score > 100:
        continue

    print("Valid score:", score)


# ============================================================
# 49. SKIP EMPTY DATA
# ============================================================

data = [
    "Python",
    "",
    "Programming",
    "",
    "Language"
]

for item in data:

    if not item:
        continue

    print(item)


# ============================================================
# 50. SKIP NULL-LIKE VALUES
# ============================================================

data = [
    "Python",
    None,
    "Java",
    None,
    "C++"
]

for item in data:

    if item is None:
        continue

    print(item)


# ============================================================
# 51. SKIP FALSE VALUES
# ============================================================

values = [
    True,
    False,
    True,
    False
]

for value in values:

    if not value:
        continue

    print(value)


# ============================================================
# 52. SKIP DUPLICATES
# ============================================================

numbers = [10, 20, 10, 30, 20, 40]

seen = set()

for number in numbers:

    if number in seen:
        continue

    seen.add(number)

    print(number)


# ============================================================
# 53. SKIP DUPLICATE STRINGS
# ============================================================

names = [
    "Amit",
    "Rahul",
    "Amit",
    "Kishor",
    "Rahul"
]

seen = set()

for name in names:

    if name in seen:
        continue

    seen.add(name)

    print(name)


# ============================================================
# 54. FILTER USING CONTINUE
# ============================================================

numbers = range(1, 21)

for number in numbers:

    if number % 2 != 0:
        continue

    print(number)


# ============================================================
# 55. FILTER POSITIVE EVEN NUMBERS
# ============================================================

numbers = [
    -10,
    -5,
    0,
    2,
    4,
    -8,
    6
]

for number in numbers:

    if number <= 0:
        continue

    if number % 2 != 0:
        continue

    print(number)


# ============================================================
# 56. FILTER WORDS
# ============================================================

words = [
    "Python",
    "Java",
    "Programming",
    "C++",
    "Code"
]

for word in words:

    if len(word) < 5:
        continue

    print(word)


# ============================================================
# 57. FILTER EMAIL-LIKE VALUES
# ============================================================

emails = [
    "user@example.com",
    "invalid",
    "admin@test.com",
    "hello"
]

for email in emails:

    if "@" not in email:
        continue

    print("Valid:", email)


# ============================================================
# 58. FILTER URLs
# ============================================================

urls = [
    "https://example.com",
    "hello",
    "https://python.org",
    "invalid"
]

for url in urls:

    if not url.startswith("https://"):
        continue

    print(url)


# ============================================================
# 59. FILTER FILE EXTENSIONS
# ============================================================

files = [
    "main.py",
    "index.html",
    "app.py",
    "style.css"
]

for file in files:

    if not file.endswith(".py"):
        continue

    print("Python file:", file)


# ============================================================
# 60. SKIP COMMENT LINES
# ============================================================

lines = [
    "print('Hello')",
    "# This is a comment",
    "x = 10",
    "# Another comment"
]

for line in lines:

    if line.startswith("#"):
        continue

    print(line)


# ============================================================
# 61. SKIP BLANK LINES
# ============================================================

lines = [
    "Python",
    "",
    "Programming",
    "",
    "Language"
]

for line in lines:

    if not line.strip():
        continue

    print(line)


# ============================================================
# 62. PROCESS ONLY VALID RECORDS
# ============================================================

records = [
    {"name": "Amit", "valid": True},
    {"name": "Rahul", "valid": False},
    {"name": "Kishor", "valid": True}
]

for record in records:

    if not record["valid"]:
        continue

    print(record["name"])


# ============================================================
# 63. PROCESS ONLY ACTIVE ACCOUNTS
# ============================================================

accounts = [
    {"username": "amit", "active": True},
    {"username": "rahul", "active": False},
    {"username": "kishor", "active": True}
]

for account in accounts:

    if not account["active"]:
        continue

    print(
        "Processing:",
        account["username"]
    )


# ============================================================
# 64. SKIP FAILED TRANSACTIONS
# ============================================================

transactions = [
    {"id": 1, "status": "success"},
    {"id": 2, "status": "failed"},
    {"id": 3, "status": "success"}
]

for transaction in transactions:

    if transaction["status"] == "failed":
        continue

    print(
        "Processing transaction:",
        transaction["id"]
    )


# ============================================================
# 65. SKIP UNSUPPORTED FILES
# ============================================================

files = [
    "app.py",
    "image.png",
    "main.py",
    "data.csv"
]

supported = [".py"]

for file in files:

    if not any(
        file.endswith(extension)
        for extension in supported
    ):
        continue

    print("Processing:", file)


# ============================================================
# 66. CONTINUE WITH EXCEPTION HANDLING
# ============================================================

values = [
    "10",
    "20",
    "abc",
    "30"
]

for value in values:

    try:
        number = int(value)

    except ValueError:
        continue

    print(number)


# ============================================================
# 67. SKIP INVALID NUMERIC DATA
# ============================================================

values = [
    "100",
    "200",
    "Python",
    "300"
]

for value in values:

    try:
        number = float(value)

    except ValueError:
        continue

    print(number)


# ============================================================
# 68. CONTINUE WITH DICTIONARY ITEMS
# ============================================================

prices = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1000
}

for product, price in prices.items():

    if price < 1000:
        continue

    print(product, price)


# ============================================================
# 69. SKIP CHEAP PRODUCTS
# ============================================================

products = [
    {"name": "Mouse", "price": 500},
    {"name": "Keyboard", "price": 1200},
    {"name": "Monitor", "price": 10000}
]

for product in products:

    if product["price"] < 1000:
        continue

    print(product)


# ============================================================
# 70. SKIP EXPENSIVE PRODUCTS
# ============================================================

products = [
    {"name": "Mouse", "price": 500},
    {"name": "Keyboard", "price": 1200},
    {"name": "Monitor", "price": 10000}
]

for product in products:

    if product["price"] > 2000:
        continue

    print(product)


# ============================================================
# 71. CONTINUE IN PRIME NUMBER CHECK
# ============================================================

for number in range(2, 21):

    is_prime = True

    for divisor in range(2, number):

        if number % divisor == 0:
            is_prime = False
            break

    if not is_prime:
        continue

    print("Prime:", number)


# ============================================================
# 72. SKIP NON-PRIME NUMBERS
# ============================================================

numbers = range(2, 20)

for number in numbers:

    if number < 2:
        continue

    for divisor in range(2, number):

        if number % divisor == 0:
            break

    else:
        print("Prime:", number)


# ============================================================
# 73. CONTINUE WITH FACTORS
# ============================================================

number = 30

for divisor in range(1, number + 1):

    if number % divisor != 0:
        continue

    print("Factor:", divisor)


# ============================================================
# 74. SKIP NON-VOWELS
# ============================================================

text = "Python Programming"

for character in text:

    if character.lower() not in "aeiou":
        continue

    print(character)


# ============================================================
# 75. SKIP VOWELS
# ============================================================

text = "Python Programming"

for character in text:

    if character.lower() in "aeiou":
        continue

    print(character)


# ============================================================
# 76. SKIP SPACES
# ============================================================

text = "Python Programming Language"

for character in text:

    if character == " ":
        continue

    print(character)


# ============================================================
# 77. SKIP DIGITS
# ============================================================

text = "Python123"

for character in text:

    if character.isdigit():
        continue

    print(character)


# ============================================================
# 78. SKIP NON-DIGITS
# ============================================================

text = "Python123"

for character in text:

    if not character.isdigit():
        continue

    print(character)


# ============================================================
# 79. SKIP SPECIAL CHARACTERS
# ============================================================

text = "Python@123!"

for character in text:

    if not character.isalnum():
        continue

    print(character)


# ============================================================
# 80. SKIP LOWERCASE CHARACTERS
# ============================================================

text = "PyThOn"

for character in text:

    if character.islower():
        continue

    print(character)


# ============================================================
# 81. SKIP UPPERCASE CHARACTERS
# ============================================================

text = "PyThOn"

for character in text:

    if character.isupper():
        continue

    print(character)


# ============================================================
# 82. CONTINUE WITH RANGE STEP
# ============================================================

for number in range(1, 21, 2):

    if number == 9:
        continue

    print(number)


# ============================================================
# 83. CONTINUE WITH REVERSED RANGE
# ============================================================

for number in range(10, 0, -1):

    if number == 5:
        continue

    print(number)


# ============================================================
# 84. CONTINUE WITH ZIP
# ============================================================

names = ["Amit", "Rahul", "Kishor"]
marks = [75, 35, 90]

for name, mark in zip(names, marks):

    if mark < 40:
        continue

    print(name, mark)


# ============================================================
# 85. CONTINUE WITH ENUMERATE
# ============================================================

languages = [
    "Python",
    "Java",
    "C++",
    "JavaScript"
]

for index, language in enumerate(languages):

    if index % 2 == 0:
        continue

    print(index, language)


# ============================================================
# 86. SKIP EVERY THIRD ITEM
# ============================================================

for index, value in enumerate(range(1, 11), start=1):

    if index % 3 == 0:
        continue

    print(value)


# ============================================================
# 87. CONTINUE AND ELSE
# ============================================================

for number in range(1, 6):

    if number == 3:
        continue

    print(number)

else:
    print("Loop completed")


# `continue` does not prevent the loop's `else` block
# from executing because `continue` does not terminate
# the loop.


# ============================================================
# 88. CONTINUE VS BREAK
# ============================================================

numbers = range(1, 6)

for number in numbers:

    if number == 3:
        continue

    print(number)

# Output:
# 1
# 2
# 4
# 5


for number in numbers:

    if number == 3:
        break

    print(number)

# Output:
# 1
# 2


# ============================================================
# 89. CONTINUE VS PASS
# ============================================================

for number in range(1, 6):

    if number == 3:
        continue

    print(number)


for number in range(1, 6):

    if number == 3:
        pass

    print(number)

# `continue` skips the remaining loop body.
# `pass` skips no execution; it simply does nothing.


# ============================================================
# 90. COMMON MISTAKE IN WHILE LOOP
# ============================================================

"""
Incorrect:

    number = 0

    while number < 10:

        if number == 5:
            continue

        number += 1

This can create an infinite loop because when number becomes
5, `continue` executes before `number += 1`.

Correct:

    number = 0

    while number < 10:

        number += 1

        if number == 5:
            continue

        print(number)
"""


# ============================================================
# 91. SAFE WHILE LOOP WITH CONTINUE
# ============================================================

number = 0

while number < 10:

    number += 1

    if number % 2 == 0:
        continue

    print(number)


# ============================================================
# 92. SKIP CURRENT ITERATION
# ============================================================

for number in range(1, 6):

    print("Before:", number)

    if number == 3:
        continue

    print("After:", number)


# ============================================================
# 93. CONTINUE SKIPS REMAINING LOOP BODY
# ============================================================

for number in range(1, 6):

    if number == 3:
        continue

    print("Statement 1:", number)
    print("Statement 2:", number)
    print("Statement 3:", number)


# ============================================================
# 94. CONTINUE WITH BUSINESS RULE
# ============================================================

orders = [
    {"id": 1, "status": "paid"},
    {"id": 2, "status": "cancelled"},
    {"id": 3, "status": "paid"}
]

for order in orders:

    if order["status"] == "cancelled":
        continue

    print(
        "Processing order:",
        order["id"]
    )


# ============================================================
# 95. CONTINUE WITH AGE RESTRICTION
# ============================================================

users = [
    {"name": "Amit", "age": 25},
    {"name": "Rahul", "age": 16},
    {"name": "Kishor", "age": 30}
]

for user in users:

    if user["age"] < 18:
        continue

    print(
        "Eligible:",
        user["name"]
    )


# ============================================================
# 96. CONTINUE WITH ROLE FILTER
# ============================================================

users = [
    {"name": "Amit", "role": "admin"},
    {"name": "Rahul", "role": "user"},
    {"name": "Kishor", "role": "admin"}
]

for user in users:

    if user["role"] != "admin":
        continue

    print(
        "Admin:",
        user["name"]
    )


# ============================================================
# 97. CONTINUE WITH STATUS FILTER
# ============================================================

tasks = [
    {"id": 1, "status": "completed"},
    {"id": 2, "status": "pending"},
    {"id": 3, "status": "completed"}
]

for task in tasks:

    if task["status"] != "pending":
        continue

    print(
        "Pending task:",
        task["id"]
    )


# ============================================================
# 98. CONTINUE WITH SCORE FILTER
# ============================================================

scores = [35, 50, 75, 20, 90]

for score in scores:

    if score < 50:
        continue

    print("Qualified score:", score)


# ============================================================
# 99. CONTINUE WITH TEMPERATURE FILTER
# ============================================================

temperatures = [20, -5, 30, 45, 25]

for temperature in temperatures:

    if temperature < 0:
        continue

    print(
        "Valid temperature:",
        temperature
    )


# ============================================================
# 100. PROFESSIONAL FILTERING PATTERN
# ============================================================

records = [
    {"name": "Amit", "active": True, "score": 80},
    {"name": "Rahul", "active": False, "score": 90},
    {"name": "Kishor", "active": True, "score": 45},
    {"name": "Rohit", "active": True, "score": 95}
]

for record in records:

    # Skip inactive records.
    if not record["active"]:
        continue

    # Skip records below the required score.
    if record["score"] < 50:
        continue

    print(
        "Qualified:",
        record["name"]
    )


# ============================================================
# 101. CONTINUE IN DATA PROCESSING
# ============================================================

data = [
    "10",
    "20",
    "",
    "30",
    "invalid",
    "40"
]

total = 0

for value in data:

    if not value:
        continue

    if not value.isdigit():
        continue

    total += int(value)

print("Total:", total)


# ============================================================
# 102. CONTINUE IN VALIDATION
# ============================================================

records = [
    {"name": "Amit", "age": 25},
    {"name": "", "age": 30},
    {"name": "Rahul", "age": -1},
    {"name": "Kishor", "age": 28}
]

for record in records:

    if not record["name"]:
        continue

    if record["age"] < 0:
        continue

    print(
        "Valid record:",
        record
    )


# ============================================================
# 103. CONTINUE WITH MULTIPLE VALIDATION RULES
# ============================================================

numbers = [
    10,
    -20,
    25,
    0,
    30,
    101
]

for number in numbers:

    if number <= 0:
        continue

    if number > 100:
        continue

    if number % 5 != 0:
        continue

    print(
        "Valid number:",
        number
    )


# ============================================================
# 104. CONTINUE IN NESTED LOOPS
# ============================================================

for row in range(1, 4):

    for column in range(1, 6):

        if row == 2:
            continue

        if column == 3:
            continue

        print(row, column)


# ============================================================
# 105. CONTINUE WITH PATTERN GENERATION
# ============================================================

for row in range(1, 6):

    for column in range(1, 6):

        if row == column:
            continue

        print("*", end=" ")

    print()


# ============================================================
# 106. CONTINUE WITH MULTIPLICATION TABLE
# ============================================================

number = 5

for multiplier in range(1, 11):

    if multiplier == 5:
        continue

    print(
        number,
        "x",
        multiplier,
        "=",
        number * multiplier
    )


# ============================================================
# 107. CONTINUE WITH FIZZBUZZ FILTER
# ============================================================

for number in range(1, 31):

    if number % 3 == 0 or number % 5 == 0:
        continue

    print(number)


# ============================================================
# 108. CONTINUE TO IGNORE RESERVED VALUES
# ============================================================

values = [10, 20, -1, 30, -1, 40]

for value in values:

    if value == -1:
        continue

    print(value)


# ============================================================
# 109. CONTINUE WITH SENTINEL-LIKE VALUE
# ============================================================

values = [10, 20, 0, 30, 40]

for value in values:

    if value == 0:
        continue

    print(value)


# Unlike `break`, the sentinel does not stop processing.
# It only skips that particular value.


# ============================================================
# 110. CONTINUE WITH CALCULATION
# ============================================================

numbers = range(1, 11)

for number in numbers:

    if number == 5:
        continue

    square = number ** 2

    print(
        number,
        "=>",
        square
    )


# ============================================================
# 111. CONTINUE WITH FUNCTION RESULT
# ============================================================

def is_valid(number):
    return number > 0


numbers = [10, -5, 20, -2, 30]

for number in numbers:

    if not is_valid(number):
        continue

    print(number)


# ============================================================
# 112. CONTINUE WITH CUSTOM CONDITION
# ============================================================

def is_even(number):
    return number % 2 == 0


for number in range(1, 11):

    if not is_even(number):
        continue

    print(number)


# ============================================================
# 113. CONTINUE WITH LIST OF FUNCTIONS
# ============================================================

numbers = [10, -2, 20, 0, 30]

for number in numbers:

    if number <= 0:
        continue

    print(
        "Square:",
        number ** 2
    )


# ============================================================
# 114. CONTINUE WITH FILE EXTENSIONS
# ============================================================

files = [
    "main.py",
    "app.js",
    "test.py",
    "style.css",
    "server.py"
]

for file in files:

    if not file.endswith(".py"):
        continue

    print(
        "Python source:",
        file
    )


# ============================================================
# 115. CONTINUE WITH LOG LEVEL
# ============================================================

logs = [
    {"level": "INFO", "message": "Started"},
    {"level": "DEBUG", "message": "Value = 10"},
    {"level": "ERROR", "message": "Failed"},
    {"level": "INFO", "message": "Completed"}
]

for log in logs:

    if log["level"] != "ERROR":
        continue

    print(
        log["level"],
        log["message"]
    )


# ============================================================
# 116. CONTINUE WITH HTTP STATUS
# ============================================================

responses = [
    {"status": 200},
    {"status": 404},
    {"status": 201},
    {"status": 500}
]

for response in responses:

    if response["status"] >= 400:
        continue

    print(
        "Successful response:",
        response["status"]
    )


# ============================================================
# 117. CONTINUE WITH INVENTORY
# ============================================================

inventory = [
    {"name": "Laptop", "quantity": 10},
    {"name": "Mouse", "quantity": 0},
    {"name": "Keyboard", "quantity": 5}
]

for item in inventory:

    if item["quantity"] <= 0:
        continue

    print(
        item["name"],
        item["quantity"]
    )


# ============================================================
# 118. CONTINUE WITH PRICE RANGE
# ============================================================

prices = [
    500,
    1500,
    2500,
    5000
]

for price in prices:

    if price < 1000:
        continue

    if price > 3000:
        continue

    print(
        "Accepted price:",
        price
    )


# ============================================================
# 119. CONTINUE WITH DATE-LIKE DATA
# ============================================================

years = [1999, 2000, 2020, 2024, 2030]

for year in years:

    if year < 2000:
        continue

    if year > 2026:
        continue

    print(
        "Year:",
        year
    )


# ============================================================
# 120. FINAL SUMMARY
# ============================================================

"""
CONTINUE STATEMENT — FINAL SUMMARY
==================================

`continue` skips the remaining statements in the current
iteration and starts the next iteration of the loop.

Syntax:

    for item in iterable:

        if condition:
            continue

    while condition:

        if condition:
            continue


BREAK
-----
Stops the entire nearest loop.

CONTINUE
--------
Skips only the current iteration.

PASS
----
Does nothing.


Example:

    for number in range(1, 6):

        if number == 3:
            continue

        print(number)

Output:

    1
    2
    4
    5


Important points:

1. `continue` does not terminate the loop.

2. `continue` works with both `for` and `while` loops.

3. In nested loops, `continue` affects only the nearest loop.

4. `continue` is useful for filtering unwanted values.

5. `continue` is useful for validation.

6. `continue` can make deeply nested conditions easier to read.

7. In a `while` loop, update the loop variable before
   executing `continue` when necessary.

8. `continue` does not prevent a loop's `else` block from
   executing.

9. Use `break` when you want to stop.
   
10. Use `continue` when you want to skip and keep going.

Core mental model:

    break
        STOP

    continue
        SKIP THIS ITERATION

    pass
        DO NOTHING
"""


# ============================================================
# END OF CONTINUE
# ============================================================

print("\nContinue statement demonstration completed successfully!")
