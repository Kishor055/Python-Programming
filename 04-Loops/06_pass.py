"""
04-Loops/06_pass.py
===================

Python pass Statement

The `pass` statement is a null operation.
It does nothing when executed.

It is mainly used as a placeholder when Python syntax
requires a statement but you do not want to execute
any code yet.

Syntax:

    pass

Key difference:

    pass
        -> Does nothing and continues normally.

    continue
        -> Skips the rest of the current loop iteration.

    break
        -> Terminates the loop completely.
"""


# ============================================================
# 1. BASIC PASS
# ============================================================

pass


# ============================================================
# 2. PASS IN AN IF STATEMENT
# ============================================================

number = 10

if number > 0:
    pass


# ============================================================
# 3. PASS IN AN ELSE BLOCK
# ============================================================

number = 10

if number > 0:
    print("Positive number")
else:
    pass


# ============================================================
# 4. PASS IN A FOR LOOP
# ============================================================

for number in range(5):
    pass


# ============================================================
# 5. PASS IN A WHILE LOOP
# ============================================================

counter = 0

while counter < 5:
    pass
    counter += 1


# ============================================================
# 6. PASS WITH CONDITION
# ============================================================

for number in range(1, 6):

    if number == 3:
        pass

    print(number)


# `pass` does not skip the print statement.
# Output:
#
# 1
# 2
# 3
# 4
# 5


# ============================================================
# 7. PASS VS CONTINUE
# ============================================================

for number in range(1, 6):

    if number == 3:
        pass

    print("PASS:", number)


for number in range(1, 6):

    if number == 3:
        continue

    print("CONTINUE:", number)


# `pass`:
#     Does nothing.
#
# `continue`:
#     Skips the remaining code in the iteration.


# ============================================================
# 8. PASS VS BREAK
# ============================================================

for number in range(1, 6):

    if number == 3:
        pass

    print("PASS:", number)


for number in range(1, 6):

    if number == 3:
        break

    print("BREAK:", number)


# `pass` keeps the loop running.
#
# `break` terminates the loop.


# ============================================================
# 9. PASS IN NESTED LOOP
# ============================================================

for row in range(3):

    for column in range(3):

        if row == column:
            pass

        print(row, column)


# ============================================================
# 10. PASS AS A PLACEHOLDER
# ============================================================

for number in range(1, 11):

    if number % 2 == 0:
        pass
    else:
        print(number)


# ============================================================
# 11. PASS FOR FUTURE IMPLEMENTATION
# ============================================================

def calculate_salary():
    pass


# The function is syntactically valid but currently
# contains no implementation.


# ============================================================
# 12. EMPTY FUNCTION WITHOUT PASS
# ============================================================

# This is invalid Python:
#
# def calculate_tax():
#
# Python requires an indented statement inside the function.


# Correct:

def calculate_tax():
    pass


# ============================================================
# 13. EMPTY CLASS WITH PASS
# ============================================================

class Employee:
    pass


# ============================================================
# 14. EMPTY EXCEPTION CLASS
# ============================================================

class InvalidUserError(Exception):
    pass


# ============================================================
# 15. PASS IN CLASS BODY
# ============================================================

class Student:
    pass


student = Student()


# ============================================================
# 16. PASS WITH CLASS ATTRIBUTE
# ============================================================

class Product:

    name = "Unknown"

    pass


# ============================================================
# 17. PASS IN TRY BLOCK
# ============================================================

try:
    number = int("10")

except ValueError:
    pass


# ============================================================
# 18. PASS IN EXCEPT BLOCK
# ============================================================

try:
    number = int("Python")

except ValueError:
    pass


# ============================================================
# 19. PASS IN FINALLY BLOCK
# ============================================================

try:
    number = 10

finally:
    pass


# ============================================================
# 20. PASS IN MULTIPLE EXCEPTION HANDLERS
# ============================================================

try:
    number = int("10")

except ValueError:
    pass

except TypeError:
    pass


# ============================================================
# 21. PASS WITH USER VALIDATION
# ============================================================

username = ""

if not username:
    pass
else:
    print("Username is valid")


# ============================================================
# 22. PASS WITH STATUS CHECK
# ============================================================

status = "pending"

