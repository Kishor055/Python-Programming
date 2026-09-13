"""
02_dictionary_methods.py
------------------------
Common Python Dictionary methods.

Topics covered:
    1. get()
    2. keys()
    3. values()
    4. items()
    5. update()
    6. pop()
    7. popitem()
    8. setdefault()
    9. clear()
    10. copy()
    11. fromkeys()
    12. Practical examples
"""


# ============================================================
# 1. get()
# ============================================================
# Returns the value associated with a key.
#
# If the key does not exist, get() returns None instead of
# raising a KeyError.
#
# Syntax:
#
#     dictionary.get(key)
#     dictionary.get(key, default)


student = {
    "name": "Alice",
    "age": 21,
    "course": "Python",
}

print("Name:", student.get("name"))
print("Age:", student.get("age"))

# Missing key

print("Email:", student.get("email"))


# get() with a default value

print(
    "Email:",
    student.get("email", "Not available"),
)


# ============================================================
# 2. keys()
# ============================================================
# Returns a view containing all dictionary keys.

student = {
    "name": "Alice",
    "age": 21,
    "course": "Python",
}

keys = student.keys()

print("\nKeys:", keys)


# Iterate over keys

print("Student keys:")

for key in student.keys():
    print(key)


# ============================================================
# 3. values()
# ============================================================
# Returns a view containing all dictionary values.

values = student.values()

print("\nValues:", values)


# Iterate over values

print("Student values:")

for value in student.values():
    print(value)


# ============================================================
# 4. items()
# ============================================================
# Returns a view containing key-value pairs.
#
# Each item is represented as a tuple:
#
#     (key, value)


items = student.items()

print("\nItems:", items)


# Iterate over key-value pairs

print("Student information:")

for key, value in student.items():
    print(f"{key}: {value}")


# ============================================================
# 5. update()
# ============================================================
# Adds new key-value pairs or updates existing keys.
#
# Syntax:
#
#     dictionary.update(other)


student = {
    "name": "Alice",
    "age": 21,
}

student.update({
    "course": "Python",
    "city": "Pune",
})

print("\nAfter update():")
print(student)


# Update an existing key

student.update({
    "age": 22,
})

print("After updating age:")
print(student)


# ============================================================
# 6. update() with Another Dictionary
# ============================================================

employee = {
    "name": "Alice",
    "department": "Engineering",
}

additional_data = {
    "experience": 3,
    "location": "Pune",
}

employee.update(additional_data)

print("\nUpdated employee:")
print(employee)


# ============================================================
# 7. pop()
# ============================================================
# Removes the specified key and returns its value.
#
# Syntax:
#
#     dictionary.pop(key)
#     dictionary.pop(key, default)
#
# If the key does not exist and no default is provided,
# pop() raises KeyError.


student = {
    "name": "Alice",
    "age": 21,
    "course": "Python",
}

removed_age = student.pop("age")

print("\nRemoved age:", removed_age)
print("Updated student:", student)


# pop() with a default value

email = student.pop("email", "Not available")

print("Removed email:", email)


# ============================================================
# 8. popitem()
# ============================================================
# Removes and returns the last inserted key-value pair.
#
# The returned value is a tuple:
#
#     (key, value)


student = {
    "name": "Alice",
    "age": 21,
    "course": "Python",
}

removed_item = student.popitem()

print("\nRemoved item:", removed_item)
print("Remaining dictionary:", student)


# ============================================================
# 9. setdefault()
# ============================================================
# Returns the value of a key if it exists.
#
# If the key does not exist, setdefault() inserts the key
# with the specified default value and returns that value.
#
# Syntax:
#
#     dictionary.setdefault(key)
#     dictionary.setdefault(key, default)


student = {
    "name": "Alice",
}

age = student.setdefault("age", 21)

print("\nAge:", age)
print("Student:", student)


# If the key already exists, its value is NOT replaced.

student = {
    "name": "Alice",
    "age": 21,
}

age = student.setdefault("age", 25)

print("\nExisting age:", age)
print("Student:", student)


# ============================================================
# 10. clear()
# ============================================================
# Removes all key-value pairs.

student = {
    "name": "Alice",
    "age": 21,
    "course": "Python",
}

student.clear()

print("\nAfter clear():")
print(student)


# ============================================================
# 11. copy()
# ============================================================
# Returns a shallow copy of the dictionary.


original = {
    "name": "Alice",
    "age": 21,
}

copied = original.copy()

print("\nOriginal:", original)
print("Copied:", copied)


# Modify the copy

copied["age"] = 22

print("\nAfter modifying copied dictionary:")

print("Original:", original)
print("Copied:", copied)


