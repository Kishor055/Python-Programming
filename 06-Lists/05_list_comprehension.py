"""
05_list_comprehension.py
========================

Python List Comprehension

List comprehension provides a concise way to create lists.

Basic syntax:

    [expression for item in iterable]

With condition:

    [expression for item in iterable if condition]

With if-else:

    [expression if condition else expression for item in iterable]

List comprehensions are useful for transforming, filtering,
and generating lists in a readable and Pythonic way.
"""


# ============================================================
# 1. BASIC LIST COMPREHENSION
# ============================================================

numbers = [number for number in range(1, 6)]

print(numbers)


# Equivalent for loop:

numbers = []

for number in range(1, 6):
    numbers.append(number)

print(numbers)


# ============================================================
# 2. SQUARE NUMBERS
# ============================================================

squares = [number ** 2 for number in range(1, 6)]

print(squares)


# Equivalent for loop:

squares = []

for number in range(1, 6):
    squares.append(number ** 2)

print(squares)


# ============================================================
# 3. CUBE NUMBERS
# ============================================================

cubes = [number ** 3 for number in range(1, 6)]

print(cubes)


# ============================================================
# 4. MULTIPLY EACH ELEMENT
# ============================================================

numbers = [1, 2, 3, 4, 5]

result = [number * 10 for number in numbers]

print(result)


# ============================================================
# 5. ADD VALUE TO EACH ELEMENT
# ============================================================

numbers = [10, 20, 30, 40]

result = [number + 5 for number in numbers]

print(result)


# ============================================================
# 6. CONVERT STRINGS TO UPPERCASE
# ============================================================

languages = ["python", "java", "c++", "javascript"]

result = [language.upper() for language in languages]

print(result)


# ============================================================
# 7. CONVERT STRINGS TO LOWERCASE
# ============================================================

languages = ["Python", "JAVA", "C++", "JavaScript"]

result = [language.lower() for language in languages]

print(result)


# ============================================================
# 8. GET STRING LENGTHS
# ============================================================

languages = ["Python", "Java", "C++", "JavaScript"]

lengths = [len(language) for language in languages]

print(lengths)


# ============================================================
# 9. ABSOLUTE VALUES
# ============================================================

numbers = [-10, -5, 0, 5, 10]

result = [abs(number) for number in numbers]

print(result)


# ============================================================
# 10. FILTER EVEN NUMBERS
# ============================================================

numbers = range(1, 11)

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)


# ============================================================
# 11. FILTER ODD NUMBERS
# ============================================================

numbers = range(1, 11)

odd_numbers = [
    number
    for number in numbers
    if number % 2 != 0
]

print(odd_numbers)


# ============================================================
# 12. FILTER POSITIVE NUMBERS
# ============================================================

numbers = [-5, 10, -3, 7, 0, 8, -1]

positive_numbers = [
    number
    for number in numbers
    if number > 0
]

print(positive_numbers)


# ============================================================
# 13. FILTER NEGATIVE NUMBERS
# ============================================================

numbers = [-5, 10, -3, 7, 0, 8, -1]

negative_numbers = [
    number
    for number in numbers
    if number < 0
]

print(negative_numbers)


# ============================================================
# 14. FILTER NUMBERS GREATER THAN A VALUE
# ============================================================

numbers = [10, 25, 5, 40, 15, 50]

result = [
    number
    for number in numbers
    if number > 20
]

print(result)


# ============================================================
# 15. FILTER NUMBERS LESS THAN A VALUE
# ============================================================

numbers = [10, 25, 5, 40, 15, 50]

result = [
    number
    for number in numbers
    if number < 20
]

print(result)


# ============================================================
# 16. IF-ELSE IN LIST COMPREHENSION
# ============================================================
# Syntax:
#
# [value_if_true if condition else value_if_false
#  for item in iterable]


numbers = range(1, 11)

result = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]

print(result)


# ============================================================
# 17. EVEN / ODD LABELS
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

result = [
    number * 2 if number % 2 == 0 else number
    for number in numbers
]

print(result)


# ============================================================
# 18. PASS / FAIL
# ============================================================

marks = [35, 80, 42, 25, 90, 60]

result = [
    "Pass" if mark >= 40 else "Fail"
    for mark in marks
]

print(result)


