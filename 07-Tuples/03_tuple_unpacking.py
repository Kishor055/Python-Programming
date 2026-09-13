"""
============================================================
03_tuple_unpacking.py
============================================================

Python Tuples - Packing & Unpacking

Tuple unpacking is the process of assigning the individual
elements of a tuple to separate variables.

Topics Covered:
    1. What is Tuple Unpacking?
    2. Basic Tuple Unpacking
    3. Number of Variables Must Match
    4. Multiple Assignment
    5. Ignoring Values Using _
    6. Extended Unpacking Using *
    7. *args Style Unpacking
    8. Unpacking with First and Last Values
    9. Nested Tuple Unpacking
    10. Unpacking in for Loops
    11. Function Return Values
    12. Swapping Variables
    13. Star Unpacking Rules
    14. Common Errors
    15. Practical Examples
    16. Key Takeaways

Author: Kishor
============================================================
"""


# ============================================================
# 1. WHAT IS TUPLE UNPACKING?
# ============================================================

"""
Tuple unpacking means assigning the elements of a tuple
to individual variables.

Example:

    student = ("Kishor", 21, "Python")

    name, age, language = student

The values are assigned as:

    name     -> "Kishor"
    age      -> 21
    language -> "Python"
"""

student = ("Kishor", 21, "Python")

name, age, language = student

print("Name    :", name)
print("Age     :", age)
print("Language:", language)


# ============================================================
# 2. BASIC TUPLE UNPACKING
# ============================================================

"""
The number of variables should normally match the number
of elements in the tuple.
"""

numbers = (10, 20, 30)

a, b, c = numbers

print("\nA:", a)
print("B:", b)
print("C:", c)


# ============================================================
# 3. NUMBER OF VARIABLES MUST MATCH
# ============================================================

"""
Correct:

    (10, 20, 30)
    a, b, c

Three values -> Three variables


Incorrect:

    (10, 20, 30)
    a, b

Two variables cannot receive three values.

This produces:

    ValueError: too many values to unpack
"""

numbers = (10, 20, 30)

# a, b = numbers    # ValueError


"""
Another incorrect example:

    (10, 20)
    a, b, c

This produces:

    ValueError: not enough values to unpack
"""

numbers = (10, 20)

# a, b, c = numbers    # ValueError


# ============================================================
# 4. MULTIPLE ASSIGNMENT
# ============================================================

"""
Python allows multiple variables to be assigned
in a single statement.

This is closely related to tuple packing and unpacking.
"""

name, age, city = "Kishor", 21, "Pune"

print("\nName:", name)
print("Age :", age)
print("City:", city)


"""
Conceptually, Python can treat the right side as:

    ("Kishor", 21, "Pune")

and then unpack the values into:

    name, age, city
"""


# ============================================================
# 5. IGNORING VALUES USING _
# ============================================================

"""
Sometimes we do not need every value.

By convention, '_' is used for a value that we want
to ignore.
"""

student = ("Kishor", 21, "Python")

name, _, language = student

print("\nName    :", name)
print("Language:", language)


"""
Here:

    name     -> "Kishor"
    _        -> 21
    language -> "Python"

The underscore tells the reader:

    "This value is intentionally not needed."
"""


# ============================================================
# 6. EXTENDED UNPACKING USING *
# ============================================================

"""
Python provides the * operator for extended unpacking.

It allows one variable to collect multiple elements.

Example:

    numbers = (10, 20, 30, 40, 50)

    first, *middle, last = numbers

Result:

    first  -> 10
    middle -> [20, 30, 40]
    last   -> 50
"""

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print("\nFirst :", first)
print("Middle:", middle)
print("Last  :", last)


# ============================================================
# 7. STAR UNPACKING - FIRST VALUE
# ============================================================

"""
The * variable collects all remaining values.
"""

numbers = (10, 20, 30, 40, 50)

first, *remaining = numbers

print("\nFirst:", first)
print("Remaining:", remaining)


# Output:
#
# First: 10
# Remaining: [20, 30, 40, 50]


# ============================================================
# 8. STAR UNPACKING - LAST VALUE
# ============================================================

"""
We can also keep the last value separately.
"""

numbers = (10, 20, 30, 40, 50)

*remaining, last = numbers

print("\nRemaining:", remaining)
print("Last:", last)


# ============================================================
# 9. STAR UNPACKING - FIRST, MIDDLE, LAST
# ============================================================

