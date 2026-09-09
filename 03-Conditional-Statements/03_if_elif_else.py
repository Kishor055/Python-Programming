# ============================================================
# Python Conditional Statements
# File: 03_if_elif_else.py
# Description: Demonstrates if-elif-else conditional logic.
# ============================================================


# ------------------------------------------------------------
# 1. Basic if-elif-else Statement
# ------------------------------------------------------------

age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")


# ------------------------------------------------------------
# 2. Grade Classification
# ------------------------------------------------------------

marks = 85

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)


# ------------------------------------------------------------
# 3. Number Classification
# ------------------------------------------------------------

number = -10

if number > 0:
    print("Positive number.")
elif number < 0:
    print("Negative number.")
else:
    print("Zero.")


# ------------------------------------------------------------
# 4. Temperature Classification
# ------------------------------------------------------------

temperature = 32

if temperature >= 40:
    print("Extremely hot.")
elif temperature >= 30:
    print("Hot.")
elif temperature >= 20:
    print("Moderate.")
elif temperature >= 10:
    print("Cool.")
else:
    print("Cold.")


# ------------------------------------------------------------
# 5. Multiple Conditions
# ------------------------------------------------------------

score = 78

if score >= 90:
    print("Excellent performance.")
elif score >= 75:
    print("Very good performance.")
elif score >= 50:
    print("Good performance.")
else:
    print("Needs improvement.")


# ------------------------------------------------------------
# 6. Practical Example
# ------------------------------------------------------------

age = 22

if age < 13:
    category = "Child"
elif age < 20:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else:
    category = "Senior"

print("Age Category:", category)
