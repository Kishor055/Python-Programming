"""
05 - Keyword Arguments
======================

Keyword arguments allow us to pass values to a function by
explicitly specifying the parameter name.

Syntax:

    function_name(parameter=value)

Example:

    def student(name, age):
        print(name, age)

    student(name="Kishor", age=20)

Why use keyword arguments?
--------------------------
1. They make function calls easier to understand.
2. The order of keyword arguments does not matter.
3. They make code more readable.
4. They are useful when a function has many parameters.
5. They allow us to provide values for specific parameters.
"""

# ============================================================
# 1. Basic Keyword Argument
# ============================================================

def greet(name):
    print("Hello,", name)

greet(name="Kishor")

# `name="Kishor"` is a keyword argument.

# ============================================================
# 2. Positional Argument vs Keyword Argument
# ============================================================

def student(name, age):
    print("Name:", name)
    print("Age:", age)

# Positional arguments

student("Kishor", 20)

# Keyword arguments

student(
    name="Kishor",
    age=20
)

# ============================================================
# 3. Keyword Arguments Do Not Depend on Position
# ============================================================

def person(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

person(
    city="Pune",
    name="Kishor",
    age=20
)

# The order does not matter because parameter names
# explicitly identify the values.

# ============================================================
# 4. Compare Positional and Keyword Arguments
# ============================================================

def employee(name, department, salary):
    print("Name:", name)
    print("Department:", department)
    print("Salary:", salary)

# Positional

employee(
    "Kishor",
    "Development",
    50000
)

# Keyword

employee(
    name="Kishor",
    department="Development",
    salary=50000
)

# Keyword arguments make the meaning of each value clearer.

# ============================================================
# 5. Keyword Arguments with Different Data Types
# ============================================================

def profile(name, age, active, skills):
    print("Name:", name)
    print("Age:", age)
    print("Active:", active)
    print("Skills:", skills)

profile(
    name="Kishor",
    age=20,
    active=True,
    skills=["Python", "SQL", "Git"]
)

# ============================================================
# 6. Keyword Arguments Can Be Written in Any Order
# ============================================================

def course(name, duration, level):
    print("Course:", name)
    print("Duration:", duration)
    print("Level:", level)

course(
    level="Beginner",
    name="Python",
    duration=30
)

course(
    duration=30,
    level="Beginner",
    name="Python"
)

# Both calls are valid.

# ============================================================
# 7. Mixing Positional and Keyword Arguments
# ============================================================

"""
Positional arguments can be followed by keyword arguments.
"""

def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student_info(
    "Kishor",
    age=20,
    course="Python"
)

# Here:
#
# "Kishor" -> positional argument
# age=20    -> keyword argument
# course=   -> keyword argument

# ============================================================
# 8. Positional Arguments Must Come First
# ============================================================

# Correct:

student_info(
    "Kishor",
    age=20,
    course="Python"
)

# Incorrect:
#
# student_info(
#     name="Kishor",
#     20,
#     "Python"
# )
#
# A positional argument cannot appear after a keyword argument.

# ============================================================
# 9. All Arguments as Keyword Arguments
# ============================================================

student_info(
    name="Kishor",
    age=20,
    course="Python"
)

# ============================================================
# 10. Keyword Arguments with Default Parameters
# ============================================================

def greet_user(name, message="Hello"):
    print(message, name)

# Uses default message

greet_user(name="Kishor")

# Overrides default message

greet_user(
    name="Kishor",
    message="Good Morning"
)

# ============================================================
# 11. Selecting Specific Default Parameters
# ============================================================

def introduce(
    name,
    age=18,
    city="Pune",
    course="Python"
):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)
    print("Course:", course)

# Only change city.
# age and course keep their default values.

introduce(
    name="Kishor",
    city="Mumbai"
)

# Change only course.

introduce(
    name="Kishor",
    course="Java"
)

# Change age and course.

introduce(
    name="Kishor",
    age=20,
    course="Python"
)

# ============================================================
# 12. Practical Example - Product
# ============================================================

def product(
    name,
    price,
    quantity=1
):
    total = price * quantity

    print("Product:", name)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Total:", total)

product(
    name="Keyboard",
    price=1000
)

product(
    name="Mouse",
    price=500,
    quantity=2
)

# ============================================================
# 13. Practical Example - Student
# ============================================================

def display_student(
    name,
    age,
    course,
    city
):
    print("-------------------------")
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)
    print("City:", city)
    print("-------------------------")

display_student(
    name="Kishor",
    age=20,
    course="Python",
    city="Pune"
)

# ============================================================
# 14. Practical Example - Calculator
# ============================================================

def calculate(a, b, operation):

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

print(
    calculate(
        a=10,
        b=5,
        operation="add"
    )
)

print(
    calculate(
        operation="multiply",
        a=10,
        b=5
    )
)

# ============================================================
# 15. Keyword Arguments Improve Readability
# ============================================================

def create_account(
    username,
    email,
    age,
    country
):
    print("Username:", username)
    print("Email:", email)
    print("Age:", age)
    print("Country:", country)

# Positional version

create_account(
    "kishor",
    "kishor@example.com",
    20,
    "India"
)

# Keyword version

create_account(
    username="kishor",
    email="kishor@example.com",
    age=20,
    country="India"
)

# The second version makes it much easier to understand
# which value belongs to which parameter.

# ============================================================
# 16. Keyword Arguments with Boolean Values
# ============================================================

def account_settings(
    username,
    active=True,
    notifications=True,
    dark_mode=False
):
    print("Username:", username)
    print("Active:", active)
    print("Notifications:", notifications)
    print("Dark mode:", dark_mode)

account_settings(
    username="kishor"
)

