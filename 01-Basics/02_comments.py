# 02_comments.py

# ============================================================
# Python Comments
# ============================================================

# A comment is ignored by Python during program execution.
# Comments are written to explain code and improve readability.

print("Hello, Python!")


# ------------------------------------------------------------
# 1. Single-Line Comment
# ------------------------------------------------------------

# This is a single-line comment.
print("This line is executed.")


# ------------------------------------------------------------
# 2. Inline Comment
# ------------------------------------------------------------

name = "Alice"  # Store the user's name
age = 25        # Store the user's age

print(name)
print(age)


# ------------------------------------------------------------
# 3. Comments for Explanation
# ------------------------------------------------------------

# Calculate the total price of two products.
price1 = 100
price2 = 200

total = price1 + price2

print("Total:", total)


# ------------------------------------------------------------
# 4. Temporarily Disabling Code
# ------------------------------------------------------------

# print("This line will not execute.")

print("The commented line above is ignored by Python.")


# ------------------------------------------------------------
# 5. Multi-Line Documentation String
# ------------------------------------------------------------

"""
This is a multi-line string.

When used as the first statement inside a module,
function, or class, it can serve as a docstring.
"""

print("Comments help make code easier to understand.")


# ------------------------------------------------------------
# Best Practice
# ------------------------------------------------------------

# Good comment:
# Convert the user's age from text to an integer.
age = int("25")

print("Age:", age)
