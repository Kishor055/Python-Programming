"""
03_dictionary_operations.py
---------------------------
Python Dictionary Operations.

This file covers common operations performed on dictionaries.

Topics covered:
    1. Accessing dictionary elements
    2. Adding elements
    3. Updating elements
    4. Removing elements
    5. Checking key existence
    6. Checking value existence
    7. Iterating over dictionaries
    8. Dictionary merging
    9. Dictionary unpacking
    10. Comparing dictionaries
    11. Copying dictionaries
    12. Filtering dictionary data
    13. Practical examples
"""


# ============================================================
# 1. Accessing Dictionary Elements
# ============================================================

student = {
    "name": "Alice",
    "age": 21,
    "course": "Python",
}

print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])


# Safe access

print("Email:", student.get("email", "Not available"))


# ============================================================
# 2. Adding Elements
# ============================================================
# Add a new key-value pair using:
#
#     dictionary[key] = value


student["city"] = "Pune"

print("\nAfter adding city:")
print(student)


# Add another field

student["marks"] = 92

print("After adding marks:")
print(student)


# ============================================================
# 3. Updating Elements
# ============================================================
# Existing keys are updated when a new value is assigned.

student["age"] = 22

print("\nAfter updating age:")
print(student)


# Multiple updates using update()

student.update({
    "course": "Advanced Python",
    "marks": 95,
})

print("After multiple updates:")
print(student)


# ============================================================
# 4. Removing Elements Using del
# ============================================================

student = {
    "name": "Alice",
    "age": 21,
    "course": "Python",
    "city": "Pune",
}

del student["city"]

print("\nAfter del:")
print(student)


# ============================================================
# 5. Removing Elements Using pop()
# ============================================================

student = {
    "name": "Alice",
    "age": 21,
    "course": "Python",
}

removed_age = student.pop("age")

print("\nRemoved value:", removed_age)
print("Dictionary:", student)


# ============================================================
# 6. Removing the Last Inserted Element
# ============================================================

student = {
    "name": "Alice",
    "age": 21,
    "course": "Python",
}

removed_item = student.popitem()

print("\nRemoved item:", removed_item)
print("Dictionary:", student)


# ============================================================
# 7. Removing All Elements
# ============================================================

student = {
    "name": "Alice",
    "age": 21,
}

student.clear()

print("\nAfter clear():")
print(student)


# ============================================================
# 8. Checking if a Key Exists
# ============================================================

student = {
    "name": "Alice",
    "age": 21,
}

if "name" in student:
    print("\nName key exists.")


if "email" not in student:
    print("Email key does not exist.")


# ============================================================
# 9. Checking if a Value Exists
# ============================================================
# By default, "in" checks keys.
#
# To check values, use values().


student = {
    "name": "Alice",
    "age": 21,
}

if "Alice" in student.values():
    print("\nAlice exists as a value.")


if 21 in student.values():
    print("21 exists as a value.")


# ============================================================
# 10. Iterating Over Keys
# ============================================================

student = {
    "name": "Alice",
    "age": 21,
    "course": "Python",
}

print("\n--- Keys ---")

for key in student:
    print(key)


# ============================================================
# 11. Iterating Over Values
# ============================================================

print("\n--- Values ---")

for value in student.values():
    print(value)


# ============================================================
# 12. Iterating Over Key-Value Pairs
# ============================================================

print("\n--- Key-Value Pairs ---")

for key, value in student.items():
    print(f"{key}: {value}")


# ============================================================
# 13. Dictionary Length
# ============================================================

print("\nNumber of entries:", len(student))


# ============================================================
# 14. Merging Dictionaries Using update()
# ============================================================

personal_info = {
    "name": "Alice",
    "age": 21,
}

contact_info = {
    "email": "alice@example.com",
    "phone": "9876543210",
}

personal_info.update(contact_info)

print("\nMerged dictionary:")
print(personal_info)


# ============================================================
# 15. Merging Dictionaries Using |
# ============================================================
# Python 3.9+ supports the | operator for dictionary merging.


first = {
    "name": "Alice",
    "age": 21,
}

second = {
    "city": "Pune",
    "course": "Python",
}

