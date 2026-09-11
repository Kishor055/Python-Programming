"""
01_for_loop.py
==============

Python for Loop

A for loop is used to iterate over the items of an iterable.

Syntax:

    for variable in iterable:
        # code

Common iterables:
    - list
    - tuple
    - string
    - set
    - dictionary
    - range()
"""


# ============================================================
# 1. BASIC FOR LOOP
# ============================================================

for number in [1, 2, 3, 4, 5]:
    print(number)


# ============================================================
# 2. ITERATE OVER A STRING
# ============================================================

for character in "Python":
    print(character)


# ============================================================
# 3. ITERATE OVER A LIST
# ============================================================

languages = ["Python", "Java", "C++", "JavaScript"]

for language in languages:
    print(language)


# ============================================================
# 4. ITERATE OVER A TUPLE
# ============================================================

numbers = (10, 20, 30, 40)

for number in numbers:
    print(number)


# ============================================================
# 5. ITERATE OVER A SET
# ============================================================

numbers = {10, 20, 30, 40}

for number in numbers:
    print(number)


# Set iteration order should not be relied upon.


# ============================================================
# 6. ITERATE OVER A DICTIONARY
# ============================================================

student = {
    "name": "Kishor",
    "age": 21,
    "course": "Python"
}

for key in student:
    print(key)


# ============================================================
# 7. ITERATE OVER DICTIONARY VALUES
# ============================================================

for value in student.values():
    print(value)


# ============================================================
# 8. ITERATE OVER DICTIONARY KEYS AND VALUES
# ============================================================

for key, value in student.items():
    print(key, ":", value)


# ============================================================
# 9. USING range()
# ============================================================

for number in range(5):
    print(number)


# range(5) generates:
# 0, 1, 2, 3, 4


# ============================================================
# 10. range() WITH START AND STOP
# ============================================================

for number in range(1, 6):
    print(number)


# ============================================================
# 11. range() WITH STEP
# ============================================================

for number in range(1, 11, 2):
    print(number)


# ============================================================
# 12. COUNT BACKWARD
# ============================================================

for number in range(10, 0, -1):
    print(number)


# ============================================================
# 13. EVEN NUMBERS
# ============================================================

for number in range(2, 11, 2):
    print(number)


# ============================================================
# 14. ODD NUMBERS
# ============================================================

for number in range(1, 11, 2):
    print(number)


# ============================================================
# 15. SQUARES
# ============================================================

for number in range(1, 6):
    print(number ** 2)


# ============================================================
# 16. CUBES
# ============================================================

for number in range(1, 6):
    print(number ** 3)


# ============================================================
# 17. SUM OF NUMBERS
# ============================================================

total = 0

for number in range(1, 11):
    total += number

print("Total:", total)


# ============================================================
# 18. MULTIPLICATION TABLE
# ============================================================

number = 5

for multiplier in range(1, 11):
    print(number, "x", multiplier, "=", number * multiplier)


# ============================================================
# 19. MULTIPLICATION TABLE USING F-STRING
# ============================================================

number = 7

for multiplier in range(1, 11):
    print(f"{number} x {multiplier} = {number * multiplier}")


# ============================================================
# 20. LOOP THROUGH LIST
# ============================================================

marks = [85, 90, 78, 92, 88]

for mark in marks:
    print(mark)


# ============================================================
# 21. CALCULATE TOTAL MARKS
# ============================================================

marks = [85, 90, 78, 92, 88]

total = 0

for mark in marks:
    total += mark

print("Total:", total)


# ============================================================
# 22. CALCULATE AVERAGE
# ============================================================

marks = [85, 90, 78, 92, 88]

total = 0

for mark in marks:
    total += mark

average = total / len(marks)

print("Average:", average)


# ============================================================
# 23. FIND MAXIMUM WITHOUT max()
# ============================================================

numbers = [10, 50, 30, 90, 20]

maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

print("Maximum:", maximum)


# ============================================================
# 24. FIND MINIMUM WITHOUT min()
# ============================================================

numbers = [10, 50, 30, 90, 20]

minimum = numbers[0]

for number in numbers:
    if number < minimum:
        minimum = number

print("Minimum:", minimum)


