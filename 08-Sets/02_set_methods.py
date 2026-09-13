"""
02_set_methods.py
-----------------
Common Python Set methods.

Topics covered:
    1. add()
    2. update()
    3. remove()
    4. discard()
    5. pop()
    6. clear()
    7. copy()
    8. Practical examples
"""


# ============================================================
# 1. add()
# ============================================================
# Adds a single element to the set.
#
# If the element already exists, nothing changes.

languages = {"Python", "Java"}

languages.add("C++")

print("After add():", languages)

# Adding an existing element
languages.add("Python")

print("After adding duplicate:", languages)


# ============================================================
# 2. update()
# ============================================================
# Adds multiple elements to a set.
#
# update() accepts any iterable such as:
# list, tuple, set, string, etc.

languages = {"Python", "Java"}

languages.update(["C++", "Go", "Rust"])

print("\nAfter update():", languages)


# update() with another set

backend = {"Python", "Django"}
backend.update({"FastAPI", "Flask"})

print("Backend technologies:", backend)


# ============================================================
# 3. remove()
# ============================================================
# Removes a specific element.
#
# IMPORTANT:
# If the element does not exist, remove() raises KeyError.

numbers = {10, 20, 30, 40}

numbers.remove(30)

print("\nAfter remove(30):", numbers)


# The following would raise KeyError:
#
# numbers.remove(100)


# ============================================================
# 4. discard()
# ============================================================
# Removes a specific element.
#
# Unlike remove(), discard() does NOT raise an error
# if the element does not exist.

numbers = {10, 20, 30, 40}

numbers.discard(30)

print("\nAfter discard(30):", numbers)

# No error even though 100 does not exist
numbers.discard(100)

print("After discard(100):", numbers)


# ============================================================
# 5. remove() vs discard()
# ============================================================

numbers = {10, 20, 30}

# remove() -> raises KeyError if element is missing
# discard() -> safely does nothing if element is missing

numbers.discard(100)

print("\nremove() vs discard():")
print(numbers)


# ============================================================
# 6. pop()
# ============================================================
# Removes and returns an arbitrary element.
#
# IMPORTANT:
# Sets are unordered, so do not assume which element
# will be removed.

numbers = {10, 20, 30, 40}

removed_value = numbers.pop()

print("\nRemoved value:", removed_value)
print("Remaining set:", numbers)


# ============================================================
# 7. clear()
# ============================================================
# Removes all elements from the set.

numbers = {10, 20, 30, 40}

numbers.clear()

print("\nAfter clear():", numbers)


# ============================================================
# 8. copy()
# ============================================================
# Creates a shallow copy of a set.

original = {10, 20, 30}

copied = original.copy()

print("\nOriginal:", original)
print("Copied:", copied)


# Modifying the copy does not modify the original

copied.add(40)

print("After modifying copied set:")
print("Original:", original)
print("Copied:", copied)


# ============================================================
# 9. Practical Example — Managing Skills
# ============================================================

skills = {"Python", "SQL"}

# Add one skill
skills.add("Git")

# Add multiple skills
skills.update(["Docker", "Linux"])

print("\nDeveloper skills:", skills)


# ============================================================
# 10. Practical Example — Removing Skills
# ============================================================

skills = {
    "Python",
    "SQL",
    "Git",
    "Docker",
    "Linux",
}

skills.remove("Docker")

# Safe removal
skills.discard("Java")

print("\nUpdated skills:", skills)


# ============================================================
# 11. Practical Example — User Permissions
# ============================================================

permissions = {"read", "write"}

print("\nInitial permissions:", permissions)

# Grant permission
permissions.add("delete")

print("After granting permission:", permissions)

# Grant multiple permissions
permissions.update(["upload", "download"])

print("After adding multiple permissions:", permissions)

# Revoke permission
permissions.discard("delete")

print("After revoking permission:", permissions)


# ============================================================
# 12. Practical Example — Removing Duplicates
# ============================================================

user_ids = [
    101,
    102,
    101,
    103,
    102,
    104,
    105,
]

unique_user_ids = set(user_ids)

print("\nOriginal user IDs:", user_ids)
print("Unique user IDs:", unique_user_ids)


# ============================================================
# Set Methods Quick Reference
# ============================================================
#
# add(element)
#     Add one element.
#
# update(iterable)
#     Add multiple elements.
#
# remove(element)
#     Remove element.
#     Raises KeyError if element is missing.
#
# discard(element)
#     Remove element.
#     Does not raise an error if element is missing.
#
# pop()
#     Remove and return an arbitrary element.
#
# clear()
#     Remove all elements.
#
# copy()
#     Return a shallow copy.
#
# ============================================================
# Key Takeaways
# ============================================================
#
# 1. Use add() for one element.
# 2. Use update() for multiple elements.
# 3. Use remove() when missing elements should raise an error.
# 4. Use discard() for safe removal.
# 5. pop() removes an arbitrary element.
# 6. clear() empties the entire set.
# 7. copy() creates a separate shallow copy.
#
# Next:
# 03_set_operations.py
# ============================================================