# ============================================================
# 19. GRADE ASSIGNMENT
# ============================================================

marks = [95, 82, 67, 45, 30]

grades = [
    "A" if mark >= 90
    else "B" if mark >= 75
    else "C" if mark >= 60
    else "D" if mark >= 40
    else "F"
    for mark in marks
]

print(grades)


# ============================================================
# 20. STRING FILTERING
# ============================================================

languages = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "Go"
]

result = [
    language
    for language in languages
    if len(language) > 4
]

print(result)


# ============================================================
# 21. FILTER STRINGS STARTING WITH A CHARACTER
# ============================================================

languages = [
    "Python",
    "Java",
    "Perl",
    "C++",
    "PHP"
]

result = [
    language
    for language in languages
    if language.startswith("P")
]

print(result)


# ============================================================
# 22. FILTER STRINGS ENDING WITH A CHARACTER
# ============================================================

languages = [
    "Python",
    "Java",
    "C++",
    "Go"
]

result = [
    language
    for language in languages
    if language.endswith("a")
]

print(result)


# ============================================================
# 23. REMOVE EMPTY STRINGS
# ============================================================

items = ["Python", "", "Java", "", "C++"]

result = [
    item
    for item in items
    if item
]

print(result)


# ============================================================
# 24. STRIP STRINGS
# ============================================================

names = [
    "  Kishor  ",
    " Rahul ",
    "Amit"
]

result = [
    name.strip()
    for name in names
]

print(result)


# ============================================================
# 25. FILTER AND TRANSFORM
# ============================================================

numbers = range(1, 11)

result = [
    number ** 2
    for number in numbers
    if number % 2 == 0
]

print(result)


# ============================================================
# 26. EVEN SQUARES
# ============================================================

numbers = range(1, 11)

even_squares = [
    number ** 2
    for number in numbers
    if number % 2 == 0
]

print(even_squares)


# ============================================================
# 27. ODD CUBES
# ============================================================

numbers = range(1, 11)

odd_cubes = [
    number ** 3
    for number in numbers
    if number % 2 != 0
]

print(odd_cubes)


# ============================================================
# 28. MULTIPLE CONDITIONS
# ============================================================

numbers = range(1, 21)

result = [
    number
    for number in numbers
    if number % 2 == 0
    if number > 10
]

print(result)


# Equivalent using and:

result = [
    number
    for number in numbers
    if number % 2 == 0 and number > 10
]

print(result)


# ============================================================
# 29. MULTIPLE CONDITIONS WITH OR
# ============================================================

numbers = range(1, 21)

result = [
    number
    for number in numbers
    if number % 3 == 0 or number % 5 == 0
]

print(result)


# ============================================================
# 30. LIST COMPREHENSION WITH RANGE STEP
# ============================================================

numbers = [
    number
    for number in range(0, 21, 2)
]

print(numbers)


# ============================================================
# 31. CREATE A LIST OF ZEROS
# ============================================================

zeros = [0 for _ in range(5)]

print(zeros)


# ============================================================
# 32. CREATE A LIST OF REPEATED VALUES
# ============================================================

values = ["Python" for _ in range(5)]

print(values)


# ============================================================
# 33. CREATE MULTIPLICATION TABLE
# ============================================================

number = 5

table = [
    number * multiplier
    for multiplier in range(1, 11)
]

print(table)


# ============================================================
# 34. MULTIPLICATION TABLE WITH FORMATTING
# ============================================================

number = 5

table = [
    f"{number} x {multiplier} = {number * multiplier}"
    for multiplier in range(1, 11)
]

for line in table:
    print(line)


# ============================================================
# 35. NESTED LIST COMPREHENSION
# ============================================================
# A list comprehension can contain another loop.


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [
    value
    for row in matrix
    for value in row
]

print(flattened)


# Equivalent loops:

flattened = []

for row in matrix:
    for value in row:
        flattened.append(value)

print(flattened)


# ============================================================
# 36. FLATTEN A MATRIX
# ============================================================

matrix = [
    [10, 20],
    [30, 40],
    [50, 60]
]

result = [
    value
    for row in matrix
    for value in row
]

print(result)


# ============================================================
# 37. CREATE A MATRIX
# ============================================================

matrix = [
    [0 for _ in range(3)]
    for _ in range(3)
]

print(matrix)


