"""
07 - **kwargs
=============

Sometimes we don't know in advance how many keyword arguments
a function will receive.

Python provides **kwargs for this situation.

**kwargs
--------
`**kwargs` allows a function to accept any number of
keyword arguments.

The arguments are collected into a dictionary.

Syntax:

    def function_name(**kwargs):
        ...


Example:

    def show_details(**kwargs):
        print(kwargs)

    show_details(
        name="Kishor",
        age=20
    )

Output:

    {'name': 'Kishor', 'age': 20}


Important:
----------
*args  -> multiple positional arguments -> tuple
**kwargs -> multiple keyword arguments -> dictionary
"""


# ============================================================
# 1. Basic **kwargs
# ============================================================

def show_details(**kwargs):
    print(kwargs)


show_details(
    name="Kishor",
    age=20
)


# ============================================================
# 2. **kwargs Stores Values in a Dictionary
# ============================================================

def check_kwargs(**kwargs):

    print("Arguments:", kwargs)
    print("Type:", type(kwargs))


check_kwargs(
    name="Kishor",
    age=20,
    city="Pune"
)


# Output:
#
# Arguments: {'name': 'Kishor', 'age': 20, 'city': 'Pune'}
# Type: <class 'dict'>


# ============================================================
# 3. Loop Through **kwargs
# ============================================================

def display_details(**details):

    for key, value in details.items():
        print(key, ":", value)


display_details(
    name="Kishor",
    age=20,
    city="Pune",
    course="Python"
)


# ============================================================
# 4. Access Individual Values
# ============================================================

def student(**details):

    print("Name:", details["name"])
    print("Age:", details["age"])
    print("Course:", details["course"])


student(
    name="Kishor",
    age=20,
    course="Python"
)


# ============================================================
# 5. Using get() with **kwargs
# ============================================================

"""
Using [] raises KeyError if the key does not exist.

Using .get() allows us to provide a default value.
"""


def profile(**details):

    name = details.get("name")
    age = details.get("age")
    city = details.get("city", "Unknown")

    print("Name:", name)
    print("Age:", age)
    print("City:", city)


profile(
    name="Kishor",
    age=20
)


# `city` was not provided, so "Unknown" is used.


# ============================================================
# 6. Any Number of Keyword Arguments
# ============================================================

def show(**kwargs):

    print("Number of arguments:", len(kwargs))

    for key, value in kwargs.items():
        print(f"{key} = {value}")


show()

show(
    name="Kishor"
)

show(
    name="Kishor",
    age=20
)

show(
    name="Kishor",
    age=20,
    city="Pune",
    course="Python"
)


# ============================================================
# 7. **kwargs with Different Data Types
# ============================================================

def display(**kwargs):

    for key, value in kwargs.items():
        print(key, "=>", value, type(value))


display(
    name="Kishor",
    age=20,
    salary=50000.50,
    active=True,
    skills=["Python", "SQL"]
)


# ============================================================
# 8. Empty **kwargs
# ============================================================

def test(**kwargs):

    print("Arguments:", kwargs)
    print("Count:", len(kwargs))


test()


# Output:
#
# Arguments: {}
# Count: 0


# ============================================================
# 9. **kwargs with a Normal Parameter
# ============================================================

"""
A normal parameter can come before **kwargs.

Example:

    def student(name, **details):
        ...


The first argument is assigned to name.

The remaining keyword arguments are collected in details.
"""


def student(name, **details):

    print("Name:", name)
    print("Details:", details)


student(
    "Kishor",
    age=20,
    city="Pune",
    course="Python"
)


# ============================================================
# 10. Loop Through Additional Details
# ============================================================

def employee(name, **details):

    print("Employee:", name)

    for key, value in details.items():
        print(f"{key}: {value}")


employee(
    "Kishor",
    department="Development",
    experience=2,
    city="Pune"
)


# ============================================================
# 11. Practical Example - Student Profile
# ============================================================

def student_profile(name, **details):

    print("-------------------------")
    print("Student:", name)

    for key, value in details.items():
        print(f"{key}: {value}")

    print("-------------------------")


student_profile(
    "Kishor",
    age=20,
    course="Python",
    city="Pune"
)


# ============================================================
# 12. Practical Example - Employee Profile
# ============================================================

def employee_profile(name, **details):

    print("Name:", name)

    print("Additional Information:")

    for key, value in details.items():
        print(f"{key}: {value}")


employee_profile(
    "Kishor",
    department="IT",
    role="Developer",
    experience=2,
    city="Pune"
)


# ============================================================
# 13. Updating the kwargs Dictionary
# ============================================================

def update_details(**kwargs):

    kwargs["updated"] = True

    print(kwargs)


update_details(
    name="Kishor",
    age=20
)


# `kwargs` is a normal dictionary inside the function.


# ============================================================
# 14. Checking Whether a Key Exists
# ============================================================

