# 03_variables.py

# ============================================================
# Python Variables
# ============================================================

# A variable is a name that refers to a value (object).
# Python does not require us to declare the data type
# of a variable explicitly.


# ------------------------------------------------------------
# 1. Creating Variables
# ------------------------------------------------------------

name = "Alice"
age = 25
height = 5.7
is_student = True

print(name)
print(age)
print(height)
print(is_student)


# ------------------------------------------------------------
# 2. Checking the Type of a Variable
# ------------------------------------------------------------

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


# ------------------------------------------------------------
# 3. Reassigning Variables
# ------------------------------------------------------------

score = 50

print("Before:", score)

score = 100

print("After:", score)


# ------------------------------------------------------------
# 4. Multiple Assignment
# ------------------------------------------------------------

first_name, age, city = "Alice", 25, "Pune"

print(first_name)
print(age)
print(city)


# ------------------------------------------------------------
# 5. Assigning the Same Value
# ------------------------------------------------------------

x = y = z = 0

print(x)
print(y)
print(z)


# ------------------------------------------------------------
# 6. Swapping Variables
# ------------------------------------------------------------

a = 10
b = 20

print("Before swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)


# ------------------------------------------------------------
# 7. Variable Naming
# ------------------------------------------------------------

student_name = "Alice"
student_age = 25
total_marks = 450

print(student_name)
print(student_age)
print(total_marks)


# ------------------------------------------------------------
# 8. Case-Sensitive Variables
# ------------------------------------------------------------

name = "Alice"
Name = "Bob"
NAME = "Charlie"

print(name)
print(Name)
print(NAME)


# ------------------------------------------------------------
# 9. Dynamic Typing
# ------------------------------------------------------------

value = 100

print(value)
print(type(value))

value = "Python"

print(value)
print(type(value))


# ------------------------------------------------------------
# 10. Variables Can Store Expressions
# ------------------------------------------------------------

price = 100
quantity = 3

total = price * quantity

print("Total:", total)


# ------------------------------------------------------------
# 11. Using Variables in f-Strings
# ------------------------------------------------------------

user_name = "Alice"
user_age = 25

print(f"My name is {user_name}.")
print(f"I am {user_age} years old.")


# ------------------------------------------------------------
# 12. Constants by Convention
# ------------------------------------------------------------

# Python does not enforce constants.
# Uppercase names are commonly used to indicate
# that a value should not normally be changed.

PI = 3.14159
MAX_USERS = 100

print("PI:", PI)
print("Maximum users:", MAX_USERS)
