"""
04 - Default, Positional and Keyword Arguments
===============================================

Python allows us to pass arguments to functions in different ways.

This file covers:

1. Positional arguments
2. Keyword arguments
3. Default arguments
4. Combining positional and keyword arguments
5. Rules for argument ordering
6. Common mistakes
7. Practical examples


Quick Reference
---------------

Positional:
    function("Kishor", 20)

Keyword:
    function(name="Kishor", age=20)

Default:
    def function(name="Guest"):
        ...

    function()
"""


# ============================================================
# 1. Positional Arguments
# ============================================================

"""
Positional arguments are assigned to parameters according
to their position.
"""


def student(name, age):
    print("Name:", name)
    print("Age:", age)


student("Kishor", 20)


# Assignment:
#
# name = "Kishor"
# age  = 20


# ============================================================
# 2. Position Matters
# ============================================================

def person(name, age):
    print("Name:", name)
    print("Age:", age)


person("Kishor", 20)


# If the values are swapped:

person(20, "Kishor")

# Python does not automatically determine the correct
# parameter based on the data type.
#
# It simply follows the position.


# ============================================================
# 3. Multiple Positional Arguments
# ============================================================

def student_details(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student_details("Kishor", 20, "Python")


# ============================================================
# 4. Keyword Arguments
# ============================================================

"""
Keyword arguments are passed using parameter names.
"""


def employee(name, department):
    print("Name:", name)
    print("Department:", department)


employee(
    name="Kishor",
    department="Python"
)


# ============================================================
# 5. Keyword Arguments Ignore Order
# ============================================================

employee(
    department="Python",
    name="Kishor"
)

# Both calls produce the same result.


# ============================================================
# 6. Positional vs Keyword Arguments
# ============================================================

def course(student_name, course_name, duration):
    print("Student:", student_name)
    print("Course:", course_name)
    print("Duration:", duration)


# Positional arguments

course("Kishor", "Python", 30)


# Keyword arguments

course(
    student_name="Kishor",
    course_name="Python",
    duration=30
)


# Keyword arguments make the meaning of each value clearer.


# ============================================================
# 7. Default Arguments
# ============================================================

"""
A default argument is a parameter with a predefined value.

If the caller does not provide a value,
the default value is used.
"""


def greet(name="Guest"):
    print("Hello,", name)


# Uses default value.

greet()


# Uses provided value.

greet("Kishor")


# ============================================================
# 8. Multiple Default Arguments
# ============================================================

def student_info(
    name="Unknown",
    age=0,
    course="Python"
):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student_info()

student_info("Kishor")

student_info("Kishor", 20)

student_info("Kishor", 20, "Java")


# ============================================================
# 9. Required + Default Parameters
# ============================================================

"""
Required parameters should come before default parameters.
"""


def welcome(name, message="Welcome to Python!"):
    print(message, name)


welcome("Kishor")

welcome(
    "Kishor",
    "Good Morning!"
)


# ============================================================
# 10. Keyword Argument with Default Parameter
# ============================================================

def introduce(
    name,
    age=18,
    city="Pune"
):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)


introduce("Kishor")

introduce(
    "Kishor",
    city="Mumbai"
)

introduce(
    "Kishor",
    age=20,
    city="Pune"
)


# ============================================================
# 11. Mixing Positional and Keyword Arguments
# ============================================================

def student(
    name,
    age,
    course
):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


# Positional argument first,
# followed by keyword arguments.

student(
    "Kishor",
    age=20,
    course="Python"
)


# Another example:

student(
    "Kishor",
    course="Python",
    age=20
)


# ============================================================
# 12. Argument Ordering Rule
# ============================================================

"""
When calling a function:

    Positional arguments
            ↓
    Keyword arguments

Example:

    student(
        "Kishor",       # positional
        age=20,         # keyword
        course="Python" # keyword
    )

Correct.
"""


# ============================================================
# 13. Invalid Argument Ordering
# ============================================================

"""
This is INVALID:

    student(
        name="Kishor",
        20,
        "Python"
    )

Why?

Because positional arguments cannot appear after
keyword arguments.
"""


# ============================================================
# 14. Default Parameter Rule
# ============================================================

"""
When defining a function, required parameters should come
before parameters with default values.

Correct:

    def greet(name, message="Hello"):
        ...


Incorrect:

    def greet(message="Hello", name):
        ...

Python will raise a SyntaxError.
"""


# ============================================================
# 15. Practical Example - Product
# ============================================================

def product_details(
    name,
    price,
    quantity=1
):
    total = price * quantity

    print("Product:", name)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Total:", total)


product_details(
    "Keyboard",
    1000
)


product_details(
    "Mouse",
    500,
    2
)


# Using keyword arguments:

product_details(
    name="Monitor",
    price=10000,
    quantity=2
)


# ============================================================
# 16. Practical Example - Student
# ============================================================