# ============================================================
# 25. COUNT EVEN NUMBERS
# ============================================================

numbers = [10, 15, 22, 31, 40, 55]

count = 0

for number in numbers:
    if number % 2 == 0:
        count += 1

print("Even numbers:", count)


# ============================================================
# 26. COUNT ODD NUMBERS
# ============================================================

numbers = [10, 15, 22, 31, 40, 55]

count = 0

for number in numbers:
    if number % 2 != 0:
        count += 1

print("Odd numbers:", count)


# ============================================================
# 27. FILTER EVEN NUMBERS
# ============================================================

numbers = [10, 15, 22, 31, 40, 55]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)


# ============================================================
# 28. FILTER ODD NUMBERS
# ============================================================

numbers = [10, 15, 22, 31, 40, 55]

odd_numbers = []

for number in numbers:
    if number % 2 != 0:
        odd_numbers.append(number)

print(odd_numbers)


# ============================================================
# 29. STRING CHARACTERS
# ============================================================

text = "Python"

for character in text:
    print(character)


# ============================================================
# 30. COUNT VOWELS
# ============================================================

text = "Python Programming"

vowels = "aeiou"

count = 0

for character in text.lower():
    if character in vowels:
        count += 1

print("Vowels:", count)


# ============================================================
# 31. COUNT CONSONANTS
# ============================================================

text = "Python Programming"

vowels = "aeiou"

count = 0

for character in text.lower():
    if character.isalpha() and character not in vowels:
        count += 1

print("Consonants:", count)


# ============================================================
# 32. COUNT DIGITS
# ============================================================

text = "Python123Programming456"

count = 0

for character in text:
    if character.isdigit():
        count += 1

print("Digits:", count)


# ============================================================
# 33. REVERSE A STRING
# ============================================================

text = "Python"

reversed_text = ""

for character in text:
    reversed_text = character + reversed_text

print(reversed_text)


# ============================================================
# 34. BUILD A STRING
# ============================================================

words = ["Python", "is", "powerful"]

sentence = ""

for word in words:
    sentence += word + " "

print(sentence.strip())


# ============================================================
# 35. ENUMERATE
# ============================================================

languages = ["Python", "Java", "C++"]

for index, language in enumerate(languages):
    print(index, language)


# ============================================================
# 36. ENUMERATE STARTING FROM 1
# ============================================================

languages = ["Python", "Java", "C++"]

for index, language in enumerate(languages, start=1):
    print(index, language)


# ============================================================
# 37. ZIP
# ============================================================

names = ["Kishor", "Rahul", "Amit"]
marks = [90, 85, 95]

for name, mark in zip(names, marks):
    print(name, mark)


# ============================================================
# 38. ZIP THREE ITERABLES
# ============================================================

names = ["Kishor", "Rahul", "Amit"]
marks = [90, 85, 95]
courses = ["Python", "Java", "C++"]

for name, mark, course in zip(names, marks, courses):
    print(name, mark, course)


# ============================================================
# 39. NESTED FOR LOOP
# ============================================================

for row in range(3):
    for column in range(3):
        print(row, column)


# ============================================================
# 40. NESTED LOOP — MATRIX
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for value in row:
        print(value)


# ============================================================
# 41. PRINT MATRIX
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()


# ============================================================
# 42. STAR PATTERN
# ============================================================

for row in range(1, 6):
    for column in range(row):
        print("*", end=" ")
    print()


# ============================================================
# 43. NUMBER PATTERN
# ============================================================

for row in range(1, 6):
    for column in range(row):
        print(row, end=" ")
    print()


# ============================================================
# 44. MULTIPLICATION TABLES
# ============================================================

for number in range(1, 6):
    for multiplier in range(1, 11):
        print(
            f"{number} x {multiplier} = "
            f"{number * multiplier}"
        )
    print()


# ============================================================
# 45. BREAK
# ============================================================
# break immediately terminates the loop.


for number in range(1, 11):
    if number == 5:
        break

    print(number)


# ============================================================
# 46. BREAK — SEARCH
# ============================================================

numbers = [10, 20, 30, 40, 50]

target = 30

for number in numbers:
    if number == target:
        print("Found:", target)
        break


# ============================================================
# 47. CONTINUE
# ============================================================
# continue skips the current iteration.


