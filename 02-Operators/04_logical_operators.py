# ============================================================
# Python Operators
# File: 04_logical_operators.py
# Description: Demonstrates Python logical operators.
# ============================================================


# ------------------------------------------------------------
# Variables
# ------------------------------------------------------------

age = 25
has_id = True


# ------------------------------------------------------------
# 1. Logical AND (and)
# ------------------------------------------------------------

result = age >= 18 and has_id

print("Logical AND:", result)


# ------------------------------------------------------------
# 2. Logical OR (or)
# ------------------------------------------------------------

result = age < 18 or has_id

print("Logical OR:", result)


# ------------------------------------------------------------
# 3. Logical NOT (not)
# ------------------------------------------------------------

result = not has_id

print("Logical NOT:", result)


# ------------------------------------------------------------
# 4. Combining Logical Operators
# ------------------------------------------------------------

marks = 85
attendance = 90

passed = marks >= 40 and attendance >= 75

print("Passed:", passed)


# ------------------------------------------------------------
# 5. Logical Operators with Conditions
# ------------------------------------------------------------

username = "admin"
password = "python123"

is_valid_user = username == "admin"
is_valid_password = password == "python123"

login_successful = is_valid_user and is_valid_password

print("Login Successful:", login_successful)