def display_student(
    name,
    age,
    course="Python",
    city="Pune"
):
    print("-------------------------")
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)
    print("City:", city)
    print("-------------------------")


display_student("Kishor", 20)


display_student(
    "Rahul",
    21,
    "Java",
    "Mumbai"
)


display_student(
    name="Priya",
    age=22,
    city="Delhi"
)


# ============================================================
# 17. Practical Example - Calculator
# ============================================================

def calculate(
    a,
    b,
    operation="add"
):

    if operation == "add":
        return a + b

    elif operation == "subtract":
        return a - b

    elif operation == "multiply":
        return a * b

    elif operation == "divide":

        if b == 0:
            return "Cannot divide by zero"

        return a / b

    return "Invalid operation"


print(calculate(10, 5))

print(calculate(10, 5, "subtract"))

print(
    calculate(
        10,
        5,
        operation="multiply"
    )
)

print(
    calculate(
        a=10,
        b=5,
        operation="divide"
    )
)


# ============================================================
# 18. Keyword Arguments Improve Readability
# ============================================================

def create_account(
    username,
    age,
    country,
    active=True
):
    print("Username:", username)
    print("Age:", age)
    print("Country:", country)
    print("Active:", active)


# Positional version

create_account(
    "Kishor",
    20,
    "India",
    True
)


# Keyword version

create_account(
    username="Kishor",
    age=20,
    country="India",
    active=True
)


# Keyword arguments make long function calls easier to read.


# ============================================================
# 19. Default Values Can Be Overridden
# ============================================================

def order(item, quantity=1):
    print("Item:", item)
    print("Quantity:", quantity)


# Default quantity

order("Book")


# Override default quantity

order("Book", 5)


# Keyword override

order(
    item="Book",
    quantity=10
)


# ============================================================
# 20. Common Mistake - Too Few Arguments
# ============================================================

def add(a, b):
    return a + b


# This is incorrect:
#
# add(10)
#
# Python raises TypeError because b is missing.


# Correct:

print(add(10, 20))


# ============================================================
# 21. Common Mistake - Too Many Arguments
# ============================================================

def greet_user(name):
    print("Hello", name)


# This is incorrect:
#
# greet_user("Kishor", 20)
#
# The function accepts only one argument.


# Correct:

greet_user("Kishor")


# ============================================================
# 22. Common Mistake - Duplicate Argument
# ============================================================

def display(name, age):
    print(name, age)


# This is incorrect:
#
# display("Kishor", name="Rahul", age=20)
#
# `name` receives two values.


# Correct:

display(
    name="Kishor",
    age=20
)


# ============================================================
# 23. Practical Example - Rectangle
# ============================================================

def rectangle(
    length,
    width=10
):
    return length * width


print(rectangle(20))

print(rectangle(20, 5))

print(
    rectangle(
        length=30,
        width=15
    )
)


# ============================================================
# 24. Practical Example - Greeting
# ============================================================

def greet_person(
    name,
    greeting="Hello"
):
    return f"{greeting}, {name}!"


print(greet_person("Kishor"))

print(
    greet_person(
        "Kishor",
        "Good Morning"
    )
)

print(
    greet_person(
        name="Priya",
        greeting="Welcome"
    )
)


# ============================================================
# 25. Quick Comparison
# ============================================================

"""
POSITIONAL ARGUMENTS
--------------------

def student(name, age):
    ...


student("Kishor", 20)


The order matters.


KEYWORD ARGUMENTS
-----------------

student(
    age=20,
    name="Kishor"
)


The parameter names are specified,
so the order does not matter.


DEFAULT ARGUMENTS
-----------------

def student(name, course="Python"):
    ...


student("Kishor")

The default value is used when course
is not provided.
"""


# ============================================================
# 26. Mini Practice
# ============================================================

# Practice 1:
# Create a function:
#
# def greet(name, message="Hello"):
#     ...
#
# Call it using both the default and custom message.


# Practice 2:
# Create a function that accepts:
#
# name
# age
# city="Pune"
#
# Print all three values.


# Practice 3:
# Create a function to calculate the price of a product:
#
# price
# quantity=1
#
# Return the total price.


# Practice 4:
# Create a function with three parameters and call it
# using keyword arguments in a different order.


# Practice 5:
# Create a function for calculating simple interest:
#
# principal
# rate
# time=1
#
# Formula:
#
# SI = (principal * rate * time) / 100


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
1. Positional arguments are assigned according to order.
2. Keyword arguments are assigned using parameter names.
3. Keyword argument order does not matter.
4. Default parameters provide fallback values.
5. Required parameters should come before default parameters.
6. Positional arguments should come before keyword arguments.
7. A default value can be overridden by providing an argument.
8. Keyword arguments improve readability for complex calls.
9. Too few or too many arguments can cause TypeError.
10. Understanding argument rules is essential before learning
    *args and **kwargs.
"""