account_settings(
    username="kishor",
    notifications=False,
    dark_mode=True
)

# ============================================================
# 17. Keyword-Only Arguments
# ============================================================

"""
Python also allows us to force certain parameters to be
passed using keywords.

A `*` can be used to create keyword-only parameters.

Example:

    def student(name, *, age, city):
        ...

Here:
    name -> can be positional or keyword
    age  -> must be keyword
    city -> must be keyword
"""

def student(name, *, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

student(
    "Kishor",
    age=20,
    city="Pune"
)

# This is also valid:

student(
    name="Kishor",
    age=20,
    city="Pune"
)

# The following is invalid:
#
# student("Kishor", 20, "Pune")
#
# because age and city are keyword-only parameters.

# ============================================================
# 18. Why Keyword-Only Parameters Are Useful
# ============================================================

def create_user(
    username,
    *,
    active=True,
    admin=False
):
    print("Username:", username)
    print("Active:", active)
    print("Admin:", admin)

create_user(
    "kishor",
    active=True,
    admin=False
)

# This makes it very clear what True and False represent.

# ============================================================
# 19. Keyword Argument with Expression
# ============================================================

def calculate_price(price, quantity, discount):
    return price * quantity - discount

total = calculate_price(
    price=1000,
    quantity=2,
    discount=100
)

print("Total:", total)

# ============================================================
# 20. Passing a Dictionary Using **
# ============================================================

"""
A dictionary can be unpacked into keyword arguments using **.
"""

def student(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

details = {
    "name": "Kishor",
    "age": 20,
    "city": "Pune"
}

student(**details)

# This is equivalent to:
#
# student(
#     name="Kishor",
#     age=20,
#     city="Pune"
# )

# ============================================================
# 21. Dictionary Keys Must Match Parameter Names
# ============================================================

def employee(name, department):
    print(name, department)

details = {
    "name": "Kishor",
    "department": "Development"
}

employee(**details)

# The dictionary keys:
#
# "name"
# "department"
#
# match the function parameters.

# ============================================================
# 22. Practical Example - Order
# ============================================================

def create_order(
    customer,
    product,
    quantity=1,
    express=False
):
    print("Customer:", customer)
    print("Product:", product)
    print("Quantity:", quantity)
    print("Express:", express)

create_order(
    customer="Kishor",
    product="Laptop",
    quantity=1,
    express=True
)

# ============================================================
# 23. Common Mistake - Unknown Keyword
# ============================================================

def greet(name):
    print("Hello", name)

# Incorrect:
#
# greet(username="Kishor")
#
# The function has `name`, not `username`.
#
# Python raises:
#
# TypeError

# Correct:

greet(name="Kishor")

# ============================================================
# 24. Common Mistake - Duplicate Argument
# ============================================================

def display(name, age):
    print(name, age)

# Incorrect:
#
# display(
#     "Kishor",
#     name="Rahul",
#     age=20
# )
#
# `name` receives two values:
#
# "Kishor"
# "Rahul"
#
# Python raises TypeError.

# Correct:

display(
    name="Kishor",
    age=20
)

# ============================================================
# 25. Common Mistake - Positional After Keyword
# ============================================================

def example(name, age, city):
    print(name, age, city)

# Incorrect:
#
# example(
#     name="Kishor",
#     20,
#     "Pune"
# )
#
# Positional arguments cannot appear after keyword arguments.

# Correct:

example(
    "Kishor",
    age=20,
    city="Pune"
)

# ============================================================
# 26. Practical Example - Course Registration
# ============================================================

def register(
    student_name,
    course,
    duration=30,
    online=True
):
    print("-------------------------")
    print("Student:", student_name)
    print("Course:", course)
    print("Duration:", duration, "days")
    print("Online:", online)
    print("-------------------------")

register(
    student_name="Kishor",
    course="Python"
)

register(
    student_name="Rahul",
    course="Java",
    duration=45,
    online=False
)

# ============================================================
# 27. Practical Example - Function with Many Parameters
# ============================================================

def profile(
    name,
    age,
    city,
    profession,
    experience
):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)
    print("Profession:", profession)
    print("Experience:", experience)

profile(
    name="Kishor",
    age=20,
    city="Pune",
    profession="Developer",
    experience=2
)

# Keyword arguments are especially useful when a function
# has many parameters.

# ============================================================
# 28. Mini Practice
# ============================================================

# Practice 1:
# Create a function:
#
# def student(name, age, city):
#     ...
#
# Call it using only keyword arguments.

# Practice 2:
# Create a function with:
#
# name
# age
# city="Pune"
#
# Use a keyword argument to change only the city.

# Practice 3:
# Create a function:
#
# def calculate(principal, rate, time):
#     ...
#
# Call it using keyword arguments in a different order.

# Practice 4:
# Create a function with keyword-only parameters:
#
# def account(username, *, active=True, admin=False):
#     ...
#
# Call it correctly.

# Practice 5:
# Create a dictionary containing student details and
# pass it to a function using **.

# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
1. Keyword arguments use parameter names when calling
   a function.

2. Example:
       greet(name="Kishor")

3. Keyword argument order does not matter.

4. Positional arguments must come before keyword arguments.

5. Keyword arguments improve readability.

6. Keyword arguments are especially useful for functions
   with many parameters.

7. Default parameters can be overridden using keywords.

8. `*` can be used to create keyword-only parameters.

9. `**dictionary` can unpack dictionary values into
   keyword arguments.

10. The dictionary keys must match the function's
    parameter names.

11. A parameter cannot receive two values in the same call.

12. An unknown keyword argument causes a TypeError.
"""
```
 **Basics → Parameters → Return → Default/Positional → Keyword Arguments → `*args`**.