if status == "pending":
    pass
elif status == "completed":
    print("Completed")
else:
    print("Unknown status")


# ============================================================
# 23. PASS FOR UNIMPLEMENTED CASE
# ============================================================

operation = "multiply"

if operation == "add":
    print("Addition")

elif operation == "subtract":
    print("Subtraction")

elif operation == "multiply":
    pass


# ============================================================
# 24. PASS IN MENU OPTIONS
# ============================================================

choice = 2

if choice == 1:
    print("Create")

elif choice == 2:
    pass

elif choice == 3:
    print("Exit")


# ============================================================
# 25. PASS IN FOR LOOP FOR FUTURE LOGIC
# ============================================================

users = [
    "Amit",
    "Rahul",
    "Kishor"
]

for user in users:

    if user == "Rahul":
        pass
    else:
        print(user)


# ============================================================
# 26. PASS WITH MULTIPLE CONDITIONS
# ============================================================

number = 20

if number > 10:

    if number < 30:
        pass


# ============================================================
# 27. PASS IN NESTED IF
# ============================================================

age = 25

if age >= 18:

    if age <= 60:
        pass

    else:
        print("Senior citizen")

else:
    print("Minor")


# ============================================================
# 28. PASS WITH FOR-ELSE
# ============================================================

for number in range(5):

    if number == 2:
        pass

else:
    print("Loop completed")


# `pass` does not affect the completion of the loop.


# ============================================================
# 29. PASS WITH WHILE-ELSE
# ============================================================

counter = 0

while counter < 3:

    pass

    counter += 1

else:
    print("While loop completed")


# ============================================================
# 30. PASS IN NESTED CONDITIONS
# ============================================================

numbers = [1, 2, 3, 4, 5]

for number in numbers:

    if number % 2 == 0:

        if number == 2:
            pass

        print("Even:", number)


# ============================================================
# 31. PASS DOES NOT SKIP EXECUTION
# ============================================================

for number in range(1, 6):

    if number == 3:
        pass

    print("Number:", number)


# Output:
#
# Number: 1
# Number: 2
# Number: 3
# Number: 4
# Number: 5


# ============================================================
# 32. PASS DOES NOT STOP EXECUTION
# ============================================================

print("Before")

pass

print("After")


# ============================================================
# 33. PASS AS A PLACEHOLDER IN A LOOP
# ============================================================

for item in ["A", "B", "C"]:
    pass


# Useful when loop logic will be added later.


# ============================================================
# 34. PASS AS A PLACEHOLDER IN A FUNCTION
# ============================================================

def process_data(data):
    pass


# ============================================================
# 35. PASS AS A PLACEHOLDER IN A CLASS
# ============================================================

class Database:
    pass


# ============================================================
# 36. PASS FOR ABSTRACT-STYLE PLACEHOLDER
# ============================================================

class PaymentService:

    def process_payment(self):
        pass


# For a real abstract interface, prefer the `abc` module
# and `@abstractmethod` when appropriate.


# ============================================================
# 37. PASS IN CUSTOM EXCEPTION
# ============================================================

class AuthenticationError(Exception):
    pass


# ============================================================
# 38. PASS WITH EMPTY EXCEPTION HANDLING
# ============================================================

try:
    result = 10 / 2

except ZeroDivisionError:
    pass


# ============================================================
# 39. PASS WITH OPTIONAL FEATURE
# ============================================================

feature_enabled = False

if feature_enabled:
    print("Feature enabled")
else:
    pass


# ============================================================
# 40. PASS WITH DEBUG CODE
# ============================================================

debug = False

if debug:
    pass


# ============================================================
# 41. PASS IN A LOOP FOR SELECTIVE FUTURE PROCESSING
# ============================================================

tasks = [
    "Task 1",
    "Task 2",
    "Task 3"
]

for task in tasks:

    if task == "Task 2":
        pass

    print(task)


# ============================================================
# 42. PASS WITH DATA FILTER PLACEHOLDER
# ============================================================

data = [10, 20, 30, 40]

for value in data:

    if value > 25:
        pass
    else:
        print(value)


# ============================================================
# 43. PASS WITH DICTIONARY
# ============================================================

student = {
    "name": "Kishor",
    "age": 25
}

