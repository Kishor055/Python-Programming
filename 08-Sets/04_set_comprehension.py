"""
04_set_comprehension.py
-----------------------
Python Set Comprehension.

Set comprehension provides a concise way to create sets
from iterables using a single expression.

Topics covered:
    1. Basic set comprehension
    2. Set comprehension with expressions
    3. Set comprehension with conditions
    4. if-else with set comprehension
    5. Working with strings
    6. Removing duplicates
    7. Nested loops
    8. Practical examples
    9. Set comprehension vs traditional loop
"""


# ============================================================
# 1. Basic Set Comprehension
# ============================================================
# Syntax:
#
#     {expression for item in iterable}
#
# Example:
#     Create a set containing numbers from 1 to 5.

numbers = {number for number in range(1, 6)}

print("Numbers:", numbers)


# ============================================================
# 2. Set Comprehension with an Expression
# ============================================================
# We can transform each item while creating the set.

numbers = {1, 2, 3, 4, 5}

squares = {number ** 2 for number in numbers}

print("\nOriginal numbers:", numbers)
print("Squares:", squares)


# Another example

numbers = {1, 2, 3, 4, 5}

doubled = {number * 2 for number in numbers}

print("Doubled:", doubled)


# ============================================================
# 3. Set Comprehension with a Condition
# ============================================================
# Syntax:
#
#     {expression for item in iterable if condition}
#
# Example:
#     Create a set containing only even numbers.

numbers = range(1, 11)

even_numbers = {
    number
    for number in numbers
    if number % 2 == 0
}

print("\nEven numbers:", even_numbers)


# Odd numbers

odd_numbers = {
    number
    for number in numbers
    if number % 2 != 0
}

print("Odd numbers:", odd_numbers)


# ============================================================
# 4. Set Comprehension with Transformation + Condition
# ============================================================
# Create squares only for even numbers.

numbers = range(1, 11)

even_squares = {
    number ** 2
    for number in numbers
    if number % 2 == 0
}

print("\nEven squares:", even_squares)


# ============================================================
# 5. Set Comprehension with if-else
# ============================================================
# Syntax:
#
#     {value_if_true if condition else value_if_false
#      for item in iterable}
#
# Example:

numbers = range(1, 6)

result = {
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
}

print("\nEven/Odd labels:", result)


# IMPORTANT:
# Because this is a SET, duplicate results are automatically
# removed.
#
# The expression above can produce:
#
#     "Odd"
#     "Even"
#     "Odd"
#     "Even"
#     "Odd"
#
# But the final set contains only:
#
#     {"Odd", "Even"}


# ============================================================
# 6. Set Comprehension with Strings
# ============================================================
# Create a set containing unique characters.

text = "programming"

unique_characters = {
    character
    for character in text
}

print("\nText:", text)
print("Unique characters:", unique_characters)


# ============================================================
# 7. Convert Characters to Uppercase
# ============================================================

text = "python"

uppercase_characters = {
    character.upper()
    for character in text
}

print("\nOriginal text:", text)
print("Uppercase characters:", uppercase_characters)


# ============================================================
# 8. Filter Characters
# ============================================================
# Get only vowels from a string.

text = "programming"

vowels = {
    character
    for character in text
    if character in "aeiou"
}

print("\nVowels:", vowels)


# Get only consonants

consonants = {
    character
    for character in text
    if character.isalpha() and character not in "aeiou"
}

print("Consonants:", consonants)


# ============================================================
# 9. Remove Duplicates Using Set Comprehension
# ============================================================

numbers = [10, 20, 20, 30, 30, 40, 40, 50]

unique_numbers = {
    number
    for number in numbers
}

print("\nOriginal list:", numbers)
print("Unique numbers:", unique_numbers)


# ============================================================
# 10. Set Comprehension with Conditions
# ============================================================
# Find numbers greater than 50.

numbers = [10, 25, 50, 60, 75, 90, 100]

greater_than_50 = {
    number
    for number in numbers
    if number > 50
}

print("\nNumbers greater than 50:", greater_than_50)


# ============================================================
# 11. String Length with Set Comprehension
# ============================================================

names = {
    "Alice",
    "Bob",
    "Charlie",
    "David",
}

name_lengths = {
    len(name)
    for name in names
}

print("\nNames:", names)
print("Unique name lengths:", name_lengths)


# Notice:
# Alice  -> 5
# Bob    -> 3
# Charlie -> 7
# David  -> 5
#
# Because this is a set, the duplicate length 5 appears once.


# ============================================================
# 12. Nested Set Comprehension
# ============================================================
# Set comprehension can contain more than one loop.
#
# Example:
# Create all coordinate pairs.

coordinates = {
    (x, y)
    for x in range(1, 4)
    for y in range(1, 4)
}

print("\nCoordinates:", coordinates)


# ============================================================
# 13. Nested Set Comprehension with Condition
# ============================================================
# Find coordinate pairs where x + y is even.

coordinates = {
    (x, y)
    for x in range(1, 4)
    for y in range(1, 4)
    if (x + y) % 2 == 0
}

print("\nCoordinates where x + y is even:")
print(coordinates)


# ============================================================
# 14. Set Comprehension from a Dictionary
# ============================================================
# By default, iterating over a dictionary produces its keys.