for number in range(1, 11):
    if number == 5:
        continue

    print(number)


# ============================================================
# 48. PRINT ONLY ODD NUMBERS USING CONTINUE
# ============================================================

for number in range(1, 11):
    if number % 2 == 0:
        continue

    print(number)


# ============================================================
# 49. PASS
# ============================================================
# pass does nothing.
# It is used as a placeholder.


for number in range(5):
    pass


# ============================================================
# 50. FOR-ELSE
# ============================================================
# The else block executes when the loop completes normally.
# It does not execute if the loop terminates using break.


for number in range(5):
    print(number)
else:
    print("Loop completed")


# ============================================================
# 51. FOR-ELSE WITH BREAK
# ============================================================

for number in range(1, 10):
    if number == 5:
        break

    print(number)
else:
    print("Loop completed")


# ============================================================
# 52. SEARCH USING FOR-ELSE
# ============================================================

numbers = [10, 20, 30, 40]

target = 50

for number in numbers:
    if number == target:
        print("Found")
        break
else:
    print("Not found")


# ============================================================
# 53. PRIME NUMBER CHECK
# ============================================================

number = 29

if number < 2:
    print("Not prime")
else:
    for divisor in range(2, number):
        if number % divisor == 0:
            print("Not prime")
            break
    else:
        print("Prime")


# ============================================================
# 54. PRIME NUMBERS
# ============================================================

for number in range(2, 51):

    for divisor in range(2, number):

        if number % divisor == 0:
            break

    else:
        print(number)


# ============================================================
# 55. OPTIMIZED PRIME NUMBER CHECK
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
# 56. FACTORIAL
# ============================================================

number = 5

factorial = 1

for value in range(1, number + 1):
    factorial *= value

print("Factorial:", factorial)


# ============================================================
# 57. FIBONACCI SERIES
# ============================================================

terms = 10

first = 0
second = 1

for _ in range(terms):
    print(first, end=" ")

    first, second = second, first + second

print()


# ============================================================
# 58. SUM OF DIGITS
# ============================================================

number = 12345

total = 0

for digit in str(number):
    total += int(digit)

print("Sum:", total)


# ============================================================
# 59. PRODUCT OF DIGITS
# ============================================================

number = 12345

product = 1

for digit in str(number):
    product *= int(digit)

print("Product:", product)


# ============================================================
# 60. COUNT DIGITS IN A NUMBER
# ============================================================

number = 123456

count = 0

for _ in str(number):
    count += 1

print("Digits:", count)


# ============================================================
# 61. FIND DUPLICATES
# ============================================================

numbers = [10, 20, 10, 30, 20, 40]

duplicates = []

for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)

print(duplicates)


# ============================================================
# 62. REMOVE DUPLICATES
# ============================================================

numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)


# ============================================================
# 63. COMMON ELEMENTS
# ============================================================

list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

common = []

for value in list_a:
    if value in list_b:
        common.append(value)

print(common)


# ============================================================
# 64. WORD LENGTHS
# ============================================================

words = ["Python", "Java", "Programming"]

for word in words:
    print(word, len(word))


# ============================================================
# 65. FILTER LONG WORDS
# ============================================================

words = [
    "Python",
    "Java",
    "Programming",
    "C++"
]

for word in words:
    if len(word) > 4:
        print(word)


# ============================================================
# 66. DICTIONARY OF SQUARES
# ============================================================

squares = {}

for number in range(1, 6):
    squares[number] = number ** 2

print(squares)


# ============================================================
# 67. DICTIONARY ITERATION
# ============================================================

student = {
    "name": "Kishor",
    "age": 21,
    "marks": 90
}

for key, value in student.items():
    print(f"{key}: {value}")


# ============================================================
# 68. LIST OF DICTIONARIES
# ============================================================

students = [
    {"name": "Kishor", "marks": 90},
    {"name": "Rahul", "marks": 85},
    {"name": "Amit", "marks": 95}
]

for student in students:
    print(
        student["name"],
        student["marks"]
    )


# ============================================================
# 69. FILTER STUDENTS
# ============================================================

students = [
    {"name": "Kishor", "marks": 90},
    {"name": "Rahul", "marks": 35},
    {"name": "Amit", "marks": 95}
]

