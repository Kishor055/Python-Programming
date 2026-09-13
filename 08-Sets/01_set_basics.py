"""
01_set_basics.py
----------------
Introduction to Python Sets.

A set is an unordered collection of unique and hashable elements.

Topics covered:
    1. Creating a set
    2. Duplicate values
    3. Creating an empty set
    4. Checking the type
    5. Set length
    6. Membership testing
    7. Iterating over a set
    8. Creating a set from other iterables
"""


# ============================================================
# 1. Creating a Set
# ============================================================

numbers = {10, 20, 30, 40}

print("Set:", numbers)


# ============================================================
# 2. Sets Automatically Remove Duplicates
# ============================================================

numbers = {10, 20, 20, 30, 30, 40}

print("Duplicates removed:", numbers)


# ============================================================
# 3. Creating a Set from a List
# ============================================================

numbers_list = [10, 20, 20, 30, 30, 40]

unique_numbers = set(numbers_list)

print("Original list:", numbers_list)
print("Converted set:", unique_numbers)


# ============================================================
# 4. Creating a Set from a String
# ============================================================

text = "programming"

characters = set(text)

print("String:", text)
print("Unique characters:", characters)


# ============================================================
# 5. Empty Set
# ============================================================

# IMPORTANT:
# {} creates an empty dictionary, NOT an empty set.

empty_dictionary = {}

empty_set = set()

print("Empty dictionary:", empty_dictionary)
print("Empty set:", empty_set)

print("Type of {}:", type(empty_dictionary))
print("Type of set():", type(empty_set))


# ============================================================
# 6. Checking the Type of a Set
# ============================================================

languages = {"Python", "Java", "C++"}

print("Languages:", languages)
print("Type:", type(languages))


# ============================================================
# 7. Finding the Number of Elements
# ============================================================

numbers = {10, 20, 30, 40, 50}

print("Number of elements:", len(numbers))


# ============================================================
# 8. Membership Testing
# ============================================================

languages = {"Python", "Java", "C++"}

print("Python in set:", "Python" in languages)
print("Ruby in set:", "Ruby" in languages)

print("Ruby not in set:", "Ruby" not in languages)


# ============================================================
# 9. Iterating Over a Set
# ============================================================

languages = {"Python", "Java", "C++"}

print("\nLanguages:")

for language in languages:
    print(language)


# ============================================================
# 10. Set with Different Data Types
# ============================================================

data = {
    100,
    3.14,
    "Python",
    True,
}

print("\nMixed data types:", data)


# ============================================================
# 11. Important: Sets Are Unordered
# ============================================================

numbers = {1, 2, 3, 4, 5}

# Do not rely on the order in which elements are displayed
# or iterated over.

print("\nSet:", numbers)

for number in numbers:
    print(number)


# ============================================================
# 12. Sets Do Not Support Indexing
# ============================================================

numbers = {10, 20, 30}

# The following is invalid:
#
# print(numbers[0])
#
# Sets do not support indexing because they are unordered.


# ============================================================
# 13. Practical Example — Remove Duplicate User IDs
# ============================================================

user_ids = [101, 102, 101, 103, 102, 104, 105]

unique_user_ids = set(user_ids)

print("\nUser IDs:", user_ids)
print("Unique User IDs:", unique_user_ids)


# ============================================================
# 14. Practical Example — Unique Skills
# ============================================================

skills = [
    "Python",
    "Git",
    "SQL",
    "Python",
    "Docker",
    "Git",
]

unique_skills = set(skills)

print("\nSkills:", skills)
print("Unique skills:", unique_skills)


# ============================================================
# Key Takeaways
# ============================================================
#
# 1. Sets store unique elements.
# 2. Sets are unordered.
# 3. Sets do not support indexing or slicing.
# 4. Duplicate values are automatically removed.
# 5. Use set() to create an empty set.
# 6. Set elements must be hashable.
# 7. Use "in" and "not in" for membership testing.
# 8. Use len() to find the number of elements.
#
# Next:
# 02_set_methods.py
# ============================================================