def check_user(**details):

    if "name" in details:
        print("Name:", details["name"])

    if "email" in details:
        print("Email:", details["email"])

    if "phone" in details:
        print("Phone:", details["phone"])


check_user(
    name="Kishor",
    email="kishor@example.com"
)


# ============================================================
# 15. Practical Example - Configuration
# ============================================================

def configure_app(**settings):

    print("Application Configuration")

    for key, value in settings.items():
        print(f"{key}: {value}")


configure_app(
    debug=True,
    port=8000,
    host="localhost",
    theme="dark"
)


# ============================================================
# 16. Practical Example - Create Account
# ============================================================

def create_account(username, **settings):

    print("Username:", username)

    for key, value in settings.items():
        print(f"{key}: {value}")


create_account(
    "kishor",
    age=20,
    country="India",
    active=True,
    notifications=True
)


# ============================================================
# 17. Passing a Dictionary Using **
# ============================================================

"""
A dictionary can be unpacked into keyword arguments using **.
"""


def introduce(name, age, city):

    print("Name:", name)
    print("Age:", age)
    print("City:", city)


student = {
    "name": "Kishor",
    "age": 20,
    "city": "Pune"
}


introduce(**student)


# This is equivalent to:
#
# introduce(
#     name="Kishor",
#     age=20,
#     city="Pune"
# )


# ============================================================
# 18. Dictionary Unpacking
# ============================================================

def display(name, age, course):

    print(name)
    print(age)
    print(course)


details = {
    "name": "Kishor",
    "age": 20,
    "course": "Python"
}


display(**details)


# ============================================================
# 19. Dictionary Keys Must Match Parameter Names
# ============================================================

def employee(name, department):

    print("Name:", name)
    print("Department:", department)


employee_data = {
    "name": "Kishor",
    "department": "Development"
}


employee(**employee_data)


# Correct because:
#
# "name"       -> name
# "department" -> department


# ============================================================
# 20. Practical Example - Product
# ============================================================

def product(name, **details):

    print("Product:", name)

    for key, value in details.items():
        print(f"{key}: {value}")


product(
    "Laptop",
    price=50000,
    brand="ExampleBrand",
    quantity=1,
    color="Black"
)


# ============================================================
# 21. Practical Example - Order
# ============================================================

def order(customer, **details):

    print("Customer:", customer)

    for key, value in details.items():
        print(f"{key}: {value}")


order(
    "Kishor",
    product="Laptop",
    quantity=1,
    express=True,
    payment="UPI"
)


# ============================================================
# 22. Practical Example - Flexible Logger
# ============================================================

def log(message, **metadata):

    print("[LOG]", message)

    for key, value in metadata.items():
        print(f"{key}: {value}")


log(
    "User logged in",
    user_id=101,
    location="Pune",
    browser="Chrome"
)


# ============================================================
# 23. **kwargs with Default-Like Values
# ============================================================

def account(**settings):

    active = settings.get("active", True)
    admin = settings.get("admin", False)

    print("Active:", active)
    print("Admin:", admin)


account()

account(
    active=False
)

account(
    active=True,
    admin=True
)


# ============================================================
# 24. Combining *args and **kwargs
# ============================================================

"""
A function can accept both:

    *args
    **kwargs
"""


def demo(*args, **kwargs):

    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


demo(
    10,
    20,
    30,
    name="Kishor",
    age=20
)


# *args  -> (10, 20, 30)
# **kwargs -> {"name": "Kishor", "age": 20}


# ============================================================
# 25. Normal Parameter + *args + **kwargs
# ============================================================

def student(name, *subjects, **details):

    print("Name:", name)

    print("Subjects:")

    for subject in subjects:
        print("-", subject)

    print("Additional Details:")

    for key, value in details.items():
        print(f"{key}: {value}")


student(
    "Kishor",
    "Python",
    "SQL",
    "Git",
    age=20,
    city="Pune"
)


# ============================================================
# 26. Practical Example - Report
# ============================================================

def report(title, *items, **settings):

    print("Title:", title)

    print("\nItems:")

    for item in items:
        print("-", item)

    print("\nSettings:")

    for key, value in settings.items():
        print(f"{key}: {value}")


report(
    "Python Topics",
    "Functions",
    "Lists",
    "Dictionaries",
    "Tuples",
    level="Beginner",
    language="Python"
)


# ============================================================
# 27. Merging Dictionaries
# ============================================================

def show_user(**user):

    print(user)


basic_info = {
    "name": "Kishor",
    "age": 20
}

location_info = {
    "city": "Pune",
    "country": "India"
}


show_user(
    **basic_info,
    **location_info
)


# ============================================================
# 28. Duplicate Keys During Unpacking
# ============================================================

"""
Two dictionaries cannot provide the same keyword to a function
call.

For example:

    first = {"name": "Kishor"}
    second = {"name": "Rahul"}

    function(**first, **second)

This causes a TypeError because `name` is provided twice.
"""


# ============================================================
# 29. **kwargs is a Dictionary
# ============================================================

