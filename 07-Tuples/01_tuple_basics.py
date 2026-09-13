"""
============================================================
01_tuple_basics.py
============================================================

Python Tuples - Basics

A tuple is an ordered and immutable collection of elements.

Topics Covered:
    1. Creating a tuple
    2. Empty tuple
    3. Single-element tuple
    4. Multiple-element tuple
    5. Tuple with different data types
    6. Checking tuple type
    7. Tuple indexing
    8. Negative indexing
    9. Tuple immutability
    10. Tuple length
    11. Membership operators
    12. Tuple concatenation
    13. Tuple repetition
    14. Practical example

Author: Kishor
============================================================
"""


# ============================================================
# 1. CREATING A TUPLE
# ============================================================

"""
A tuple is normally created using parentheses ().

Syntax:

    tuple_name = (value1, value2, value3)
"""

numbers = (10, 20, 30, 40, 50)

print("Numbers:", numbers)


# ============================================================
# 2. EMPTY TUPLE
# ============================================================

"""
An empty tuple contains no elements.

Syntax:

    empty_tuple = ()
"""

empty_tuple = ()

print("Empty Tuple:", empty_tuple)
print("Type:", type(empty_tuple))


# ============================================================
# 3. SINGLE-ELEMENT TUPLE
# ============================================================

"""
A single-element tuple MUST contain a comma.

Correct:

    (10,)

Incorrect:

    (10)

The comma is what makes it a tuple.
"""

single_tuple = (10,)

print("\nSingle-element Tuple:", single_tuple)
print("Type:", type(single_tuple))


# (10) is NOT a tuple.
# It is simply an integer inside parentheses.

not_a_tuple = (10)

print("Without comma:", not_a_tuple)
print("Type:", type(not_a_tuple))


# ============================================================
# 4. MULTIPLE-ELEMENT TUPLE
# ============================================================

"""
A tuple can contain multiple elements.
"""

fruits = ("Apple", "Banana", "Mango", "Orange")

print("\nFruits:", fruits)


# ============================================================
# 5. TUPLE WITH DIFFERENT DATA TYPES
# ============================================================

"""
A tuple can contain different Python data types.
"""

student = (
    101,          # int
    "Kishor",     # str
    21,           # int
    85.5,         # float
    True          # bool
)

print("\nStudent:", student)


# ============================================================
# 6. CHECKING TUPLE TYPE
# ============================================================

"""
The type() function tells us the data type of an object.
"""

data = (10, 20, 30)

print("\nData:", data)
print("Data Type:", type(data))


# ============================================================
# 7. TUPLE INDEXING
# ============================================================

"""
Tuples are ordered collections.

Indexing starts from 0.

Example:

    Tuple:     10    20    30    40    50
    Index:      0     1     2     3     4
"""

numbers = (10, 20, 30, 40, 50)

print("\nTuple:", numbers)

print("First element :", numbers[0])
print("Second element:", numbers[1])
print("Third element :", numbers[2])
print("Last element  :", numbers[4])


# ============================================================
# 8. NEGATIVE INDEXING
# ============================================================

"""
Python also supports negative indexing.

Example:

    Tuple:          10    20    30    40    50
    Negative Index: -5    -4    -3    -2    -1
"""

numbers = (10, 20, 30, 40, 50)

print("\nTuple:", numbers)

print("Last element       :", numbers[-1])
print("Second-last element:", numbers[-2])
print("First element       :", numbers[-5])


# ============================================================
# 9. TUPLE IMMUTABILITY
# ============================================================

"""
Tuples are IMMUTABLE.

Immutable means that once a tuple is created,
its elements cannot be changed.

Example:

    numbers[0] = 100

This produces:

    TypeError:
    'tuple' object does not support item assignment

The following statement is intentionally commented out.
"""

numbers = (10, 20, 30)

# numbers[0] = 100    # TypeError

print("\nOriginal Tuple:", numbers)


# ============================================================
# 10. LENGTH OF A TUPLE
# ============================================================

"""
The len() function returns the number of elements
in a tuple.
"""

numbers = (10, 20, 30, 40, 50)

print("\nTuple:", numbers)
print("Number of elements:", len(numbers))


# ============================================================
# 11. MEMBERSHIP OPERATORS
# ============================================================

"""
The 'in' operator checks whether an element exists
inside the tuple.

The 'not in' operator checks whether an element does
not exist inside the tuple.
"""

languages = ("Python", "Java", "C++", "JavaScript")

print("\nLanguages:", languages)

print("Python" in languages)
print("PHP" in languages)

print("PHP" not in languages)


# ============================================================
# 12. TUPLE CONCATENATION
# ============================================================

"""
The + operator can combine two tuples.

A NEW tuple is created.

The original tuples remain unchanged.
"""

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combined = tuple1 + tuple2

print("\nTuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Combined:", combined)


# ============================================================
# 13. TUPLE REPETITION
# ============================================================

"""
The * operator repeats the elements of a tuple.
"""

numbers = (1, 2, 3)

repeated = numbers * 3

print("\nOriginal:", numbers)
print("Repeated:", repeated)


# ============================================================
# 14. PRACTICAL EXAMPLE
# ============================================================

"""
Tuples are useful for storing fixed information.

Example:
A student record can be represented using a tuple.
"""

student = (
    101,
    "Kishor",
    "Python",
    85
)

print("\nStudent Record")
print("--------------")
print("Roll No :", student[0])
print("Name    :", student[1])
print("Course  :", student[2])
print("Marks   :", student[3])


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
KEY TAKEAWAYS

1. Tuple is an ordered collection.
2. Tuple is immutable.
3. Tuple allows duplicate values.
4. Tuple can contain different data types.
5. Tuple supports indexing.
6. Tuple supports negative indexing.
7. len() returns the number of elements.
8. 'in' and 'not in' can be used with tuples.
9. '+' combines tuples.
10. '*' repeats tuples.
11. A single-element tuple requires a comma.

Example:

    single = (10,)

NOT:

    single = (10)
"""