numbers = (10, 20, 30, 40, 50, 60)

first, *middle, last = numbers

print("\nFirst :", first)
print("Middle:", middle)
print("Last  :", last)


# ============================================================
# 10. STAR UNPACKING WITH TWO VARIABLES
# ============================================================

"""
The starred variable receives the remaining values.

Example:

    first, second, *remaining = numbers
"""

numbers = (10, 20, 30, 40, 50)

first, second, *remaining = numbers

print("\nFirst :", first)
print("Second:", second)
print("Remaining:", remaining)


# ============================================================
# 11. STARRED VARIABLE BECOMES A LIST
# ============================================================

"""
Important:

Even if the original object is a tuple, the starred
variable receives a LIST.

Example:

    numbers = (10, 20, 30, 40)

    first, *rest = numbers

    type(rest) -> list
"""

numbers = (10, 20, 30, 40)

first, *rest = numbers

print("\nFirst:", first)
print("Rest:", rest)
print("Type of rest:", type(rest))


# ============================================================
# 12. NESTED TUPLE UNPACKING
# ============================================================

"""
Tuples can contain other tuples.

Nested structures can also be unpacked.
"""

student = (
    "Kishor",
    (21, "Python")
)

name, (age, language) = student

print("\nName    :", name)
print("Age     :", age)
print("Language:", language)


# ============================================================
# 13. NESTED TUPLE PRACTICAL EXAMPLE
# ============================================================

students = (
    ("Kishor", 85),
    ("Rahul", 90),
    ("Amit", 78)
)

for name, marks in students:
    print(name, "->", marks)


# ============================================================
# 14. UNPACKING IN FOR LOOPS
# ============================================================

"""
If each element of a tuple contains multiple values,
we can unpack them directly inside a for loop.
"""

employees = (
    ("Kishor", "Developer", 75000),
    ("Rahul", "Tester", 65000),
    ("Amit", "Designer", 70000)
)

for name, role, salary in employees:
    print("\nName  :", name)
    print("Role  :", role)
    print("Salary:", salary)


# ============================================================
# 15. FUNCTION RETURN VALUES
# ============================================================

"""
Functions can return multiple values.

Python automatically packs the returned values into
a tuple.
"""

def get_student():
    return "Kishor", 21, "Python"


student = get_student()

print("\nReturned Value:", student)
print("Type:", type(student))


# The returned tuple can be unpacked.

name, age, language = get_student()

print("\nName    :", name)
print("Age     :", age)
print("Language:", language)


# ============================================================
# 16. PRACTICAL FUNCTION EXAMPLE
# ============================================================

def calculate(a, b):
    total = a + b
    difference = a - b
    product = a * b

    return total, difference, product


result = calculate(10, 5)

total, difference, product = result

print("\nCalculation")
print("-----------")
print("Total     :", total)
print("Difference:", difference)
print("Product   :", product)


# ============================================================
# 17. VARIABLE SWAPPING
# ============================================================

"""
Tuple unpacking makes swapping variables very simple.

Traditional approach:

    temp = a
    a = b
    b = temp

Python approach:

    a, b = b, a
"""

a = 10
b = 20

print("\nBefore Swapping")
print("A:", a)
print("B:", b)

a, b = b, a

print("\nAfter Swapping")
print("A:", a)
print("B:", b)


# ============================================================
# 18. REVERSE VALUES USING UNPACKING
# ============================================================

numbers = (10, 20, 30, 40)

a, b, c, d = numbers

print("\nOriginal values:")
print(a, b, c, d)

a, b, c, d = d, c, b, a

print("Reversed values:")
print(a, b, c, d)


# ============================================================
# 19. UNPACKING WITH RANGE
# ============================================================

"""
Any iterable can generally participate in unpacking,
not just tuples.
"""

numbers = range(1, 6)

a, b, c, d, e = numbers

print("\nA:", a)
print("B:", b)
print("C:", c)
print("D:", d)
print("E:", e)


# ============================================================
# 20. UNPACKING A STRING
# ============================================================

"""
Strings are iterable, so their characters can also
be unpacked.
"""

word = "CAT"

first, second, third = word

print("\nFirst :", first)
print("Second:", second)
print("Third :", third)


# ============================================================
# 21. STAR UNPACKING WITH A STRING
# ============================================================

word = "PYTHON"

first, *middle, last = word

print("\nFirst :", first)
print("Middle:", middle)
print("Last  :", last)