if "email" not in student:
    pass


# ============================================================
# 44. PASS WITH LIST
# ============================================================

numbers = [1, 2, 3, 4, 5]

if not numbers:
    pass


# ============================================================
# 45. PASS WITH STRING
# ============================================================

text = "Python"

if not text:
    pass


# ============================================================
# 46. PASS IN MATCH-CASE
# ============================================================

command = "unknown"

match command:

    case "start":
        print("Starting")

    case "stop":
        print("Stopping")

    case _:
        pass


# ============================================================
# 47. PASS IN MATCH-CASE PLACEHOLDER
# ============================================================

value = 10

match value:

    case 1:
        print("One")

    case 2:
        print("Two")

    case 10:
        pass

    case _:
        print("Other")


# ============================================================
# 48. PASS WITH LAMBDA IS NOT NEEDED
# ============================================================

# Lambda expressions already require an expression.
#
# This is invalid:
#
# lambda: pass
#
# Use a normal function with `pass` if you need
# an intentionally empty callable.


def empty_function():
    pass


# ============================================================
# 49. PASS IN DEVELOPMENT CODE
# ============================================================

def login():
    pass


def logout():
    pass


def register():
    pass


# These functions can be implemented later without
# causing a syntax error.


# ============================================================
# 50. PASS FOR RAPID PROTOTYPING
# ============================================================

class Application:

    def start(self):
        pass

    def stop(self):
        pass

    def restart(self):
        pass


# ============================================================
# 51. PASS WITH TODO COMMENTS
# ============================================================

def calculate_discount(price):
    # TODO: Implement discount calculation.
    pass


# ============================================================
# 52. PASS WITH MULTIPLE TODO METHODS
# ============================================================

class ShoppingCart:

    def add_item(self, item):
        # TODO: Implement item addition.
        pass

    def remove_item(self, item):
        # TODO: Implement item removal.
        pass

    def calculate_total(self):
        # TODO: Implement total calculation.
        pass


# ============================================================
# 53. PASS IN EXCEPTION HANDLING
# ============================================================

values = ["10", "20", "Python", "30"]

for value in values:

    try:
        number = int(value)

    except ValueError:
        pass

    else:
        print(number)


# ============================================================
# 54. PASS VS CONTINUE — PRACTICAL EXAMPLE
# ============================================================

numbers = [1, 2, 3, 4, 5]

for number in numbers:

    if number == 3:
        pass

    print("PASS:", number)


for number in numbers:

    if number == 3:
        continue

    print("CONTINUE:", number)


# PASS:
#     1 2 3 4 5
#
# CONTINUE:
#     1 2 4 5


# ============================================================
# 55. PASS VS BREAK — PRACTICAL EXAMPLE
# ============================================================

numbers = [1, 2, 3, 4, 5]

for number in numbers:

    if number == 3:
        pass

    print("PASS:", number)


for number in numbers:

    if number == 3:
        break

    print("BREAK:", number)


# PASS:
#     1 2 3 4 5
#
# BREAK:
#     1 2


# ============================================================
# 56. PASS IN NESTED LOOP VS CONTINUE
# ============================================================

for row in range(1, 4):

    for column in range(1, 4):

        if column == 2:
            pass

        print(row, column)


for row in range(1, 4):

    for column in range(1, 4):

        if column == 2:
            continue

        print(row, column)


# ============================================================
# 57. PASS WITH CLASS INHERITANCE
# ============================================================

class Animal:
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass


# ============================================================
# 58. PASS WITH EMPTY DATA MODEL
# ============================================================

class User:
    pass


user = User()
user.name = "Kishor"

print(user.name)


# ============================================================
# 59. PASS WITH CUSTOM EXCEPTION HIERARCHY
# ============================================================

class ApplicationError(Exception):
    pass


class DatabaseError(ApplicationError):
    pass


class ValidationError(ApplicationError):
    pass


# ============================================================
# 60. PASS WITH CONDITIONAL CLASS CREATION
# ============================================================

development_mode = True

if development_mode:

    class DevelopmentConfig:
        pass


# ============================================================
# 61. PASS WITH PLACEHOLDER LOOP
# ============================================================

items = ["A", "B", "C"]