merged = first | second

print("\nMerged using |:")
print(merged)


# ============================================================
# 16. Dictionary Merge Behavior
# ============================================================
# If both dictionaries contain the same key,
# the value from the right-hand dictionary wins.


first = {
    "name": "Alice",
    "age": 21,
}

second = {
    "name": "Bob",
    "city": "Pune",
}

merged = first | second

print("\nMerge with duplicate key:")
print(merged)


# Result:
#
# "name" becomes "Bob"
#
# because the second dictionary is on the right side.


# ============================================================
# 17. In-Place Dictionary Merge Using |=
# ============================================================
# Python 3.9+


student = {
    "name": "Alice",
    "age": 21,
}

additional_data = {
    "course": "Python",
    "city": "Pune",
}

student |= additional_data

print("\nAfter |=:")
print(student)


# ============================================================
# 18. Dictionary Unpacking with **
# ============================================================
# ** can unpack dictionary key-value pairs.


personal = {
    "name": "Alice",
    "age": 21,
}

contact = {
    "email": "alice@example.com",
}

user = {
    **personal,
    **contact,
}

print("\nDictionary unpacking:")
print(user)


# ============================================================
# 19. Dictionary Unpacking with Duplicate Keys
# ============================================================

first = {
    "name": "Alice",
    "age": 21,
}

second = {
    "name": "Bob",
    "city": "Pune",
}

result = {
    **first,
    **second,
}

print("\nUnpacking with duplicate key:")
print(result)


# ============================================================
# 20. Comparing Dictionaries
# ============================================================
# Dictionaries can be compared using:
#
#     ==
#     !=
#
# Equality depends on the key-value pairs.


first = {
    "name": "Alice",
    "age": 21,
}

second = {
    "name": "Alice",
    "age": 21,
}

print("\nAre dictionaries equal?")
print(first == second)


# Different data

third = {
    "name": "Bob",
    "age": 21,
}

print("First == Third:", first == third)
print("First != Third:", first != third)


# ============================================================
# 21. Dictionary Order and Equality
# ============================================================
# Dictionary equality does NOT depend on insertion order.


first = {
    "name": "Alice",
    "age": 21,
}

second = {
    "age": 21,
    "name": "Alice",
}

print("\nSame data, different insertion order:")
print(first == second)


# ============================================================
# 22. Copying a Dictionary
# ============================================================

original = {
    "name": "Alice",
    "age": 21,
}

copied = original.copy()

copied["age"] = 22

print("\nOriginal:")
print(original)

print("Copied:")
print(copied)


# ============================================================
# 23. Filtering Dictionary Data
# ============================================================
# We can create a new dictionary containing only entries
# that satisfy a condition.


marks = {
    "Alice": 92,
    "Bob": 75,
    "Charlie": 88,
    "David": 65,
}

passed_students = {}

for name, score in marks.items():
    if score >= 80:
        passed_students[name] = score

print("\nStudents scoring 80 or above:")
print(passed_students)


# ============================================================
# 24. Finding the Highest Value
# ============================================================

marks = {
    "Alice": 92,
    "Bob": 75,
    "Charlie": 88,
    "David": 65,
}

highest_score = max(marks.values())

print("\nHighest score:", highest_score)


# Find the student with the highest score

top_student = max(
    marks,
    key=marks.get,
)

print("Top student:", top_student)
print("Top score:", marks[top_student])


# ============================================================
# 25. Finding the Lowest Value
# ============================================================

lowest_score = min(marks.values())

print("\nLowest score:", lowest_score)


lowest_student = min(
    marks,
    key=marks.get,
)

print("Lowest student:", lowest_student)
print("Lowest score:", marks[lowest_student])


# ============================================================
# 26. Sorting Dictionary Keys
# ============================================================

marks = {
    "Charlie": 88,
    "Alice": 92,
    "David": 65,
    "Bob": 75,
}

sorted_names = sorted(marks)

print("\nSorted keys:")
print(sorted_names)


# ============================================================
# 27. Sorting by Dictionary Values
# ============================================================
# sorted() returns a list.