# ============================================================
# 12. fromkeys()
# ============================================================
# Creates a new dictionary from a sequence of keys.
#
# Syntax:
#
#     dict.fromkeys(keys)
#     dict.fromkeys(keys, value)


keys = ["name", "age", "city"]

student = dict.fromkeys(keys)

print("\nUsing fromkeys():")
print(student)


# fromkeys() with a default value

student = dict.fromkeys(keys, "Unknown")

print("With default value:")
print(student)


# ============================================================
# 13. keys(), values(), and items() Together
# ============================================================

employee = {
    "id": 1001,
    "name": "Alice",
    "department": "Engineering",
}

print("\n--- Employee Information ---")

print("Keys:")

for key in employee.keys():
    print(key)


print("\nValues:")

for value in employee.values():
    print(value)


print("\nKey-Value pairs:")

for key, value in employee.items():
    print(f"{key}: {value}")


# ============================================================
# 14. Practical Example — Product Management
# ============================================================

product = {
    "id": 101,
    "name": "Laptop",
    "price": 75000,
    "stock": 10,
}

print("\n--- Product ---")
print(product)


# Update product information

product.update({
    "price": 72000,
    "stock": 8,
})

print("After update:")
print(product)


# Safely retrieve a value

category = product.get("category", "Electronics")

print("Category:", category)


# ============================================================
# 15. Practical Example — User Profile
# ============================================================

user = {
    "username": "alice",
    "email": "alice@example.com",
}

# Add missing information

user.setdefault("age", 21)

print("\n--- User Profile ---")
print(user)


# ============================================================
# 16. Practical Example — Word Frequency
# ============================================================
# get() is particularly useful for counting occurrences.


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


# ============================================================
# 17. Practical Example — Grouping Data
# ============================================================
# setdefault() can be useful for creating groups.


students = [
    ("Alice", "Python"),
    ("Bob", "Java"),
    ("Charlie", "Python"),
    ("David", "Java"),
]

groups = {}

for name, course in students:
    groups.setdefault(course, []).append(name)

print("\n--- Students by Course ---")
print(groups)


# Expected result:
#
# {
#     "Python": ["Alice", "Charlie"],
#     "Java": ["Bob", "David"]
# }


# ============================================================
# 18. Practical Example — Remove Optional Data
# ============================================================

user = {
    "username": "alice",
    "email": "alice@example.com",
    "phone": "9876543210",
}

# Remove phone safely

phone = user.pop("phone", None)

print("\nRemoved phone:", phone)
print("Updated user:", user)


# ============================================================
# 19. Method Comparison
# ============================================================

data = {
    "name": "Alice",
    "age": 21,
}

print("\n--- Dictionary Method Summary ---")

# Retrieve
print("get():", data.get("name"))

# Keys
print("keys():", data.keys())

# Values
print("values():", data.values())

# Items
print("items():", data.items())


# ============================================================
# Dictionary Methods Quick Reference
# ============================================================
#
# get()
#     Safely retrieve a value.
#
# keys()
#     Return a view of all keys.
#
# values()
#     Return a view of all values.
#
# items()
#     Return a view of key-value pairs.
#
# update()
#     Add or update multiple entries.
#
# pop()
#     Remove a specified key and return its value.
#
# popitem()
#     Remove and return the last inserted key-value pair.
#
# setdefault()
#     Get a value or create the key with a default value.
#
# clear()
#     Remove all entries.
#
# copy()
#     Create a shallow copy.
#
# fromkeys()
#     Create a dictionary from a sequence of keys.
#
# ============================================================


# ============================================================
# Important Differences
# ============================================================
#
# get() vs []
#
#     data["key"]
#         Raises KeyError if key is missing.
#
#     data.get("key")
#         Returns None if key is missing.
#
#
# remove vs pop
#
#     Dictionary has no remove() method.
#
#     data.pop("key")
#         Removes a specific key.
#
#     data.popitem()
#         Removes the last inserted pair.
#
#
# setdefault() vs get()
#
#     get()
#         Reads a value.
#
#     setdefault()
#         Reads a value and creates the key if missing.
#
# ============================================================


# ============================================================
# Key Takeaways
# ============================================================
#
# 1. get() is useful for safe key access.
#
# 2. keys() gives dictionary keys.
#
# 3. values() gives dictionary values.
#
# 4. items() gives key-value pairs.
#
# 5. update() adds or modifies multiple entries.
#
# 6. pop() removes a specific key.
#
# 7. popitem() removes the last inserted pair.
#
# 8. setdefault() retrieves or creates a key.
#
# 9. clear() removes all entries.
#
# 10. copy() creates a shallow copy.
#
# 11. fromkeys() creates a dictionary from keys.
#
# Next:
# 03_dictionary_operations.py
# ============================================================