# ============================================================
# 38. CREATE AN IDENTITY MATRIX
# ============================================================

size = 3

matrix = [
    [
        1 if row == column else 0
        for column in range(size)
    ]
    for row in range(size)
]

print(matrix)


# ============================================================
# 39. TRANSPOSE A MATRIX
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = [
    [matrix[row][column] for row in range(len(matrix))]
    for column in range(len(matrix[0]))
]

print(transpose)


# ============================================================
# 40. LIST COMPREHENSION WITH ENUMERATE
# ============================================================

languages = ["Python", "Java", "C++"]

result = [
    f"{index}: {language}"
    for index, language in enumerate(languages)
]

print(result)


# ============================================================
# 41. LIST COMPREHENSION WITH ZIP
# ============================================================

names = ["Kishor", "Rahul", "Amit"]
marks = [90, 85, 95]

result = [
    f"{name}: {mark}"
    for name, mark in zip(names, marks)
]

print(result)


# ============================================================
# 42. CREATE DICTIONARIES USING LIST COMPREHENSION
# ============================================================

names = ["Kishor", "Rahul", "Amit"]

result = [
    {"name": name}
    for name in names
]

print(result)


# ============================================================
# 43. TRANSFORM DICTIONARY DATA
# ============================================================

students = [
    {"name": "Kishor", "marks": 90},
    {"name": "Rahul", "marks": 85},
    {"name": "Amit", "marks": 95}
]

names = [
    student["name"]
    for student in students
]

print(names)


# ============================================================
# 44. FILTER DICTIONARY DATA
# ============================================================

students = [
    {"name": "Kishor", "marks": 90},
    {"name": "Rahul", "marks": 35},
    {"name": "Amit", "marks": 95}
]

passed_students = [
    student
    for student in students
    if student["marks"] >= 40
]

print(passed_students)


# ============================================================
# 45. GET MARKS FROM STUDENTS
# ============================================================

students = [
    {"name": "Kishor", "marks": 90},
    {"name": "Rahul", "marks": 85},
    {"name": "Amit", "marks": 95}
]

marks = [
    student["marks"]
    for student in students
]

print(marks)


# ============================================================
# 46. FILTER AND TRANSFORM DICTIONARY DATA
# ============================================================

students = [
    {"name": "Kishor", "marks": 90},
    {"name": "Rahul", "marks": 35},
    {"name": "Amit", "marks": 95}
]

result = [
    student["name"]
    for student in students
    if student["marks"] >= 40
]

print(result)


# ============================================================
# 47. REMOVE DUPLICATES USING SET
# ============================================================

numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = [
    number
    for number in set(numbers)
]

print(unique_numbers)


# Note:
# Set order should not be relied upon.


# ============================================================
# 48. FILTER DUPLICATES WHILE PRESERVING ORDER
# ============================================================

numbers = [10, 20, 10, 30, 20, 40]

seen = set()

unique_numbers = [
    number
    for number in numbers
    if not (number in seen or seen.add(number))
]

print(unique_numbers)


# ============================================================
# 49. STRING TO CHARACTER LIST
# ============================================================

text = "Python"

characters = [
    character
    for character in text
]

print(characters)


# ============================================================
# 50. FILTER VOWELS
# ============================================================

text = "Python Programming"

vowels = [
    character
    for character in text.lower()
    if character in "aeiou"
]

print(vowels)


# ============================================================
# 51. FILTER CONSONANTS
# ============================================================

text = "Python"

consonants = [
    character
    for character in text.lower()
    if character.isalpha() and character not in "aeiou"
]

print(consonants)


# ============================================================
# 52. GET DIGITS FROM STRING
# ============================================================

text = "Python123Programming456"

digits = [
    character
    for character in text
    if character.isdigit()
]

print(digits)


# ============================================================
# 53. GET ALPHABETIC CHARACTERS
# ============================================================

text = "Python123!"

letters = [
    character
    for character in text
    if character.isalpha()
]

print(letters)


# ============================================================
# 54. FILTER WORDS BY LENGTH
# ============================================================

words = [
    "Python",
    "AI",
    "Programming",
    "Code",
    "Developer"
]

long_words = [
    word
    for word in words
    if len(word) > 4
]

print(long_words)


# ============================================================
# 55. WORDS TO UPPERCASE
# ============================================================