for item in items:
    pass


# ============================================================
# 62. PASS WITH FUTURE IMPLEMENTATION
# ============================================================

def send_email():
    # Implementation will be added later.
    pass


def send_sms():
    # Implementation will be added later.
    pass


def send_notification():
    # Implementation will be added later.
    pass


# ============================================================
# 63. PASS IN CONDITIONAL PROCESSING
# ============================================================

score = 85

if score >= 90:
    print("Excellent")

elif score >= 75:
    pass

else:
    print("Needs improvement")


# ============================================================
# 64. PASS WITH STATE MACHINE
# ============================================================

state = "processing"

if state == "created":
    print("Created")

elif state == "processing":
    pass

elif state == "completed":
    print("Completed")


# ============================================================
# 65. PASS WITH OPTIONAL HANDLER
# ============================================================

event = "unknown"

if event == "login":
    print("Login event")

elif event == "logout":
    print("Logout event")

else:
    pass


# ============================================================
# 66. PASS WITH EMPTY ITERATION
# ============================================================

for _ in []:
    pass


# ============================================================
# 67. PASS WITH UNDERSCORE
# ============================================================

for _ in range(5):
    pass


# `_` is commonly used when the loop variable is not needed.


# ============================================================
# 68. PASS IN A PLACEHOLDER CALLBACK
# ============================================================

def on_success():
    pass


def on_error():
    pass


# ============================================================
# 69. PASS WITH CONFIGURATION
# ============================================================

config = {
    "debug": False,
    "testing": True
}

if config["debug"]:
    pass


# ============================================================
# 70. PASS WITH FEATURE FLAGS
# ============================================================

features = {
    "dark_mode": True,
    "notifications": False
}

if features["notifications"]:
    print("Notifications enabled")
else:
    pass


# ============================================================
# 71. PASS WITH VALIDATION BRANCH
# ============================================================

username = "Kishor"

if len(username) >= 5:
    pass
else:
    print("Username is too short")


# ============================================================
# 72. PASS WITH RANGE CHECK
# ============================================================

age = 25

if 18 <= age <= 60:
    pass
else:
    print("Age outside allowed range")


# ============================================================
# 73. PASS WITH MULTIPLE BRANCHES
# ============================================================

marks = 85

if marks >= 90:
    print("A+")

elif marks >= 80:
    pass

elif marks >= 70:
    print("B")

else:
    print("Needs improvement")


# ============================================================
# 74. PASS IN A DATA PROCESSING PIPELINE
# ============================================================

data = [10, 20, 30, 40]

for value in data:

    if value < 0:
        pass

    print(
        "Processing:",
        value
    )


# ============================================================
# 75. PASS WITH RESOURCE PLACEHOLDER
# ============================================================

class ResourceManager:

    def acquire(self):
        pass

    def release(self):
        pass


# ============================================================
# 76. PASS WITH SERVICE PLACEHOLDER
# ============================================================

class UserService:

    def create_user(self):
        pass

    def update_user(self):
        pass

    def delete_user(self):
        pass


# ============================================================
# 77. PASS WITH REPOSITORY PLACEHOLDER
# ============================================================

class UserRepository:

    def save(self):
        pass

    def find(self):
        pass

    def delete(self):
        pass


# ============================================================
# 78. PASS WITH CONTROLLER PLACEHOLDER
# ============================================================

class UserController:

    def get(self):
        pass

    def post(self):
        pass


# ============================================================
# 79. PASS IN CUSTOM ITERATION
# ============================================================

values = [1, 2, 3]

for value in values:

    if value == 2:
        pass

    print(value)


# ============================================================
# 80. PASS WITH LOOP ELSE
# ============================================================

for number in range(1, 4):

    if number == 2:
        pass

else:
    print("No break occurred")


# `pass` does not count as a loop termination.


# ============================================================
# 81. PASS WITH BREAK AND CONTINUE
# ============================================================

for number in range(1, 10):

    if number == 3:
        pass

    if number == 5:
        continue

    if number == 8:
        break

    print(number)


# ============================================================
# 82. PASS WITH ALL THREE CONTROL STATEMENTS
# ============================================================

