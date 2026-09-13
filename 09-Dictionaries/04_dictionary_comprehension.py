"""
04_dictionary_comprehension.py
------------------------------
Python Dictionary Comprehension.

Dictionary comprehension provides a concise way to create
dictionaries using an expression and an iterable.

Topics covered:
    1. Basic dictionary comprehension
    2. Creating key-value pairs
    3. Expressions
    4. Filtering with conditions
    5. if-else expressions
    6. Working with strings
    7. Transforming dictionaries
    8. Filtering dictionaries
    9. Nested loops
    10. Practical examples
    11. Traditional loop vs comprehension
"""


# ============================================================
# 1. Basic Dictionary Comprehension
# ============================================================
# Syntax:
#
#     {key: value for item in iterable}
#
# Example:

numbers = range(1, 6)

squares = {
    number: number ** 2
    for number in numbers
}

print("Squares:", squares)


# ============================================================
# 2. Creating Key-Value Pairs
# ============================================================

numbers = range(1, 6)

number_names = {
    number: f"Number {number}"
    for number in numbers
}

print("\nNumber names:")
print(number_names)


# ============================================================
# 3. Dictionary Comprehension with an Expression
# ============================================================
# Transform values while creating the dictionary.


numbers = range(1, 6)

doubled = {
    number: number * 2
    for number in numbers
}

print("\nDoubled values:")
print(doubled)


# Another example

numbers = range(1, 6)

cubed = {
    number: number ** 3
    for number in numbers
}

print("Cubed values:")
print(cubed)


# ============================================================
# 4. Dictionary Comprehension with a Condition
# ============================================================
# Syntax:
#
#     {
#         key: value
#         for item in iterable
#         if condition
#     }
#
# Example:
# Create a dictionary containing only even numbers.


numbers = range(1, 11)

even_numbers = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}

print("\nEven number squares:")
print(even_numbers)


# ============================================================
# 5. Filter Odd Numbers
# ============================================================

numbers = range(1, 11)

odd_numbers = {
    number: number ** 2
    for number in numbers
    if number % 2 != 0
}

print("\nOdd number squares:")
print(odd_numbers)


# ============================================================
# 6. if-else in Dictionary Comprehension
# ============================================================
# Syntax:
#
#     {
#         key: value_if_true if condition else value_if_false
#         for item in iterable
#     }


numbers = range(1, 6)

number_types = {
    number: "Even" if number % 2 == 0 else "Odd"
    for number in numbers
}

print("\nNumber types:")
print(number_types)


# Expected result:
#
# {
#     1: "Odd",
#     2: "Even",
#     3: "Odd",
#     4: "Even",
#     5: "Odd"
# }


# ============================================================
# 7. Working with Strings
# ============================================================
# Create a dictionary containing each character and
# its uppercase version.


text = "python"

uppercase = {
    character: character.upper()
    for character in text
}

print("\nUppercase characters:")
print(uppercase)


# ============================================================
# 8. Character Length Dictionary
# ============================================================

words = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
]

word_lengths = {
    word: len(word)
    for word in words
}

print("\nWord lengths:")
print(word_lengths)


# ============================================================
# 9. Filter Words by Length
# ============================================================

words = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "Go",
]

long_words = {
    word: len(word)
    for word in words
    if len(word) > 4
}

print("\nWords longer than 4 characters:")
print(long_words)


# ============================================================
# 10. Convert List to Dictionary
# ============================================================
# Create a dictionary where each number is mapped to its
# position.


numbers = [10, 20, 30, 40, 50]

number_positions = {
    index: value
    for index, value in enumerate(numbers)
}

print("\nNumber positions:")
print(number_positions)


# ============================================================
# 11. Transform an Existing Dictionary
# ============================================================

prices = {
    "Laptop": 75000,
    "Mouse": 1000,
    "Keyboard": 2500,
}

discounted_prices = {
    product: price * 0.90
    for product, price in prices.items()
}

print("\nDiscounted prices:")
print(discounted_prices)


# ============================================================
# 12. Filter an Existing Dictionary
# ============================================================
# Keep products whose price is greater than 2000.


prices = {
    "Laptop": 75000,
    "Mouse": 1000,
    "Keyboard": 2500,
    "Monitor": 15000,
}

expensive_products = {
    product: price
    for product, price in prices.items()
    if price > 2000
}

print("\nProducts above 2000:")
print(expensive_products)


# ============================================================
# 13. Filter Students by Marks
# ============================================================

marks = {
    "Alice": 92,
    "Bob": 75,
    "Charlie": 88,
    "David": 65,
}

