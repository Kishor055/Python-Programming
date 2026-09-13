"""
06 - *args
==========

Sometimes we don't know how many positional arguments a
function will receive.

Python provides *args for this situation.

*args
-----
`*args` allows a function to accept any number of
positional arguments.

The arguments are collected into a tuple.

Syntax:

    def function_name(*args):
        ...


Example:

    def numbers(*args):
        print(args)

    numbers(10, 20, 30)

Output:

    (10, 20, 30)
"""


# ============================================================
# 1. Basic *args
# ============================================================

def show_numbers(*args):
    print(args)


show_numbers(10)
show_numbers(10, 20)
show_numbers(10, 20, 30, 40)


# ============================================================
# 2. *args Stores Values in a Tuple
# ============================================================

def check_args(*args):
    print("Arguments:", args)
    print("Type:", type(args))


check_args(10, 20, 30)


# Output:
#
# Arguments: (10, 20, 30)
# Type: <class 'tuple'>


# ============================================================
# 3. Loop Through *args
# ============================================================

def print_values(*args):

    for value in args:
        print(value)


print_values(10, 20, 30, 40, 50)


# ============================================================
# 4. Any Number of Arguments
# ============================================================

def display(*args):

    print("Number of arguments:", len(args))

    for value in args:
        print("Value:", value)


display()
display(10)
display(10, 20)
display(10, 20, 30, 40)


# ============================================================
# 5. Sum of Any Number of Numbers
# ============================================================

def total(*numbers):

    result = 0

    for number in numbers:
        result += number

    return result


print("Total:", total(10, 20))
print("Total:", total(10, 20, 30))
print("Total:", total(1, 2, 3, 4, 5))


# ============================================================
# 6. Using Built-in sum()
# ============================================================

def calculate_total(*numbers):
    return sum(numbers)


print(calculate_total(10, 20, 30))
print(calculate_total(1, 2, 3, 4, 5, 6))


# ============================================================
# 7. Average Using *args
# ============================================================

def average(*numbers):

    if len(numbers) == 0:
        return 0

    return sum(numbers) / len(numbers)


print("Average:", average(10, 20))
print("Average:", average(10, 20, 30))
print("Average:", average(10, 20, 30, 40, 50))


# ============================================================
# 8. Maximum Using *args
# ============================================================

def maximum(*numbers):

    if not numbers:
        return None

    largest = numbers[0]

    for number in numbers:

        if number > largest:
            largest = number

    return largest


print("Maximum:", maximum(10, 50, 20, 40))
print("Maximum:", maximum(100, 25, 75, 10))


# ============================================================
# 9. Minimum Using *args
# ============================================================

def minimum(*numbers):

    if not numbers:
        return None

    smallest = numbers[0]

    for number in numbers:

        if number < smallest:
            smallest = number

    return smallest


print("Minimum:", minimum(10, 50, 20, 40))
print("Minimum:", minimum(100, 25, 75, 10))


# ============================================================
# 10. *args with a Normal Parameter
# ============================================================

"""
A normal parameter can come before *args.

Example:

    def student(name, *subjects):
        ...

The first argument goes to `name`.

The remaining positional arguments go into `subjects`.
"""


def student(name, *subjects):

    print("Student:", name)
    print("Subjects:", subjects)


student(
    "Kishor",
    "Python",
    "SQL",
    "Git"
)


# ============================================================
# 11. Loop Through Remaining Arguments
# ============================================================

def student_subjects(name, *subjects):

    print("Student:", name)

    for subject in subjects:
        print("-", subject)


student_subjects(
    "Kishor",
    "Python",
    "SQL",
    "Git",
    "Linux"
)


# ============================================================
# 12. Practical Example - Student Marks
# ============================================================

def student_average(name, *marks):

    if not marks:
        return f"{name} has no marks."

    total_marks = sum(marks)
    average_marks = total_marks / len(marks)

    return average_marks


print(
    "Average:",
    student_average(
        "Kishor",
        80,
        90,
        75,
        85
    )
)


# ============================================================
# 13. Practical Example - Shopping Cart
# ============================================================