def check_type(**kwargs):

    print("Type:", type(kwargs))

    if isinstance(kwargs, dict):
        print("kwargs is a dictionary")


check_type(
    name="Kishor",
    age=20
)


# ============================================================
# 30. Dictionary Methods with **kwargs
# ============================================================

def dictionary_methods(**kwargs):

    print("Keys:", kwargs.keys())
    print("Values:", kwargs.values())
    print("Items:", kwargs.items())


dictionary_methods(
    name="Kishor",
    age=20,
    city="Pune"
)


# ============================================================
# 31. Practical Example - Filter Details
# ============================================================

def important_details(**details):

    allowed = [
        "name",
        "email",
        "phone"
    ]

    for key, value in details.items():

        if key in allowed:
            print(f"{key}: {value}")


important_details(
    name="Kishor",
    email="kishor@example.com",
    age=20,
    phone="1234567890",
    city="Pune"
)


# ============================================================
# 32. Practical Example - Build a Profile
# ============================================================

def build_profile(**details):

    profile = {}

    for key, value in details.items():
        profile[key] = value

    return profile


profile = build_profile(
    name="Kishor",
    age=20,
    course="Python",
    city="Pune"
)

print(profile)


# ============================================================
# 33. Practical Example - Shopping Cart
# ============================================================

def shopping_cart(**items):

    total = 0

    for item, price in items.items():
        print(item, ":", price)
        total += price

    return total


total = shopping_cart(
    keyboard=1000,
    mouse=500,
    headphones=1500
)

print("Total:", total)


# ============================================================
# 34. Practical Example - API-Style Data
# ============================================================

def create_user(**user_data):

    print("Creating user...")

    for key, value in user_data.items():
        print(f"{key}: {value}")


create_user(
    username="kishor",
    email="kishor@example.com",
    age=20,
    country="India"
)


# ============================================================
# 35. Common Mistake - Positional Argument
# ============================================================

def show(**kwargs):

    print(kwargs)


# Incorrect:
#
# show(10)
#
# **kwargs accepts keyword arguments, not positional arguments.


# Correct:

show(
    number=10
)


# ============================================================
# 36. Common Mistake - Forgetting **
# ============================================================

def student(name, age):

    print(name, age)


details = {
    "name": "Kishor",
    "age": 20
}


# Correct:

student(**details)


# Without **:
#
# student(details)
#
# Python treats the dictionary as one positional argument.


# ============================================================
# 37. Common Mistake - Wrong Dictionary Keys
# ============================================================

def employee(name, age):

    print(name, age)


details = {
    "username": "Kishor",
    "age": 20
}


# This is incorrect:
#
# employee(**details)
#
# because the function expects `name`,
# but the dictionary contains `username`.


# Correct dictionary:

details = {
    "name": "Kishor",
    "age": 20
}

employee(**details)


# ============================================================
# 38. *args vs **kwargs
# ============================================================

"""
*args
-----

Accepts multiple positional arguments.

Example:

    def demo(*args):
        ...


    demo(10, 20, 30)

    args = (10, 20, 30)


**kwargs
--------

Accepts multiple keyword arguments.

Example:

    def demo(**kwargs):
        ...


    demo(
        name="Kishor",
        age=20
    )

    kwargs = {
        "name": "Kishor",
        "age": 20
    }


Quick comparison:

    *args       -> tuple
    **kwargs    -> dictionary
    *           -> positional unpacking
    **          -> keyword unpacking
"""


# ============================================================
# 39. Mini Practice
# ============================================================

# Practice 1:
# Create a function using **kwargs that prints all
# key-value pairs.


# Practice 2:
# Create a function that accepts a name and **details.
# Display the name and all additional details.


# Practice 3:
# Create a function that uses **kwargs to calculate the
# total price of multiple products.


# Practice 4:
# Create a dictionary containing:
#
# name
# age
# city
#
# Pass it to a function using **.


# Practice 5:
# Create a function that checks whether "email" exists
# in **kwargs.


# Practice 6:
# Create a function that accepts:
#
# name
# *skills
# **details
#
# Display all information.


# Practice 7:
# Create a flexible configuration function using **kwargs.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
1. **kwargs allows a function to accept any number of
   keyword arguments.

2. **kwargs stores arguments in a dictionary.

3. Example:

       def demo(**kwargs):
           print(kwargs)

4. Keyword arguments can be accessed using dictionary syntax.

5. `.get()` is useful when a key may not exist.

6. We can loop through kwargs using `.items()`.

7. A normal parameter can be combined with **kwargs.

8. **kwargs can be combined with *args.

9. `**` can unpack a dictionary into keyword arguments.

10. Dictionary keys must match the target function's
    parameter names when using ** unpacking.

11. *args handles positional arguments.

12. **kwargs handles keyword arguments.

13. `args` and `kwargs` are conventions; the `*` and `**`
    are what provide the special behavior.
"""
