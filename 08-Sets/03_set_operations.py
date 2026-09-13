"""
03_set_operations.py
---------------------
Python Set Operations.

Set operations allow us to compare and combine collections
of unique elements.

Topics covered:
    1. Union
    2. Intersection
    3. Difference
    4. Symmetric Difference
    5. Subset
    6. Superset
    7. Proper Subset
    8. Proper Superset
    9. Disjoint Sets
    10. Set operation methods
    11. Practical examples
"""


# ============================================================
# Basic Sets
# ============================================================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Set A:", A)
print("Set B:", B)


# ============================================================
# 1. UNION
# ============================================================
# Union combines all unique elements from both sets.
#
# Operator:
#     A | B
#
# Method:
#     A.union(B)
#
# Mathematical notation:
#     A ∪ B
#
# Example:
#
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
#
# A ∪ B = {1, 2, 3, 4, 5, 6}


union_result = A | B

print("\n--- Union ---")
print("A | B:", union_result)

union_result = A.union(B)

print("A.union(B):", union_result)


# ============================================================
# 2. INTERSECTION
# ============================================================
# Intersection returns elements that exist in BOTH sets.
#
# Operator:
#     A & B
#
# Method:
#     A.intersection(B)
#
# Mathematical notation:
#     A ∩ B


intersection_result = A & B

print("\n--- Intersection ---")
print("A & B:", intersection_result)

intersection_result = A.intersection(B)

print("A.intersection(B):", intersection_result)


# ============================================================
# 3. DIFFERENCE
# ============================================================
# Difference returns elements that exist in the first set
# but NOT in the second set.
#
# Operator:
#     A - B
#
# Method:
#     A.difference(B)
#
# IMPORTANT:
# Difference is directional.
#
# A - B is not necessarily equal to B - A.


difference_A_B = A - B
difference_B_A = B - A

print("\n--- Difference ---")
print("A - B:", difference_A_B)
print("B - A:", difference_B_A)


# Using the method

difference_result = A.difference(B)

print("A.difference(B):", difference_result)


# ============================================================
# 4. SYMMETRIC DIFFERENCE
# ============================================================
# Symmetric difference returns elements that exist in
# either set, but NOT in both sets.
#
# Operator:
#     A ^ B
#
# Method:
#     A.symmetric_difference(B)
#
# Mathematical notation:
#     A △ B
#
# Example:
#
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
#
# Result:
# {1, 2, 5, 6}


symmetric_difference_result = A ^ B

print("\n--- Symmetric Difference ---")
print("A ^ B:", symmetric_difference_result)

symmetric_difference_result = A.symmetric_difference(B)

print(
    "A.symmetric_difference(B):",
    symmetric_difference_result,
)


# ============================================================
# 5. SUBSET
# ============================================================
# A set is a subset of another set if every element of the
# first set exists in the second set.
#
# Method:
#     A.issubset(B)
#
# Operator:
#     A <= B


small_set = {1, 2}
large_set = {1, 2, 3, 4, 5}

print("\n--- Subset ---")

print(
    "small_set.issubset(large_set):",
    small_set.issubset(large_set),
)

print(
    "small_set <= large_set:",
    small_set <= large_set,
)


# ============================================================
# 6. PROPER SUBSET
# ============================================================
# A proper subset contains fewer elements than the other set.
#
# Operator:
#     A < B
#
# A proper subset cannot be equal to B.


A = {1, 2}
B = {1, 2, 3}

print("\n--- Proper Subset ---")
print("A < B:", A < B)


# ============================================================
# 7. SUPERSET
# ============================================================
# A set is a superset if it contains every element
# of another set.
#
# Method:
#     A.issuperset(B)
#
# Operator:
#     A >= B


A = {1, 2, 3, 4, 5}
B = {1, 2}

print("\n--- Superset ---")

print(
    "A.issuperset(B):",
    A.issuperset(B),
)

print(
    "A >= B:",
    A >= B,
)


# ============================================================
# 8. PROPER SUPERSET
# ============================================================
# A proper superset contains all elements of another set
# and has additional elements.
#
# Operator:
#     A > B


A = {1, 2, 3}
B = {1, 2}

print("\n--- Proper Superset ---")
print("A > B:", A > B)


# ============================================================
# 9. DISJOINT SETS
# ============================================================
# Two sets are disjoint if they have NO elements in common.
#
# Method:
#     A.isdisjoint(B)


A = {1, 2, 3}
B = {4, 5, 6}

print("\n--- Disjoint Sets ---")
print("A.isdisjoint(B):", A.isdisjoint(B))


# Sets with common elements

A = {1, 2, 3}
B = {3, 4, 5}

print("A.isdisjoint(B):", A.isdisjoint(B))


# ============================================================
# 10. UNION WITH MULTIPLE SETS
# ============================================================

A = {1, 2}
B = {2, 3}
C = {3, 4}

result = A | B | C

print("\n--- Multiple Set Union ---")
print("A | B | C:", result)


# Using the method

result = A.union(B, C)

