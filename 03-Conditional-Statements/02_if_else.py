# ============================================================
# Python Conditional Statements
# File: 02_if_else.py
# Description: Demonstrates the if-else statement in Python.
# ============================================================


# ------------------------------------------------------------
# 1. Basic if-else Statement
# ------------------------------------------------------------

age = 20

if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")


# ------------------------------------------------------------
# 2. Even or Odd Number
# ------------------------------------------------------------

number = 7

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# ------------------------------------------------------------
# 3. Pass or Fail
# ------------------------------------------------------------

marks = 75

if marks >= 40:
    print("Student has passed.")
else:
    print("Student has failed.")


# ------------------------------------------------------------
# 4. Positive or Non-Positive Number
# ------------------------------------------------------------

number = -5

if number > 0:
    print("The number is positive.")
else:
    print("The number is zero or negative.")


# ------------------------------------------------------------
# 5. String Validation
# ------------------------------------------------------------

username = "admin"

if username:
    print("Username is provided.")
else:
    print("Username is empty.")


# ------------------------------------------------------------
# 6. Practical Example
# ------------------------------------------------------------

age = 16
has_permission = True

if age >= 18 or has_permission:
    print("Access granted.")
else:
    print("Access denied.")
