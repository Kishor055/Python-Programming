"""
01_dictionary_basics.py
-----------------------
Introduction to Python Dictionaries.

A dictionary stores data in key-value pairs.

Topics covered:
    1. Creating a dictionary
    2. Empty dictionary
    3. Key-value pairs
    4. Accessing values
    5. get()
    6. Adding elements
    7. Updating elements
    8. Dictionary length
    9. Membership testing
    10. Iterating over a dictionary
    11. Keys and values
    12. Duplicate keys
    13. Different data types
    14. Practical examples
"""


# ============================================================
# 1. Creating a Dictionary
# ============================================================
# A dictionary stores data in key-value pairs.
#
# Syntax:
#
#     {
#         key: value
#     }

student = {
    "name": "Alice",
    "age": 21,
    "course": "Python",
}

print("Student:", student)


# ============================================================
# 2. Creating an Empty Dictionary
# ============================================================

empty_dictionary = {}

print("\nEmpty dictionary:", empty_dictionary)

# Another way:

empty_dictionary = dict()

print("Using dict():", empty_dictionary)


# ============================================================
# 3. Understanding Key-Value Pairs
# ============================================================

student = {
    "name": "Alice",
    "age": 21,
    "city": "Pune",
}

# Keys:
#     "name"
#     "age"
#     "city"
#
# Values:
#     "Alice"
#     21
#     "Pune"


# ============================================================
# 4. Accessing Dictionary Values
# ============================================================
# Use the key inside square brackets.

student = {
    "name": "Alice",
    "age": 21,
    "course": "Python",
}

