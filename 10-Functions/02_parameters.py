"""
02 - Function Parameters
========================

Parameters allow functions to receive data from the caller.

A parameter is a variable listed inside the function definition.

An argument is the actual value passed to the function when it is called.

Example:

    def greet(name):
        print("Hello", name)

    greet("Kishor")

Here:
    name     -> Parameter
    "Kishor" -> Argument
"""


# ============================================================
# 1. What is a Parameter?
# ============================================================

def greet(name):
    print("Hello,", name)


greet("Kishor")
greet("Python")


# ------------------------------------------------------------
# Parameter:
#
# def greet(name):
#            ^^^^
#          parameter
#
# Argument:
#
# greet("Kishor")
#       ^^^^^^^^
#        argument
# ------------------------------------------------------------


# ============================================================
# 2. Single Parameter
# ============================================================

def square(number):
    result = number ** 2
    print("Square:", result)


square(5)
square(10)
square(15)


# ============================================================
# 3. Multiple Parameters
# ============================================================

def add(a, b):
    result = a + b
    print("Sum:", result)


add(10, 20)
add(100, 200)


# Another example

def introduce(name, age):
    print("Name:", name)
    print("Age:", age)


introduce("Kishor", 20)


# ============================================================
# 4. Parameters Can Have Different Data Types
# ============================================================

def display_details(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)


display_details("Kishor", 20, "Pune")


# Functions do not require parameters to be of a specific
# type unless the function's logic requires it.


def display_value(value):
    print("Value:", value)


display_value(100)
display_value("Python")
display_value(10.5)
display_value([1, 2, 3])


# ============================================================
# 5. Positional Arguments
# ============================================================

"""
With positional arguments, values are assigned according
to their position.
"""


def student(name, age):
    print("Name:", name)
    print("Age:", age)


student("Kishor", 20)


# First argument -> name
# Second argument -> age


# ============================================================
# 6. Order Matters with Positional Arguments
# ============================================================

def person(name, age):
    print("Name:", name)
    print("Age:", age)


person("Kishor", 20)

# The following call swaps the values:
# person(20, "Kishor")
#
# Python will assign:
# name = 20
# age = "Kishor"
#
# Python follows the position of the arguments.


# ============================================================
# 7. Keyword Arguments
# ============================================================

"""
Keyword arguments are passed using parameter names.

Syntax:

    function(parameter=value)
"""


def employee(name, department):
    print("Name:", name)
    print("Department:", department)


employee(name="Kishor", department="Python")


# ============================================================
# 8. Keyword Arguments Can Change the Order
# ============================================================

employee(
    department="Python",
    name="Kishor"
)


# Both calls produce the same result because the parameter
# names explicitly identify which value goes where.


# ============================================================
# 9. Positional + Keyword Arguments
# ============================================================

def course(student_name, course_name, duration):
    print("Student:", student_name)
    print("Course:", course_name)
    print("Duration:", duration)


course(
    "Kishor",
    course_name="Python",
    duration=30
)


# IMPORTANT:
#
# Positional arguments must come before keyword arguments.
#
# Correct:
# course("Kishor", course_name="Python", duration=30)
#
# Incorrect:
# course(student_name="Kishor", "Python", 30)


# ============================================================
# 10. Default Parameters
# ============================================================

"""
A default parameter has a value that is used when the caller
does not provide an argument.
"""


def greet_user(name="Guest"):
    print("Hello,", name)


# Uses the default value.
greet_user()

# Uses the supplied value.
greet_user("Kishor")


# ============================================================
# 11. Multiple Default Parameters
# ============================================================

def student_info(name="Unknown", age=0, city="Unknown"):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)


student_info()

student_info("Kishor")

student_info("Kishor", 20)

student_info("Kishor", 20, "Pune")


# ============================================================
# 12. Mixing Required and Default Parameters
# ============================================================

def welcome(name, message="Welcome to Python!"):
    print(message, name)


welcome("Kishor")

welcome("Kishor", "Good Morning")


# `name` is required.
# `message` has a default value.


# ============================================================
# 13. Practical Example - Calculate Total
# ============================================================

def calculate_total(price, quantity):
    return price * quantity


total = calculate_total(100, 5)

print("Total:", total)


# Keyword arguments can also be used.

total = calculate_total(
    price=250,
    quantity=4
)

print("Total:", total)


# ============================================================
# 14. Practical Example - Student Details
# ============================================================

def display_student(name, age, course="Python"):
    print("------------------------")
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)
    print("------------------------")


display_student("Kishor", 20)

display_student("Rahul", 22, "Java")

display_student(
    name="Priya",
    age=21,
    course="Data Science"
)


# ============================================================
# 15. Practical Example - Rectangle
# ============================================================

def rectangle_area(length, width):
    return length * width


area = rectangle_area(10, 5)

print("Area:", area)


# Keyword arguments

area = rectangle_area(
    length=20,
    width=10
)

print("Area:", area)


# ============================================================
# 16. Parameters and Return Values Together
# ============================================================

def multiply(number1, number2):
    return number1 * number2


result = multiply(10, 5)

print("Result:", result)


# The returned value can be used in another calculation.

final_result = multiply(10, 5) + 100

print("Final result:", final_result)


# ============================================================
# 17. Function with a Default Parameter and Return
# ============================================================

def power(number, exponent=2):
    return number ** exponent


print(power(5))       # 5²
print(power(5, 3))    # 5³
print(power(2, 4))    # 2⁴


# ============================================================
# 18. Parameter vs Argument - Quick Revision
# ============================================================

"""
Parameter:

    def add(a, b):
        ...

    a and b are parameters.

Argument:

    add(10, 20)

    10 and 20 are arguments.
"""


# ============================================================
# 19. Important Rules
# ============================================================

"""
Rule 1:
Required parameters normally come before default parameters.

Correct:

    def greet(name, message="Hello"):
        ...


Rule 2:
Positional arguments come before keyword arguments.

Correct:

    greet("Kishor", message="Hello")


Rule 3:
The number of required positional arguments must match
the number of parameters that need values.

Example:

    def add(a, b):
        ...

    add(10)       # Missing argument
    add(10, 20)   # Correct
    add(10, 20, 30)  # Too many arguments
"""


# ============================================================
# 20. Mini Practice
# ============================================================

# Practice 1:
# Create a function that accepts name and age and prints:
#
# "Kishor is 20 years old."


# Practice 2:
# Create a function that accepts length and width and
# returns the area of a rectangle.


# Practice 3:
# Create a function with a default country:
#
# def introduce(name, country="India"):
#     ...


# Practice 4:
# Call a function using keyword arguments.


# Practice 5:
# Create a function that accepts three numbers and returns
# their average.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
1. Parameters are variables defined in a function.
2. Arguments are values passed during a function call.
3. Positional arguments are assigned according to position.
4. Keyword arguments are assigned using parameter names.
5. Default parameters provide fallback values.
6. Required parameters should be supplied by the caller.
7. Positional arguments should come before keyword arguments.
8. Parameters can be used together with return values.
9. Meaningful parameter names make functions easier to understand.
"""
                 FUNCTION
                     │
          ┌──────────┴──────────┐
          ↓                     ↓
      Parameter              Argument
   Function definition     Function call
          │                     │
          ↓                     ↓
    def greet(name):       greet("Kishor")
                 │                   │
                 └─────────┬─────────┘
                           ↓
                    name = "Kishor"
