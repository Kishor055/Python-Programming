# ============================================================
# Python Conditional Statements
# File: 04_nested_if.py
# Description: Demonstrates nested if statements in Python.
# ============================================================


# ------------------------------------------------------------
# 1. Basic Nested if
# ------------------------------------------------------------

age = 25

if age >= 18:
    print("You are an adult.")

    if age >= 21:
        print("You are eligible for additional privileges.")


# ------------------------------------------------------------
# 2. Nested if-else
# ------------------------------------------------------------

age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")


# ------------------------------------------------------------
# 3. Nested Conditions with Login
# ------------------------------------------------------------

username = "admin"
password = "python123"

if username == "admin":
    print("Username verified.")

    if password == "python123":
        print("Login successful.")
    else:
        print("Incorrect password.")
else:
    print("Invalid username.")


# ------------------------------------------------------------
# 4. Nested if with Multiple Conditions
# ------------------------------------------------------------

age = 22
has_id = True
has_ticket = True

if age >= 18:
    print("Age requirement satisfied.")

    if has_id:
        print("Identity verified.")

        if has_ticket:
            print("Entry allowed.")
        else:
            print("Ticket required.")
    else:
        print("Valid ID required.")
else:
    print("You must be 18 or older.")


# ------------------------------------------------------------
# 5. Nested if for Student Eligibility
# ------------------------------------------------------------

marks = 85
attendance = 90

if marks >= 40:
    print("Minimum marks requirement satisfied.")

    if attendance >= 75:
        print("Attendance requirement satisfied.")
        print("Student is eligible.")
    else:
        print("Insufficient attendance.")
else:
    print("Student has failed.")


# ------------------------------------------------------------
# 6. Practical Example
# ------------------------------------------------------------

user_role = "admin"
is_authenticated = True
is_active = True

if is_authenticated:
    print("User authenticated.")

    if is_active:
        print("Account is active.")

        if user_role == "admin":
            print("Admin access granted.")
        else:
            print("Standard user access granted.")
    else:
        print("Account is inactive.")
else:
    print("Authentication required.")