words = ["python", "java", "c++"]

uppercase_words = [
    word.upper()
    for word in words
]

print(uppercase_words)


# ============================================================
# 56. WORDS STARTING WITH A SPECIFIC LETTER
# ============================================================

words = [
    "Python",
    "Programming",
    "Java",
    "PHP",
    "Perl"
]

p_words = [
    word
    for word in words
    if word.lower().startswith("p")
]

print(p_words)


# ============================================================
# 57. LIST COMPREHENSION WITH FUNCTION
# ============================================================

def square(number):
    return number ** 2


numbers = [1, 2, 3, 4, 5]

squares = [
    square(number)
    for number in numbers
]

print(squares)


# ============================================================
# 58. LIST COMPREHENSION WITH BUILT-IN FUNCTION
# ============================================================

numbers = [-10, -20, 30, -40]

absolute_values = [
    abs(number)
    for number in numbers
]

print(absolute_values)


# ============================================================
# 59. LIST COMPREHENSION WITH CONDITIONAL FUNCTION
# ============================================================

def is_even(number):
    return number % 2 == 0


numbers = range(1, 11)

even_numbers = [
    number
    for number in numbers
    if is_even(number)
]

print(even_numbers)


# ============================================================
# 60. LIST COMPREHENSION WITH NESTED CONDITIONS
# ============================================================

numbers = range(1, 31)

result = [
    number
    for number in numbers
    if number % 2 == 0
    and number % 3 == 0
]

print(result)


# ============================================================
# 61. CARTESIAN PRODUCT
# ============================================================

colors = ["Red", "Blue"]
sizes = ["S", "M", "L"]

combinations = [
    (color, size)
    for color in colors
    for size in sizes
]

print(combinations)


# ============================================================
# 62. CARTESIAN PRODUCT WITH CONDITION
# ============================================================

numbers = [1, 2, 3]
letters = ["A", "B", "C"]

combinations = [
    (number, letter)
    for number in numbers
    for letter in letters
    if number != 2
]

print(combinations)


# ============================================================
# 63. MULTIPLE FOR CLAUSES
# ============================================================

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

result = [
    value
    for row in matrix
    for value in row
]

print(result)


# ============================================================
# 64. CONDITIONAL NESTED COMPREHENSION
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

even_values = [
    value
    for row in matrix
    for value in row
    if value % 2 == 0
]

print(even_values)


# ============================================================
# 65. CREATE PAIRS
# ============================================================

numbers = range(1, 6)

pairs = [
    (number, number ** 2)
    for number in numbers
]

print(pairs)


# ============================================================
# 66. CREATE KEY-VALUE PAIRS
# ============================================================

numbers = range(1, 6)

pairs = [
    (number, number ** 2)
    for number in numbers
]

print(pairs)


# ============================================================
# 67. CONVERT PAIRS TO DICTIONARY
# ============================================================

numbers = range(1, 6)

squares = {
    number: number ** 2
    for number in numbers
}

print(squares)


# ============================================================
# 68. LIST COMPREHENSION VS MAP
# ============================================================

numbers = [1, 2, 3, 4, 5]

result = [
    number ** 2
    for number in numbers
]

print(result)


# Equivalent map():

result = list(
    map(lambda number: number ** 2, numbers)
)

print(result)


# ============================================================
# 69. LIST COMPREHENSION VS FILTER
# ============================================================

numbers = range(1, 11)

result = [
    number
    for number in numbers
    if number % 2 == 0
]

print(result)


# Equivalent filter():

result = list(
    filter(lambda number: number % 2 == 0, numbers)
)

print(result)


# ============================================================
# 70. LIST COMPREHENSION WITH RANGE
# ============================================================

squares = [
    number * number
    for number in range(1, 11)
]

print(squares)


# ============================================================
# 71. LIST COMPREHENSION WITH USER DATA
# ============================================================

numbers = [10, 15, 20, 25, 30]

greater_than_20 = [
    number
    for number in numbers
    if number > 20
]

print(greater_than_20)


# ============================================================
# 72. DATA CLEANING
# ============================================================

data = [
    " Python ",
    "",
    " Java ",
    "   ",
    "C++"
]

cleaned_data = [
    value.strip()
    for value in data
    if value.strip()
]

print(cleaned_data)