def shopping_cart(*prices):

    total = sum(prices)

    return total


print(
    "Cart Total:",
    shopping_cart(
        100,
        250,
        500
    )
)


print(
    "Cart Total:",
    shopping_cart(
        100,
        250,
        500,
        150,
        75
    )
)


# ============================================================
# 14. Practical Example - Product Prices
# ============================================================

def calculate_bill(*prices):

    total = 0

    for price in prices:
        total += price

    return total


bill = calculate_bill(
    100,
    250,
    75,
    500
)

print("Bill:", bill)


# ============================================================
# 15. Passing No Arguments
# ============================================================

def test(*args):

    print("Arguments:", args)
    print("Count:", len(args))


test()


# Output:
#
# Arguments: ()
# Count: 0


# ============================================================
# 16. Accessing Individual *args Values
# ============================================================

def show_first(*args):

    if args:
        print("First:", args[0])


show_first(10, 20, 30)


# *args is a tuple, so we can use indexing.

def show_values(*args):

    if len(args) >= 3:
        print("First:", args[0])
        print("Second:", args[1])
        print("Third:", args[2])


show_values(10, 20, 30)


# ============================================================
# 17. Slicing *args
# ============================================================

def show_slices(*args):

    print("All:", args)
    print("First two:", args[:2])
    print("Last two:", args[-2:])


show_slices(
    10,
    20,
    30,
    40,
    50
)


# ============================================================
# 18. *args with Different Data Types
# ============================================================

def display_values(*args):

    for value in args:
        print(value, type(value))


display_values(
    10,
    "Python",
    10.5,
    True,
    [1, 2, 3]
)


# ============================================================
# 19. *args Does Not Mean "Only Numbers"
# ============================================================

def display(*args):

    for value in args:
        print(value)


display(
    "Python",
    "Java",
    "C++",
    "JavaScript"
)


# ============================================================
# 20. Unpacking a List Using *
# ============================================================

numbers = [10, 20, 30, 40]


def add(a, b, c, d):
    return a + b + c + d


# Normal call:

print(add(10, 20, 30, 40))


# Using unpacking:

print(add(*numbers))


"""
`*numbers` unpacks the list.

This:

    add(*numbers)

is equivalent to:

    add(10, 20, 30, 40)
"""


# ============================================================
# 21. Unpacking a Tuple
# ============================================================

values = (5, 10, 15)


def calculate(a, b, c):
    return a + b + c


print(calculate(*values))


# ============================================================
# 22. Passing a List to a *args Function
# ============================================================

numbers = [10, 20, 30]


def show(*args):
    print(args)


# Without unpacking:

show(numbers)

# Output:
#
# ([10, 20, 30],)


# With unpacking:

show(*numbers)

# Output:
#
# (10, 20, 30)


# Important:
#
# show(numbers)
# -> one argument: the list
#
# show(*numbers)
# -> three arguments: 10, 20, 30


# ============================================================
# 23. Practical Example - Calculate Total from a List
# ============================================================

prices = [100, 200, 300, 400]


def total_price(*prices):
    return sum(prices)


print(
    "Total:",
    total_price(*prices)
)


# ============================================================
# 24. *args with String Values
# ============================================================

def join_words(*words):

    return " ".join(words)


print(
    join_words(
        "Python",
        "is",
        "easy",
        "to",
        "learn"
    )
)


# ============================================================
# 25. Practical Example - Full Name
# ============================================================

def full_name(*names):

    return " ".join(names)


print(full_name("Kishor"))
print(full_name("Kishor", "Kumar"))
print(full_name("Kishor", "Kumar", "Patil"))


# ============================================================
# 26. Finding Even Numbers with *args
# ============================================================

def even_numbers(*numbers):

    result = []

    for number in numbers:

        if number % 2 == 0:
            result.append(number)

    return result


print(
    even_numbers(
        1, 2, 3, 4, 5, 6, 7, 8
    )
)


# ============================================================
# 27. Finding Odd Numbers with *args
# ============================================================