# ============================================================
# 22. COMMON ERROR - TOO MANY VALUES
# ============================================================

"""
Example:

    numbers = (10, 20, 30)

    a, b = numbers

There are 3 values but only 2 variables.

Result:

    ValueError: too many values to unpack
"""

numbers = (10, 20, 30)

# a, b = numbers


# ============================================================
# 23. COMMON ERROR - NOT ENOUGH VALUES
# ============================================================

"""
Example:

    numbers = (10, 20)

    a, b, c = numbers

There are only 2 values but 3 variables.

Result:

    ValueError: not enough values to unpack
"""

numbers = (10, 20)

# a, b, c = numbers


# ============================================================
# 24. COMMON ERROR - MULTIPLE STARRED VARIABLES
# ============================================================

"""
Only ONE starred variable is allowed in a single
unpacking assignment.

Incorrect:

    a, *b, *c = numbers

This produces a SyntaxError.

Correct:

    a, *b, c = numbers
"""

numbers = (10, 20, 30, 40)

a, *b, c = numbers

print("\nA:", a)
print("B:", b)
print("C:", c)


# ============================================================
# 25. PRACTICAL EXAMPLE - STUDENT DATA
# ============================================================

"""
Suppose we have student information:

    (roll_no, name, age, course, marks)

We can unpack the record into meaningful variables.
"""

student = (
    101,
    "Kishor",
    21,
    "Python",
    85
)

roll_no, name, age, course, marks = student

print("\nStudent Information")
print("-------------------")
print("Roll No:", roll_no)
print("Name   :", name)
print("Age    :", age)
print("Course :", course)
print("Marks  :", marks)


# ============================================================
# 26. PRACTICAL EXAMPLE - FIRST AND LAST
# ============================================================

"""
Extended unpacking is useful when we care about the
first and last elements but want to collect everything
in between.
"""

numbers = (10, 20, 30, 40, 50, 60, 70)

first, *middle, last = numbers

print("\nFirst value :", first)
print("Middle values:", middle)
print("Last value  :", last)


# ============================================================
# 27. PRACTICAL EXAMPLE - IGNORE UNNECESSARY DATA
# ============================================================

employee = (
    101,
    "Kishor",
    "Developer",
    75000
)

employee_id, name, _, salary = employee

print("\nEmployee ID:", employee_id)
print("Name:", name)
print("Salary:", salary)


# ============================================================
# 28. PACKING VS UNPACKING
# ============================================================

"""
PACKING
-------

Multiple values are combined into one tuple.

Example:

    student = "Kishor", 21, "Python"


UNPACKING
---------

Elements from a tuple are assigned to multiple variables.

Example:

    name, age, language = student


In short:

    Packing:
        Many values -> One tuple

    Unpacking:
        One tuple -> Many variables
"""

student = "Kishor", 21, "Python"

print("\nPacked:", student)

name, age, language = student

print("Unpacked:")
print(name)
print(age)
print(language)


# ============================================================
# 29. QUICK REFERENCE
# ============================================================

"""
TUPLE UNPACKING QUICK REFERENCE
------------------------------

Basic unpacking:

    a, b, c = (10, 20, 30)


Ignore a value:

    a, _, c = (10, 20, 30)


First + remaining:

    first, *rest = (10, 20, 30, 40)


Remaining + last:

    *rest, last = (10, 20, 30, 40)


First + middle + last:

    first, *middle, last = (10, 20, 30, 40)


Nested unpacking:

    (a, (b, c)) = (10, (20, 30))


Function return:

    def get_data():
        return 10, 20

    a, b = get_data()


Variable swapping:

    a, b = b, a
"""


# ============================================================
# 30. KEY TAKEAWAYS
# ============================================================

"""
KEY TAKEAWAYS

1. Tuple unpacking assigns tuple elements to variables.

2. The number of variables must normally match the
   number of values.

3. The underscore (_) is commonly used to ignore values.

4. The * operator enables extended unpacking.

5. A starred variable collects multiple values.

6. A starred variable always receives a list.

7. Only one starred variable can be used in an
   unpacking assignment.

8. Nested tuples can be unpacked.

9. Tuples returned from functions can be unpacked.

10. Tuple unpacking makes variable swapping easy.

11. Unpacking works with other iterables such as:
        - Lists
        - Strings
        - Ranges
        - Other iterable objects

12. Tuple packing and unpacking are fundamental Python
    concepts used throughout real-world Python programs.
"""