student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 92,
}

student_names = {
    name
    for name in student_marks
}

print("\nStudent names:", student_names)


# Get unique marks

unique_marks = {
    marks
    for marks in student_marks.values()
}

print("Unique marks:", unique_marks)


# ============================================================
# 15. Filter Dictionary Data
# ============================================================
# Get names of students who scored 80 or more.

student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 92,
}

top_students = {
    name
    for name, marks in student_marks.items()
    if marks >= 80
}

print("\nStudents scoring 80 or more:", top_students)


# ============================================================
# 16. Practical Example — Unique Skills
# ============================================================

developers = [
    {"Python", "Git", "SQL"},
    {"Python", "Docker", "Git"},
    {"Java", "SQL", "Git"},
]

all_skills = {
    skill
    for developer in developers
    for skill in developer
}

print("\nAll unique skills:", all_skills)


# ============================================================
# 17. Practical Example — Extract Domains
# ============================================================

emails = [
    "alice@gmail.com",
    "bob@yahoo.com",
    "charlie@gmail.com",
    "david@outlook.com",
]

domains = {
    email.split("@")[1]
    for email in emails
}

print("\nEmail domains:", domains)


# ============================================================
# 18. Practical Example — Valid Usernames
# ============================================================
# Get usernames containing at least 5 characters.

usernames = [
    "admin",
    "bob",
    "developer",
    "alex",
    "python",
    "joe",
]

valid_usernames = {
    username
    for username in usernames
    if len(username) >= 5
}

print("\nValid usernames:", valid_usernames)


# ============================================================
# 19. Practical Example — Unique File Extensions
# ============================================================

files = [
    "main.py",
    "app.py",
    "index.html",
    "style.css",
    "script.js",
    "test.py",
]

extensions = {
    file.split(".")[-1]
    for file in files
}

print("\nFile extensions:", extensions)


# ============================================================
# 20. Practical Example — Positive Numbers
# ============================================================

numbers = [-10, -5, 0, 5, 10, 15, -20]

positive_numbers = {
    number
    for number in numbers
    if number > 0
}

print("\nPositive numbers:", positive_numbers)


# ============================================================
# 21. Practical Example — Normalize Data
# ============================================================
# Convert names to lowercase and remove duplicates.

names = [
    "Alice",
    "BOB",
    "alice",
    "Charlie",
    "Bob",
]

normalized_names = {
    name.lower()
    for name in names
}

print("\nOriginal names:", names)
print("Normalized names:", normalized_names)


# ============================================================
# 22. Traditional Loop vs Set Comprehension
# ============================================================

numbers = [1, 2, 3, 4, 5]

# Traditional approach

squares = set()

for number in numbers:
    squares.add(number ** 2)

print("\nTraditional approach:", squares)


# Set comprehension

squares = {
    number ** 2
    for number in numbers
}

print("Set comprehension:", squares)


# ============================================================
# 23. Another Comparison — Filtering
# ============================================================

numbers = range(1, 11)

# Traditional approach

even_numbers = set()

for number in numbers:
    if number % 2 == 0:
        even_numbers.add(number)

print("\nTraditional filtering:", even_numbers)


# Set comprehension

even_numbers = {
    number
    for number in numbers
    if number % 2 == 0
}

print("Set comprehension:", even_numbers)


# ============================================================
# 24. Set Comprehension Syntax Cheat Sheet
# ============================================================
#
# Basic:
#
#     {expression for item in iterable}
#
#
# With condition:
#
#     {expression for item in iterable if condition}
#
#
# With if-else:
#
#     {
#         value_if_true if condition else value_if_false
#         for item in iterable
#     }
#
#
# Nested loops:
#
#     {
#         expression
#         for item1 in iterable1
#         for item2 in iterable2
#     }
#
# ============================================================


# ============================================================
# 25. Important Rules
# ============================================================
#
# 1. Set comprehension creates a SET.
#
# 2. Duplicate values are automatically removed.
#
# 3. The expression determines what gets stored.
#
# 4. "if" can be used to filter values.
#
# 5. if-else can be used inside the expression.
#
# 6. Multiple loops can be used for nested iteration.
#
# 7. Keep comprehensions readable.
#
# 8. Avoid extremely complex comprehensions.
#
# ============================================================


# ============================================================
# 26. When Should You Use Set Comprehension?
# ============================================================
#
# Use set comprehension when:
#
# - You need to transform data into a set.
# - You need unique results.
# - You need to filter values.
# - The logic can be expressed clearly in one statement.
#
# Example:
#
#     even_squares = {
#         number ** 2
#         for number in numbers
#         if number % 2 == 0
#     }
#
# ============================================================


# ============================================================
# Key Takeaways
# ============================================================
#
# Set comprehension provides a concise way to create sets.
#
# Basic syntax:
#
#     {expression for item in iterable}
#
# With filtering:
#
#     {expression for item in iterable if condition}
#
# Remember:
#
#     Set comprehension
#         ↓
#     Transformation
#         +
#     Optional filtering
#         ↓
#     Unique results
#
# The biggest advantage is that the resulting collection
# automatically removes duplicate values.
#
# Next:
# 05_frozenset.py
# ============================================================