# ============================================================
# 73. CONVERT DATA TYPES
# ============================================================

values = ["10", "20", "30", "40"]

numbers = [
    int(value)
    for value in values
]

print(numbers)


# ============================================================
# 74. FLOAT CONVERSION
# ============================================================

values = ["10.5", "20.25", "30.75"]

numbers = [
    float(value)
    for value in values
]

print(numbers)


# ============================================================
# 75. FILTER VALID INTEGER STRINGS
# ============================================================

values = ["10", "abc", "20", "hello", "30"]

numbers = [
    int(value)
    for value in values
    if value.isdigit()
]

print(numbers)


# ============================================================
# 76. PRACTICAL EXAMPLE — PRODUCT PRICES
# ============================================================

prices = [100, 250, 500, 1000]

discounted_prices = [
    price * 0.90
    for price in prices
]

print(discounted_prices)


# ============================================================
# 77. PRACTICAL EXAMPLE — DISCOUNT CONDITION
# ============================================================

prices = [100, 250, 500, 1000]

final_prices = [
    price * 0.90
    if price >= 500
    else price
    for price in prices
]

print(final_prices)


# ============================================================
# 78. PRACTICAL EXAMPLE — STUDENT STATUS
# ============================================================

marks = [35, 55, 72, 91, 28]

status = [
    "Pass" if mark >= 40 else "Fail"
    for mark in marks
]

print(status)


# ============================================================
# 79. PRACTICAL EXAMPLE — EVEN NUMBERS SQUARED
# ============================================================

numbers = range(1, 21)

result = [
    number ** 2
    for number in numbers
    if number % 2 == 0
]

print(result)


# ============================================================
# 80. PRACTICAL EXAMPLE — USERNAMES
# ============================================================

names = [
    "Kishor Patil",
    "Rahul Sharma",
    "Amit Kumar"
]

usernames = [
    name.lower().replace(" ", "_")
    for name in names
]

print(usernames)


# ============================================================
# 81. PRACTICAL EXAMPLE — EMAIL DOMAINS
# ============================================================

emails = [
    "kishor@example.com",
    "rahul@gmail.com",
    "amit@example.com"
]

domains = [
    email.split("@")[1]
    for email in emails
]

print(domains)


# ============================================================
# 82. PRACTICAL EXAMPLE — VALID EMAILS
# ============================================================

emails = [
    "kishor@example.com",
    "invalid-email",
    "rahul@gmail.com"
]

valid_emails = [
    email
    for email in emails
    if "@" in email
]

print(valid_emails)


# ============================================================
# 83. PRACTICAL EXAMPLE — FILE EXTENSIONS
# ============================================================

files = [
    "main.py",
    "index.html",
    "style.css",
    "app.py"
]

python_files = [
    file
    for file in files
    if file.endswith(".py")
]

print(python_files)


# ============================================================
# 84. PRACTICAL EXAMPLE — EXTRACT FILE EXTENSIONS
# ============================================================

files = [
    "main.py",
    "index.html",
    "style.css"
]

extensions = [
    file.split(".")[-1]
    for file in files
]

print(extensions)


# ============================================================
# 85. PRACTICAL EXAMPLE — API DATA
# ============================================================

users = [
    {"id": 1, "name": "Kishor", "active": True},
    {"id": 2, "name": "Rahul", "active": False},
    {"id": 3, "name": "Amit", "active": True}
]

active_users = [
    user["name"]
    for user in users
    if user["active"]
]

print(active_users)


# ============================================================
# 86. PRACTICAL EXAMPLE — HIGH SCORERS
# ============================================================

students = [
    {"name": "Kishor", "marks": 90},
    {"name": "Rahul", "marks": 65},
    {"name": "Amit", "marks": 95},
    {"name": "Sneha", "marks": 72}
]

high_scorers = [
    student["name"]
    for student in students
    if student["marks"] >= 80
]

print(high_scorers)


# ============================================================
# 87. PRACTICAL EXAMPLE — NORMALIZE NAMES
# ============================================================

names = [
    "kishor",
    "RAHUL",
    "amit",
    "Sneha"
]

normalized_names = [
    name.strip().title()
    for name in names
]

print(normalized_names)


# ============================================================
# 88. PRACTICAL EXAMPLE — TEMPERATURE CONVERSION
# ============================================================