for number in range(1, 10):

    if number == 2:
        pass

    if number == 4:
        continue

    if number == 7:
        break

    print(number)


# ============================================================
# 83. PASS IN A FUNCTION WITH RETURN LATER
# ============================================================

def get_status(active):

    if active:
        return "Active"

    pass


print(get_status(True))


# If the function reaches `pass`, execution continues.
# If the function reaches its end without `return`,
# Python returns None.


# ============================================================
# 84. PASS DOES NOT RETURN A VALUE
# ============================================================

def do_nothing():
    pass


result = do_nothing()

print(result)

# Output:
# None


# ============================================================
# 85. PASS IS A STATEMENT
# ============================================================

pass


# `pass` is a Python statement, not a value.


# ============================================================
# 86. PASS IN FUNCTION BODY
# ============================================================

def placeholder():
    pass


# ============================================================
# 87. PASS IN CLASS BODY
# ============================================================

class Placeholder:
    pass


# ============================================================
# 88. PASS IN EXCEPTION CLASS
# ============================================================

class CustomError(Exception):
    pass


# ============================================================
# 89. PASS IN LOOP BODY
# ============================================================

for _ in range(3):
    pass


# ============================================================
# 90. PASS IN CONDITIONAL BODY
# ============================================================

if True:
    pass


# ============================================================
# 91. WHEN TO USE PASS
# ============================================================

"""
Use `pass` when:

1. You need an empty function temporarily.

2. You need an empty class temporarily.

3. You need an empty exception class.

4. You need a placeholder for future implementation.

5. You are prototyping a program.

6. A branch intentionally requires no action.

7. You need syntactically valid Python while developing.


Example:

    def future_feature():
        pass


Example:

    class FutureFeature:
        pass
"""


# ============================================================
# 92. WHEN NOT TO USE PASS
# ============================================================

"""
Do NOT use `pass` when you actually want to skip a loop
iteration.

Wrong:

    for number in range(10):

        if number == 5:
            pass

        print(number)


Correct:

    for number in range(10):

        if number == 5:
            continue

        print(number)


Do NOT use `pass` when you want to stop a loop.

Wrong:

    for number in range(10):

        if number == 5:
            pass


Correct:

    for number in range(10):

        if number == 5:
            break
"""


# ============================================================
# 93. QUICK COMPARISON
# ============================================================

"""
+----------+----------------------------------------------+
| Keyword  | Behavior                                     |
+----------+----------------------------------------------+
| pass     | Does nothing                                 |
| continue | Skips current loop iteration                 |
| break    | Terminates the nearest loop                  |
+----------+----------------------------------------------+
"""


# ============================================================
# 94. FINAL PRACTICAL EXAMPLE
# ============================================================

users = [
    {"name": "Amit", "active": True},
    {"name": "Rahul", "active": False},
    {"name": "Kishor", "active": True}
]

for user in users:

    if not user["active"]:
        pass

    print(
        "User:",
        user["name"]
    )


# Notice:
#
# `pass` does NOT skip Rahul.
#
# If Rahul should be skipped, use:
#
#     if not user["active"]:
#         continue


# ============================================================
# 95. FINAL SUMMARY
# ============================================================

"""
PASS STATEMENT — FINAL SUMMARY
==============================

`pass` is a null statement.

It performs no operation.

It is primarily used as a placeholder.

Syntax:

    pass


Example:

    if condition:
        pass


Function placeholder:

    def function():
        pass


Class placeholder:

    class MyClass:
        pass


Exception placeholder:

    class MyError(Exception):
        pass


Loop placeholder:

    for item in items:
        pass


IMPORTANT DIFFERENCE
--------------------

pass
    -> Does nothing.
    -> Execution continues normally.

continue
    -> Skips the remaining loop body.
    -> Starts the next iteration.

break
    -> Stops the nearest loop completely.


Memory trick:

    pass     = "Do nothing."

    continue = "Skip this iteration."

    break    = "Stop the loop."


Most common professional use:

    def feature_not_implemented():
        pass


    class CustomError(Exception):
        pass


Avoid using `pass` when `continue` or `break` is the
actual behavior you need.
"""


# ============================================================
# END OF PASS
# ============================================================

print("\nPass statement demonstration completed successfully!")