print("A.union(B, C):", result)


# ============================================================
# 11. INTERSECTION WITH MULTIPLE SETS
# ============================================================

A = {1, 2, 3, 4}
B = {2, 3, 4, 5}
C = {3, 4, 5, 6}

result = A & B & C

print("\n--- Multiple Set Intersection ---")
print("A & B & C:", result)


# Using the method

result = A.intersection(B, C)

print("A.intersection(B, C):", result)


# ============================================================
# 12. SET OPERATION CHEAT SHEET
# ============================================================
#
# ┌──────────────────────────┬──────────┬──────────────────────┐
# │ Operation                │ Operator │ Method               │
# ├──────────────────────────┼──────────┼──────────────────────┤
# │ Union                    │ A | B    │ A.union(B)           │
# │ Intersection             │ A & B    │ A.intersection(B)    │
# │ Difference               │ A - B    │ A.difference(B)      │
# │ Symmetric Difference     │ A ^ B    │ A.symmetric_difference│
# │ Subset                   │ A <= B   │ A.issubset(B)        │
# │ Proper Subset            │ A < B    │ —                    │
# │ Superset                 │ A >= B   │ A.issuperset(B)      │
# │ Proper Superset          │ A > B    │ —                    │
# │ Disjoint                 │ —        │ A.isdisjoint(B)      │
# └──────────────────────────┴──────────┴──────────────────────┘


# ============================================================
# 13. Practical Example — Developer Skills
# ============================================================

frontend_skills = {
    "HTML",
    "CSS",
    "JavaScript",
    "Git",
}

backend_skills = {
    "Python",
    "Django",
    "SQL",
    "Git",
}


# Skills shared by both developers

common_skills = frontend_skills & backend_skills

print("\n--- Developer Skills ---")
print("Common skills:", common_skills)


# Skills unique to frontend

frontend_only = frontend_skills - backend_skills

print("Frontend only:", frontend_only)


# Skills unique to backend

backend_only = backend_skills - frontend_skills

print("Backend only:", backend_only)


# All skills

all_skills = frontend_skills | backend_skills

print("All skills:", all_skills)


# ============================================================
# 14. Practical Example — Course Completion
# ============================================================

required_topics = {
    "Variables",
    "Lists",
    "Tuples",
    "Sets",
    "Dictionaries",
}

completed_topics = {
    "Variables",
    "Lists",
    "Sets",
}


# Find incomplete topics

incomplete_topics = required_topics - completed_topics

print("\n--- Course Progress ---")
print("Required topics:", required_topics)
print("Completed topics:", completed_topics)
print("Incomplete topics:", incomplete_topics)


# Check whether all topics are completed

if required_topics.issubset(completed_topics):
    print("Course completed!")
else:
    print("Course is still in progress.")


# ============================================================
# 15. Practical Example — User Permissions
# ============================================================

required_permissions = {
    "read",
    "write",
}

user_permissions = {
    "read",
    "write",
    "delete",
    "download",
}


if required_permissions.issubset(user_permissions):
    print("\nAccess granted.")
else:
    print("\nAccess denied.")


# Find extra permissions

extra_permissions = user_permissions - required_permissions

print("Extra permissions:", extra_permissions)


# ============================================================
# 16. Practical Example — Compare Two Groups
# ============================================================

python_students = {
    "Alice",
    "Bob",
    "Charlie",
    "David",
}

sql_students = {
    "Bob",
    "David",
    "Eve",
    "Frank",
}


print("\n--- Student Groups ---")

# Students taking both courses
both_courses = python_students & sql_students

print("Students in both courses:", both_courses)


# Students taking only Python
python_only = python_students - sql_students

print("Python only:", python_only)


# Students taking only SQL
sql_only = sql_students - python_students

print("SQL only:", sql_only)


# Students taking at least one course
at_least_one = python_students | sql_students

print("At least one course:", at_least_one)


# ============================================================
# 17. Immutable Set Operations
# ============================================================
# Set operators return a NEW set.
# The original sets are not modified.

A = {1, 2, 3}
B = {3, 4, 5}

result = A | B

print("\n--- Original Sets ---")
print("A:", A)
print("B:", B)
print("Result:", result)


# ============================================================
# Key Takeaways
# ============================================================
#
# 1. Union combines unique elements from sets.
#
#       A | B
#
# 2. Intersection finds common elements.
#
#       A & B
#
# 3. Difference finds elements present in one set
#    but not the other.
#
#       A - B
#
# 4. Symmetric difference finds elements present in
#    either set but not both.
#
#       A ^ B
#
# 5. Subset checks whether all elements exist in another set.
#
#       A <= B
#
# 6. Superset checks whether a set contains another set.
#
#       A >= B
#
# 7. Proper subset uses <.
#
# 8. Proper superset uses >.
#
# 9. isdisjoint() checks whether two sets have no common
#    elements.
#
# 10. Set operations are extremely useful for comparing,
#     filtering, and combining collections of unique data.
#
# Next:
# 04_set_comprehension.py
# ============================================================