celsius = [0, 10, 20, 30, 40]

fahrenheit = [
    (temperature * 9 / 5) + 32
    for temperature in celsius
]

print(fahrenheit)


# ============================================================
# 89. PRACTICAL EXAMPLE — POSITIVE SQUARES
# ============================================================

numbers = [-5, -2, 0, 2, 5]

result = [
    number ** 2
    for number in numbers
    if number > 0
]

print(result)


# ============================================================
# 90. PRACTICAL EXAMPLE — PRIME NUMBERS
# ============================================================

numbers = range(2, 51)

primes = [
    number
    for number in numbers
    if all(
        number % divisor != 0
        for divisor in range(2, int(number ** 0.5) + 1)
    )
]

print(primes)


# ============================================================
# 91. PRACTICAL EXAMPLE — COMMON ELEMENTS
# ============================================================

list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

common = [
    value
    for value in list_a
    if value in list_b
]

print(common)


# ============================================================
# 92. PRACTICAL EXAMPLE — DIFFERENCE
# ============================================================

list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5]

difference = [
    value
    for value in list_a
    if value not in list_b
]

print(difference)


# ============================================================
# 93. PRACTICAL EXAMPLE — ZIP DATA
# ============================================================

names = ["Kishor", "Rahul", "Amit"]
marks = [90, 85, 95]

students = [
    {"name": name, "marks": mark}
    for name, mark in zip(names, marks)
]

print(students)


# ============================================================
# 94. PRACTICAL EXAMPLE — ENUMERATED DATA
# ============================================================

tasks = [
    "Learn Python",
    "Practice Lists",
    "Build Project"
]

numbered_tasks = [
    f"{index}. {task}"
    for index, task in enumerate(tasks, start=1)
]

print(numbered_tasks)


# ============================================================
# 95. CONDITIONAL EXPRESSION VS FILTER
# ============================================================

numbers = range(1, 6)

# Conditional expression:
result = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]

print(result)


# Filter:
result = [
    number
    for number in numbers
    if number % 2 == 0
]

print(result)


# ============================================================
# 96. NESTED LIST COMPREHENSION
# ============================================================

result = [
    [number * multiplier for number in range(1, 4)]
    for multiplier in range(1, 4)
]

print(result)


# ============================================================
# 97. FLATTEN NESTED LIST
# ============================================================

nested = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
]

flat = [
    value
    for group in nested
    for value in group
]

print(flat)


# ============================================================
# 98. AVOID OVERLY COMPLEX COMPREHENSIONS
# ============================================================

"""
A list comprehension should remain readable.

Avoid writing extremely complex expressions such as:

    result = [
        complicated_expression
        for ...
        if ...
        for ...
        if ...
    ]

When a comprehension becomes difficult to understand,
use a normal for loop instead.
"""


# ============================================================
# 99. LIST COMPREHENSION VS NORMAL LOOP
# ============================================================

numbers = range(1, 6)

# List comprehension:

squares = [
    number ** 2
    for number in numbers
]

print(squares)


# Normal loop:

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)


# ============================================================
# 100. PROFESSIONAL NOTES
# ============================================================

"""
PROFESSIONAL NOTES
------------------

1. List comprehension creates a new list.

2. Basic syntax:

       [expression for item in iterable]

3. Filtering syntax:

       [expression for item in iterable if condition]

4. Conditional expression syntax:

       [value_if_true if condition else value_if_false
        for item in iterable]

5. List comprehensions are useful for:
       - transformation
       - filtering
       - data cleaning
       - simple calculations
       - flattening nested lists

6. A comprehension should be readable.

7. Do not use list comprehension only for side effects.

8. If the logic becomes complicated, use a normal for loop.

9. Nested comprehensions are powerful but can become difficult
   to read.

10. List comprehensions create lists immediately, so for very
    large datasets a generator expression may use less memory.

11. List comprehensions can work with:
       - lists
       - tuples
       - strings
       - sets
       - dictionaries
       - ranges
       - generators
       - other iterables

12. The loop variable in a comprehension is local to the
    comprehension's execution scope.

13. Comprehensions are an important Pythonic technique,
    but readability should always come first.
"""


# ============================================================
# END OF LIST COMPREHENSION
# ============================================================

print("\nList comprehension demonstration completed successfully!")