print("\nName:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])


# ============================================================
# 5. Accessing a Missing Key
# ============================================================
# Accessing a key that does not exist raises KeyError.
#
# Example:
#
# student = {"name": "Alice"}
# print(student["age"])
#
# Result:
# KeyError: 'age'


# ============================================================
# 6. Using get()
# ============================================================
# get() allows us to safely access a value.
#
# If the key doesn't exist, get() returns None.

student = {
    "name": "Alice",
    "age": 21,
}

print("\nName:", student.get("name"))
print("Age:", student.get("age"))
print("Email:", student.get("email"))


# ============================================================
# 7. get() with a Default Value
# ============================================================
# We can provide a default value when the key doesn't exist.

email = student.get("email", "Not available")

print("Email:", email)


# ============================================================
# 8. Adding a New Key-Value Pair
# ============================================================
# Assigning a value to a new key adds that key.

student = {
    "name": "Alice",
    "age": 21,
}

student["city"] = "Pune"

print("\nAfter adding city:", student)


# ============================================================
# 9. Updating an Existing Value
# ============================================================
# If the key already exists, its value is replaced.

student = {
    "name": "Alice",
    "age": 21,
}

student["age"] = 22

print("\nUpdated student:", student)


# ============================================================
# 10. Dictionary Length
# ============================================================
# len() returns the number of key-value pairs.

student = {
    "name": "Alice",
    "age": 21,
    "course": "Python",
}

print("\nNumber of entries:", len(student))


# ============================================================
# 11. Membership Testing
# ============================================================
# The "in" operator checks dictionary KEYS by default.

student = {
    "name": "Alice",
    "age": 21,
}

print("\nIs 'name' a key?", "name" in student)
print("Is 'email' a key?", "email" in student)


# ============================================================
# 12. not in
# ============================================================

print("Is 'email' missing?", "email" not in student)


# ============================================================
# 13. Iterating Over Dictionary Keys
# ============================================================
# Iterating directly over a dictionary gives its keys.

student = {
    "name": "Alice",
    "age": 21,
    "course": "Python",
}

print("\nDictionary keys:")

for key in student:
    print(key)


# ============================================================
# 14. Iterating Over Keys Explicitly
# ============================================================

print("\nUsing keys():")

for key in student.keys():
    print(key)


# ============================================================
# 15. Iterating Over Values
# ============================================================

print("\nDictionary values:")

for value in student.values():
    print(value)


# ============================================================
# 16. Iterating Over Key-Value Pairs
# ============================================================
# items() returns key-value pairs.

print("\nKey-value pairs:")

for key, value in student.items():
    print(key, ":", value)


# ============================================================
# 17. Dictionary with Different Data Types
# ============================================================
# Dictionary values can contain different data types.

employee = {
    "id": 1001,
    "name": "Alice",
    "salary": 75000.50,
    "is_active": True,
    "skills": ["Python", "SQL", "Git"],
}

print("\nEmployee:", employee)


# Access individual values

print("ID:", employee["id"])
print("Name:", employee["name"])
print("Salary:", employee["salary"])
print("Active:", employee["is_active"])
print("Skills:", employee["skills"])


# ============================================================
# 18. Dictionary Can Store Nested Data
# ============================================================
# A dictionary value can itself be another dictionary.

student = {
    "name": "Alice",
    "address": {
        "city": "Pune",
        "country": "India",
    },
}

print("\nStudent:", student)

print("City:", student["address"]["city"])
print("Country:", student["address"]["country"])


# ============================================================
# 19. Duplicate Keys
# ============================================================
# Dictionary keys must be unique.
#
# If the same key appears multiple times,
# the latest value replaces the previous value.

student = {
    "name": "Alice",
    "name": "Bob",
}

print("\nDuplicate key example:")
print(student)


# Output:
#
# {'name': 'Bob'}


# ============================================================
# 20. Duplicate Values
# ============================================================
# Values can be duplicated.

students = {
    "Alice": 90,
    "Bob": 90,
    "Charlie": 85,
}

print("\nDuplicate values:")
print(students)


# ============================================================
# 21. Checking Values
# ============================================================
# "in" checks keys, not values.

student = {
    "name": "Alice",
    "age": 21,
}

print("\n'Alice' in student:", "Alice" in student)

# To check values:

print(
    "'Alice' in student.values():",
    "Alice" in student.values(),
)


# ============================================================
# 22. Dictionary Keys Must Be Hashable
# ============================================================
# Common valid keys:
#
#     strings
#     integers
#     floats
#     tuples containing hashable values
#
# Example:

data = {
    "name": "Alice",
    101: "Employee ID",
    (1, 2): "Coordinates",
}

print("\nDictionary with different key types:")
print(data)


# A list cannot be a dictionary key:
#
# data = {
#     [1, 2]: "Invalid"
# }
#
# This raises:
#
# TypeError: unhashable type: 'list'


# ============================================================
# 23. Practical Example — Student Record
# ============================================================

student = {
    "id": 101,
    "name": "Alice",
    "age": 21,
    "course": "Python",
    "marks": 92,
}

print("\n--- Student Record ---")

print("ID:", student["id"])
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("Marks:", student["marks"])


# ============================================================
# 24. Practical Example — Product
# ============================================================

product = {
    "id": 501,
    "name": "Laptop",
    "price": 75000,
    "stock": 10,
}

print("\n--- Product ---")

print("Product:", product["name"])
print("Price:", product["price"])
print("Stock:", product["stock"])


# Update stock

product["stock"] = 8

print("Updated stock:", product["stock"])


# ============================================================
# 25. Practical Example — User Profile
# ============================================================

user = {
    "username": "alice",
    "email": "alice@example.com",
    "is_active": True,
}

print("\n--- User Profile ---")

if user["is_active"]:
    print("User is active.")

if "email" in user:
    print("Email:", user["email"])


# ============================================================
# 26. Practical Example — Configuration
# ============================================================

config = {
    "host": "localhost",
    "port": 8000,
    "debug": True,
}

print("\n--- Configuration ---")

print("Host:", config["host"])
print("Port:", config["port"])
print("Debug:", config["debug"])


# ============================================================
# 27. Practical Example — Word Frequency
# ============================================================
# Dictionaries are commonly used for counting.

words = [
    "python",
    "java",
    "python",
    "c++",
    "java",
    "python",
]

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("\n--- Word Frequency ---")
print(frequency)


# Expected result:
#
# {
#     "python": 3,
#     "java": 2,
#     "c++": 1
# }


# ============================================================
# 28. Dictionary Access Pattern
# ============================================================

user = {
    "name": "Alice",
    "age": 21,
}

# Required key:
# Use [] when the key must exist.

name = user["name"]

print("\nRequired value:", name)


# Optional key:
# Use get() when the key may not exist.

email = user.get("email")

print("Optional value:", email)


# ============================================================
# 29. Important Dictionary Rules
# ============================================================
#
# 1. Dictionaries store key-value pairs.
#
# 2. Keys must be unique.
#
# 3. Values can be duplicated.
#
# 4. Dictionaries are mutable.
#
# 5. Dictionaries preserve insertion order.
#
# 6. Dictionary keys must be hashable.
#
# 7. "in" checks keys by default.
#
# 8. Use [] when a key is expected to exist.
#
# 9. Use get() when a key may be missing.
#
# 10. A dictionary can contain lists, sets, tuples,
#     and other dictionaries as values.
#
# ============================================================


# ============================================================
# Key Takeaways
# ============================================================
#
# Dictionary:
#
#     key → value
#
# Example:
#
#     student = {
#         "name": "Alice",
#         "age": 21,
#     }
#
# Access:
#
#     student["name"]
#
# Safe access:
#
#     student.get("name")
#
# Add:
#
#     student["city"] = "Pune"
#
# Update:
#
#     student["age"] = 22
#
# Check key:
#
#     "name" in student
#
# Keys:
#
#     student.keys()
#
# Values:
#
#     student.values()
#
# Key-value pairs:
#
#     student.items()
#
# Length:
#
#     len(student)
#
# Next:
# 02_dictionary_methods.py
# ============================================================