top_students = {
    name: score
    for name, score in marks.items()
    if score >= 80
}

print("\nStudents scoring 80 or above:")
print(top_students)


# ============================================================
# 14. Transform Student Marks
# ============================================================
# Add 5 bonus marks.


marks = {
    "Alice": 92,
    "Bob": 75,
    "Charlie": 88,
}

updated_marks = {
    name: score + 5
    for name, score in marks.items()
}

print("\nMarks after bonus:")
print(updated_marks)


# ============================================================
# 15. Categorize Student Performance
# ============================================================

marks = {
    "Alice": 92,
    "Bob": 75,
    "Charlie": 58,
    "David": 35,
}

performance = {
    name: (
        "Excellent"
        if score >= 80
        else "Good"
        if score >= 60
        else "Needs Improvement"
    )
    for name, score in marks.items()
}

print("\nStudent performance:")
print(performance)


# ============================================================
# 16. Convert Keys to Uppercase
# ============================================================

user = {
    "name": "Alice",
    "age": 21,
    "city": "Pune",
}

uppercase_keys = {
    key.upper(): value
    for key, value in user.items()
}

print("\nUppercase keys:")
print(uppercase_keys)


# ============================================================
# 17. Convert Values to Strings
# ============================================================

data = {
    "id": 101,
    "age": 21,
    "active": True,
}

string_values = {
    key: str(value)
    for key, value in data.items()
}

print("\nString values:")
print(string_values)


# ============================================================
# 18. Swap Keys and Values
# ============================================================
# This works when values are unique and hashable.


original = {
    "Alice": 101,
    "Bob": 102,
    "Charlie": 103,
}

swapped = {
    value: key
    for key, value in original.items()
}

print("\nSwapped dictionary:")
print(swapped)


# ============================================================
# 19. Dictionary Comprehension with enumerate()
# ============================================================

languages = [
    "Python",
    "Java",
    "JavaScript",
    "C++",
]

language_index = {
    index: language
    for index, language in enumerate(languages)
}

print("\nLanguage index:")
print(language_index)


# ============================================================
# 20. Dictionary Comprehension with zip()
# ============================================================
# zip() combines multiple iterables.


keys = ["name", "age", "city"]
values = ["Alice", 21, "Pune"]

person = {
    key: value
    for key, value in zip(keys, values)
}

print("\nPerson:")
print(person)


# ============================================================
# 21. Nested Dictionary Comprehension
# ============================================================
# Create a multiplication table.


multiplication_table = {
    number: {
        multiplier: number * multiplier
        for multiplier in range(1, 6)
    }
    for number in range(1, 4)
}

print("\nMultiplication table:")
print(multiplication_table)


# Access a value:

print(
    "3 x 4 =",
    multiplication_table[3][4],
)


# ============================================================
# 22. Dictionary Comprehension with Nested Loops
# ============================================================
# Create coordinate keys.


coordinates = {
    f"{x},{y}": x + y
    for x in range(1, 4)
    for y in range(1, 4)
}

print("\nCoordinates:")
print(coordinates)


# ============================================================
# 23. Filter and Transform at the Same Time
# ============================================================

numbers = range(1, 11)

result = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
    and number > 4
}

print("\nEven numbers greater than 4:")
print(result)


# ============================================================
# 24. Practical Example — Product Inventory
# ============================================================

inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15,
    "Monitor": 5,
}

low_stock = {
    product: quantity
    for product, quantity in inventory.items()
    if quantity < 10
}

print("\nLow-stock products:")
print(low_stock)


# ============================================================
# 25. Practical Example — Email Domains
# ============================================================

emails = [
    "alice@gmail.com",
    "bob@yahoo.com",
    "charlie@gmail.com",
    "david@outlook.com",
]

email_domains = {
    email: email.split("@")[1]
    for email in emails
}

print("\nEmail domains:")
print(email_domains)


# ============================================================
# 26. Practical Example — User Status
# ============================================================

users = {
    "Alice": True,
    "Bob": False,
    "Charlie": True,
    "David": False,
}

user_status = {
    username: "Active" if active else "Inactive"
    for username, active in users.items()
}

print("\nUser status:")
print(user_status)


# ============================================================
# 27. Practical Example — Normalize Usernames
# ============================================================

usernames = [
    "Alice",
    "BOB",
    "charlie",
    "ALICE",
]

normalized = {
    username.lower(): username
    for username in usernames
}

print("\nNormalized usernames:")
print(normalized)


