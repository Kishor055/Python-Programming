# ============================================================
# Python Conditional Statements
# File: 01_if_statement.py
# Description: Demonstrates the basic if statement in Python.
# ============================================================


# ------------------------------------------------------------
# 1. Basic if Statement
# ------------------------------------------------------------

age = 20

if age >= 18:
    print("Eligible to vote.")


# ------------------------------------------------------------
# 2. if Statement with a Number
# ------------------------------------------------------------

number = 10

if number > 0:
    print("The number is positive.")


# ------------------------------------------------------------
# 3. if Statement with a String
# ------------------------------------------------------------

name = "Alex"

if name:
    print("Name is provided.")


# ------------------------------------------------------------
# 4. if Statement with Comparison
# ------------------------------------------------------------

marks = 85

if marks >= 40:
    print("Student has passed.")


# ------------------------------------------------------------
# 5. if Statement with Logical Operator
# ------------------------------------------------------------

age = 25
has_id = True

if age >= 18 and has_id:
    print("Entry allowed.")


# ------------------------------------------------------------
# 6. Practical Example
# ------------------------------------------------------------

temperature = 35

if temperature > 30:
    print("It's a hot day.")