sorted_by_marks = sorted(
    marks.items(),
    key=lambda item: item[1],
)

print("\nSorted by marks:")
print(sorted_by_marks)


# ============================================================
# 28. Sorting in Descending Order
# ============================================================

sorted_by_marks = sorted(
    marks.items(),
    key=lambda item: item[1],
    reverse=True,
)

print("\nHighest to lowest:")
print(sorted_by_marks)


# ============================================================
# 29. Practical Example — Shopping Cart
# ============================================================

cart = {
    "Laptop": 1,
    "Mouse": 2,
    "Keyboard": 1,
}

print("\n--- Shopping Cart ---")

for product, quantity in cart.items():
    print(f"{product}: {quantity}")


# Add product

cart["Monitor"] = 1

# Update quantity

cart["Mouse"] += 1

print("\nUpdated cart:")
print(cart)


# Remove product

cart.pop("Keyboard")

print("After removing Keyboard:")
print(cart)


# ============================================================
# 30. Practical Example — Employee Data
# ============================================================

employee = {
    "id": 1001,
    "name": "Alice",
    "department": "Engineering",
    "salary": 75000,
}

# Increase salary

employee["salary"] += 5000

# Add experience

employee["experience"] = 3

print("\n--- Employee ---")
print(employee)


# ============================================================
# 31. Practical Example — Inventory
# ============================================================

inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15,
}

# Sell two laptops

inventory["Laptop"] -= 2

# Add new product

inventory["Monitor"] = 8

print("\n--- Inventory ---")
print(inventory)


# Check stock

if inventory.get("Laptop", 0) > 0:
    print("Laptop is available.")


# ============================================================
# 32. Practical Example — Student Marks
# ============================================================

students = {
    "Alice": 92,
    "Bob": 78,
    "Charlie": 85,
    "David": 65,
}

print("\n--- Student Results ---")

for name, marks in students.items():

    if marks >= 80:
        result = "Excellent"
    elif marks >= 60:
        result = "Pass"
    else:
        result = "Needs Improvement"

    print(f"{name}: {marks} - {result}")


# ============================================================
# 33. Practical Example — Counting Characters
# ============================================================

text = "programming"

character_count = {}

for character in text:
    character_count[character] = (
        character_count.get(character, 0) + 1
    )

print("\n--- Character Frequency ---")
print(character_count)


# ============================================================
# 34. Practical Example — Combining User Data
# ============================================================

profile = {
    "username": "alice",
    "age": 21,
}

preferences = {
    "theme": "dark",
    "language": "English",
}

user = profile | preferences

print("\n--- User ---")
print(user)


# ============================================================
# 35. Important Dictionary Operations
# ============================================================
#
# Access:
#
#     data[key]
#
# Safe access:
#
#     data.get(key)
#
# Add:
#
#     data[key] = value
#
# Update:
#
#     data.update(other)
#
# Remove:
#
#     data.pop(key)
#
# Remove last:
#
#     data.popitem()
#
# Delete:
#
#     del data[key]
#
# Clear:
#
#     data.clear()
#
# Check key:
#
#     key in data
#
# Check value:
#
#     value in data.values()
#
# Merge:
#
#     first | second
#
# In-place merge:
#
#     first |= second
#
# Copy:
#
#     data.copy()
#
# Iterate:
#
#     for key, value in data.items():
#
# ============================================================


# ============================================================
# Key Takeaways
# ============================================================
#
# 1. Dictionaries are mutable key-value collections.
#
# 2. New data can be added using:
#
#       dictionary[key] = value
#
# 3. Existing data can be updated using assignment or
#    update().
#
# 4. pop(), popitem(), del, and clear() remove data.
#
# 5. "in" checks dictionary keys.
#
# 6. values() can be used to check dictionary values.
#
# 7. Dictionaries can be merged using update(), |, or **.
#
# 8. Dictionary equality compares their key-value data,
#    regardless of insertion order.
#
# 9. sorted() can be used to sort dictionary keys or items.
#
# 10. Dictionaries are commonly used for structured data,
#     configuration, lookup tables, counters, and records.
#
# Next:
# 04_dictionary_comprehension.py
# ============================================================
