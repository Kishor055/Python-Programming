# ============================================================
# Python Operators
# File: 06_membership_operators.py
# Description: Demonstrates Python membership operators.
# ============================================================


# ------------------------------------------------------------
# 1. Membership Operators with a List
# ------------------------------------------------------------

languages = ["Python", "Java", "C++"]

print("Python in languages:", "Python" in languages)
print("JavaScript in languages:", "JavaScript" in languages)

print("Python not in languages:", "Python" not in languages)
print("JavaScript not in languages:", "JavaScript" not in languages)


# ------------------------------------------------------------
# 2. Membership Operators with a String
# ------------------------------------------------------------

message = "Python is powerful"

print("Python in message:", "Python" in message)
print("Java in message:", "Java" in message)

print("Python not in message:", "Python" not in message)
print("Java not in message:", "Java" not in message)


# ------------------------------------------------------------
# 3. Membership Operators with a Tuple
# ------------------------------------------------------------

numbers = (10, 20, 30, 40, 50)

print("30 in numbers:", 30 in numbers)
print("100 in numbers:", 100 in numbers)


# ------------------------------------------------------------
# 4. Membership Operators with a Set
# ------------------------------------------------------------

colors = {"red", "green", "blue"}

print("red in colors:", "red" in colors)
print("yellow in colors:", "yellow" in colors)


# ------------------------------------------------------------
# 5. Membership Operators with a Dictionary
# ------------------------------------------------------------

student = {
    "name": "Alex",
    "age": 21,
    "course": "Python"
}

print("name in student:", "name" in student)
print("email in student:", "email" in student)


# ------------------------------------------------------------
# 6. Practical Example
# ------------------------------------------------------------

users = ["admin", "developer", "guest"]

username = "developer"

if username in users:
    print("User exists.")
else:
    print("User does not exist.")