for student in students:
    if student["marks"] >= 40:
        print(student["name"])


# ============================================================
# 70. LOOP WITH CONDITIONAL EXPRESSION
# ============================================================

numbers = range(1, 6)

for number in numbers:
    result = "Even" if number % 2 == 0 else "Odd"
    print(number, result)


# ============================================================
# 71. IGNORE LOOP VARIABLE
# ============================================================
# Use `_` when the loop variable is not needed.


for _ in range(5):
    print("Hello")


# ============================================================
# 72. ITERATE OVER INDEXES
# ============================================================

languages = ["Python", "Java", "C++"]

for index in range(len(languages)):
    print(index, languages[index])


# enumerate() is generally more readable:

for index, language in enumerate(languages):
    print(index, language)


# ============================================================
# 73. REVERSE ITERATION
# ============================================================

for number in range(10, 0, -1):
    print(number)


# ============================================================
# 74. REVERSE A LIST
# ============================================================

numbers = [1, 2, 3, 4, 5]

for number in reversed(numbers):
    print(number)


# ============================================================
# 75. SORTED ITERATION
# ============================================================

numbers = [50, 10, 40, 20, 30]

for number in sorted(numbers):
    print(number)


# ============================================================
# 76. SORTED REVERSE ITERATION
# ============================================================

numbers = [50, 10, 40, 20, 30]

for number in sorted(numbers, reverse=True):
    print(number)


# ============================================================
# 77. LOOP OVER FILE-LIKE DATA
# ============================================================

lines = [
    "First line",
    "Second line",
    "Third line"
]

for line in lines:
    print(line)


# ============================================================
# 78. NESTED LOOP WITH BREAK
# ============================================================

for row in range(3):

    for column in range(3):

        if column == 1:
            break

        print(row, column)


# break only terminates the innermost loop.


# ============================================================
# 79. NESTED LOOP WITH CONTINUE
# ============================================================

for row in range(3):

    for column in range(3):

        if column == 1:
            continue

        print(row, column)


# ============================================================
# 80. SEARCH MATRIX
# ============================================================

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

target = 50

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
# 81. LOOP WITH ELSE FOR MATRIX SEARCH
# ============================================================

matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

target = 100

for row in matrix:

    for value in row:

        if value == target:
            print("Found")
            break

    else:
        continue

    break

else:
    print("Not found")


# ============================================================
# 82. PRACTICAL EXAMPLE — SHOPPING CART
# ============================================================

cart = [
    {"name": "Laptop", "price": 50000},
    {"name": "Mouse", "price": 1000},
    {"name": "Keyboard", "price": 2000}
]

total = 0

for item in cart:
    total += item["price"]

print("Cart total:", total)


# ============================================================
# 83. PRACTICAL EXAMPLE — STUDENT REPORT
# ============================================================

students = [
    {"name": "Kishor", "marks": 90},
    {"name": "Rahul", "marks": 75},
    {"name": "Amit", "marks": 35}
]

for student in students:

    if student["marks"] >= 40:
        status = "Pass"
    else:
        status = "Fail"

    print(
        student["name"],
        student["marks"],
        status
    )


# ============================================================
# 84. PRACTICAL EXAMPLE — DISCOUNT
# ============================================================

prices = [100, 250, 500, 1000]

for price in prices:

    if price >= 500:
        discount = price * 0.10
    else:
        discount = 0

    final_price = price - discount

    print(final_price)


# ============================================================
# 85. PRACTICAL EXAMPLE — WORD SEARCH
# ============================================================

words = [
    "Python",
    "Java",
    "C++",
    "JavaScript"
]

target = "Python"

for word in words:

    if word == target:
        print("Found")
        break

else:
    print("Not found")


# ============================================================
# 86. PRACTICAL EXAMPLE — LOGIN ATTEMPTS
# ============================================================

correct_password = "python123"

attempts = [
    "hello",
    "admin",
    "python123"
]

for password in attempts:

    if password == correct_password:
        print("Login successful")
        break

    print("Incorrect password")


# ============================================================
# 87. PRACTICAL EXAMPLE — TEMPERATURES
# ============================================================

temperatures = [25, 30, 35, 40, 28]