# ============================================================
# 28. Practical Example — Character Frequency
# ============================================================
# Dictionary comprehension can be combined with set()
# for unique characters.


text = "programming"

character_frequency = {
    character: text.count(character)
    for character in set(text)
}

print("\nCharacter frequency:")
print(character_frequency)


# ============================================================
# 29. Practical Example — API Data Transformation
# ============================================================

users = [
    {
        "id": 101,
        "name": "Alice",
    },
    {
        "id": 102,
        "name": "Bob",
    },
    {
        "id": 103,
        "name": "Charlie",
    },
]

users_by_id = {
    user["id"]: user["name"]
    for user in users
}

print("\nUsers by ID:")
print(users_by_id)


# ============================================================
# 30. Traditional Loop vs Dictionary Comprehension
# ============================================================

numbers = range(1, 6)


# Traditional approach

squares = {}

for number in numbers:
    squares[number] = number ** 2

print("\nTraditional approach:")
print(squares)


# Dictionary comprehension

squares = {
    number: number ** 2
    for number in numbers
}

print("Dictionary comprehension:")
print(squares)


# ============================================================
# 31. Traditional Filtering vs Comprehension
# ============================================================

marks = {
    "Alice": 92,
    "Bob": 75,
    "Charlie": 88,
    "David": 65,
}


# Traditional approach

passed = {}

for name, score in marks.items():
    if score >= 80:
        passed[name] = score

print("\nTraditional filtering:")
print(passed)


# Dictionary comprehension

passed = {
    name: score
    for name, score in marks.items()
    if score >= 80
}

print("Dictionary comprehension:")
print(passed)


# ============================================================
# 32. Dictionary Comprehension Syntax Cheat Sheet
# ============================================================
#
# Basic:
#
#     {
#         key: value
#         for item in iterable
#     }
#
#
# With condition:
#
#     {
#         key: value
#         for item in iterable
#         if condition
#     }
#
#
# With if-else:
#
#     {
#         key: value_if_true if condition else value_if_false
#         for item in iterable
#     }
#
#
# Existing dictionary:
#
#     {
#         key: value
#         for key, value in dictionary.items()
#     }
#
#
# Nested:
#
#     {
#         outer_key: {
#             inner_key: inner_value
#             for inner_item in iterable
#         }
#         for outer_item in iterable
#     }
#
# ============================================================


# ============================================================
# 33. Important Rules
# ============================================================
#
# 1. Dictionary comprehension creates a dictionary.
#
# 2. Every result contains a key and a value.
#
# 3. Conditions can filter elements.
#
# 4. Expressions can transform keys and values.
#
# 5. if-else can be used inside the value expression.
#
# 6. Existing dictionaries can be transformed with items().
#
# 7. Multiple loops can be used for nested data.
#
# 8. Duplicate keys are overwritten by later values.
#
# 9. Keep comprehensions readable.
#
# 10. Use a normal loop when the logic becomes too complex.
#
# ============================================================


# ============================================================
# 34. When Should You Use Dictionary Comprehension?
# ============================================================
#
# Use dictionary comprehension when:
#
# - You need to create a dictionary from an iterable.
# - You need to transform data.
# - You need to filter dictionary entries.
# - The logic is short and easy to understand.
#
# Example:
#
#     even_squares = {
#         number: number ** 2
#         for number in range(1, 11)
#         if number % 2 == 0
#     }
#
# ============================================================


# ============================================================
# 35. When NOT to Use Dictionary Comprehension
# ============================================================
#
# Avoid very complicated comprehensions.
#
# Bad readability:
#
#     result = {
#         x: (
#             "A"
#             if condition1
#             else "B"
#             if condition2
#             else "C"
#         )
#         for x in data
#         if condition3
#     }
#
# If the logic becomes difficult to understand,
# use a normal for loop instead.
#
# Professional code prioritizes readability over
# writing the shortest possible code.
#
# ============================================================


# ============================================================
# Key Takeaways
# ============================================================
#
# Dictionary comprehension:
#
#     {
#         key: value
#         for item in iterable
#     }
#
# With filtering:
#
#     {
#         key: value
#         for item in iterable
#         if condition
#     }
#
# With if-else:
#
#     {
#         key: value_if_true if condition else value_if_false
#         for item in iterable
#     }
#
# Remember:
#
#     Dictionary Comprehension
#             ↓
#       Transform / Filter
#             ↓
#        key → value
#             ↓
#        Dictionary
#
# Dictionary comprehensions are concise and powerful,
# but readability should always come first.
#
# Next:
# 05_nested_dictionaries.py
# ============================================================