def odd_numbers(*numbers):

    result = []

    for number in numbers:

        if number % 2 != 0:
            result.append(number)

    return result


print(
    odd_numbers(
        1, 2, 3, 4, 5, 6, 7, 8
    )
)


# ============================================================
# 28. *args with a Default Parameter
# ============================================================

def greet(message="Hello", *names):

    for name in names:
        print(message, name)


greet(
    "Hello",
    "Kishor",
    "Rahul",
    "Priya"
)


greet(
    "Good Morning",
    "Kishor",
    "Rahul"
)


# ============================================================
# 29. Important Parameter Order
# ============================================================

"""
Correct:

    def function(name, *args):
        ...


The normal parameter comes before *args.

Example:
"""


def example(name, *values):

    print("Name:", name)
    print("Values:", values)


example(
    "Kishor",
    10,
    20,
    30
)


# ============================================================
# 30. *args with Keyword Arguments
# ============================================================

def demo(*args):

    print("Positional:", args)


demo(10, 20, 30)


# Keyword arguments cannot be collected by *args.

# For keyword arguments, Python provides **kwargs.
#
# That will be covered in the next file.


# ============================================================
# 31. Common Mistake
# ============================================================

def numbers(*args):
    print(args)


values = [10, 20, 30]


# This passes the entire list as ONE argument:

numbers(values)

# Result:
#
# ([10, 20, 30],)


# This passes each list item as a separate argument:

numbers(*values)

# Result:
#
# (10, 20, 30)


# ============================================================
# 32. Real-World Example - Logger
# ============================================================

def log_messages(*messages):

    for message in messages:
        print("[LOG]:", message)


log_messages(
    "Application started",
    "Database connected",
    "User logged in"
)


# ============================================================
# 33. Real-World Example - Total Marks
# ============================================================

def total_marks(student_name, *marks):

    total = sum(marks)

    print("Student:", student_name)
    print("Marks:", marks)
    print("Total:", total)


total_marks(
    "Kishor",
    80,
    90,
    85,
    75
)


# ============================================================
# 34. Real-World Example - Order
# ============================================================

def order(customer, *items):

    print("Customer:", customer)

    print("Items:")

    for item in items:
        print("-", item)


order(
    "Kishor",
    "Laptop",
    "Mouse",
    "Keyboard"
)


# ============================================================
# 35. Quick Comparison
# ============================================================

"""
Normal parameter
----------------

def add(a, b):
    ...

add(10, 20)


*args
-----

def add(*numbers):
    ...

add(10, 20)
add(10, 20, 30)
add(1, 2, 3, 4, 5)


Storage
-------

Normal parameters:
    Individual values

*args:
    Tuple


Example:

def demo(*args):
    print(type(args))

demo(10, 20, 30)

Output:

<class 'tuple'>
"""


# ============================================================
# 36. Mini Practice
# ============================================================

# Practice 1:
# Create a function using *args that returns the sum of
# any number of numbers.


# Practice 2:
# Create a function using *args that returns the product
# of all numbers.


# Practice 3:
# Create a function that accepts a student name and any
# number of marks and returns the highest mark.


# Practice 4:
# Create a function using *args that returns all even numbers.


# Practice 5:
# Create a function using *args that joins multiple words
# into one sentence.


# Practice 6:
# Create a shopping cart function that accepts any number
# of product prices and returns the total.


# Practice 7:
# Create a function:
#
# def employee(name, *skills):
#     ...
#
# Display the employee name and all skills.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
1. *args allows a function to accept any number of
   positional arguments.

2. *args stores the arguments as a tuple.

3. The name `args` is a convention.
   The important part is the `*`.

4. We can loop through *args.

5. We can use indexing and slicing because *args is a tuple.

6. A normal parameter can come before *args.

7. * can unpack a list or tuple into individual arguments.

8. Passing a list:
       function(numbers)

   passes the entire list as one argument.

9. Unpacking a list:
       function(*numbers)

   passes each item as a separate argument.

10. *args handles positional arguments.

11. **kwargs handles keyword arguments and will be covered
    separately.
"""