for temperature in temperatures:

    if temperature >= 35:
        print(
            temperature,
            "High temperature"
        )
    else:
        print(
            temperature,
            "Normal temperature"
        )


# ============================================================
# 88. PRACTICAL EXAMPLE — DATA VALIDATION
# ============================================================

values = ["10", "20", "abc", "30"]

for value in values:

    if value.isdigit():
        print("Valid:", value)
    else:
        print("Invalid:", value)


# ============================================================
# 89. PRACTICAL EXAMPLE — FILE PROCESSING
# ============================================================

files = [
    "main.py",
    "index.html",
    "app.py",
    "style.css"
]

for file in files:

    if file.endswith(".py"):
        print("Python file:", file)


# ============================================================
# 90. FOR LOOP WITH FUNCTION
# ============================================================

def square(number):
    return number ** 2


numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(square(number))


# ============================================================
# 91. FOR LOOP WITH FUNCTION AND CONDITION
# ============================================================

def is_even(number):
    return number % 2 == 0


numbers = range(1, 11)

for number in numbers:

    if is_even(number):
        print(number)


# ============================================================
# 92. LOOPING OVER MULTIPLE VALUES
# ============================================================

names = ["Kishor", "Rahul", "Amit"]
ages = [21, 22, 20]

for name, age in zip(names, ages):
    print(
        f"{name} is {age} years old"
    )


# ============================================================
# 93. UNPACKING TUPLES
# ============================================================

students = [
    ("Kishor", 90),
    ("Rahul", 85),
    ("Amit", 95)
]

for name, marks in students:
    print(name, marks)


# ============================================================
# 94. UNPACKING NESTED DATA
# ============================================================

students = [
    ("Kishor", (90, 85, 95)),
    ("Rahul", (80, 75, 88))
]

for name, marks in students:
    print(name)

    for mark in marks:
        print(mark)


# ============================================================
# 95. LOOP WITH INDEX AND VALUE
# ============================================================

languages = [
    "Python",
    "Java",
    "C++",
    "JavaScript"
]

for index, language in enumerate(
    languages,
    start=1
):
    print(
        f"{index}. {language}"
    )


# ============================================================
# 96. PERFORMANCE NOTE
# ============================================================

"""
Prefer direct iteration when the index is not required:

    for value in values:
        print(value)

Instead of:

    for index in range(len(values)):
        print(values[index])

Use enumerate() when both index and value are needed:

    for index, value in enumerate(values):
        print(index, value)
"""


# ============================================================
# 97. ITERABLE VS ITERATOR
# ============================================================

"""
An iterable is an object that can be iterated over.

Examples:
    list
    tuple
    string
    set
    dictionary
    range

The for loop internally obtains an iterator and repeatedly
requests the next item until StopIteration occurs.
"""


# ============================================================
# 98. ITERATOR EXAMPLE
# ============================================================

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# ============================================================
# 99. FOR LOOP IS PYTHONIC
# ============================================================

numbers = [10, 20, 30]

for number in numbers:
    print(number)


# ============================================================
# 100. PROFESSIONAL NOTES
# ============================================================

"""
PROFESSIONAL NOTES
------------------

1. A for loop iterates over an iterable.

2. Common iterables:
       - list
       - tuple
       - string
       - set
       - dictionary
       - range

3. Use range() when a sequence of numbers is required.

4. Use enumerate() when both index and value are required.

5. Use zip() to iterate over multiple iterables together.

6. Use break to terminate a loop early.

7. Use continue to skip the current iteration.

8. Use pass as a placeholder when no action is required.

9. A for-else block executes else when the loop completes
   without encountering break.

10. Nested loops are useful for multidimensional data but
    can increase computational complexity.

11. Prefer direct iteration over:
       range(len(sequence))
    when the index is not required.

12. Keep loop bodies simple and readable.

13. Avoid modifying a collection while directly iterating
    over it unless the behavior is intentionally controlled.

14. For large datasets, understand the cost of nested loops
    and repeated operations such as `in` and `count()`.

15. Python's for loop works with any object implementing the
    iteration protocol.
"""


# ============================================================
# END OF FOR LOOP
# ============================================================

print("\nFor loop demonstration completed successfully!")
