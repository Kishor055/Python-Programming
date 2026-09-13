"""
============================================================
02_tuple_methods.py
============================================================

Python Tuples - Tuple Methods

A tuple is an ordered and immutable collection.

Unlike lists, tuples provide only TWO built-in methods:

    1. count()
    2. index()

Topics Covered:
    1. Tuple Methods Overview
    2. count() Method
    3. count() with Duplicate Values
    4. count() with Strings
    5. count() with Different Data Types
    6. index() Method
    7. index() with Duplicate Values
    8. index() with Start Position
    9. index() with Start and Stop Position
    10. Value Not Found
    11. Difference Between count() and index()
    12. Practical Examples
    13. Common Mistakes
    14. Key Takeaways

Author: Kishor
============================================================
"""


# ============================================================
# 1. TUPLE METHODS - OVERVIEW
# ============================================================

"""
Tuples are immutable.

Because tuples cannot be modified, they do not have
methods such as:

    append()
    extend()
    insert()
    remove()
    pop()
    clear()
    sort()
    reverse()

A tuple mainly provides two methods:

    count()
    index()
"""

numbers = (10, 20, 30, 20, 40, 20)

print("Tuple:", numbers)


# ============================================================
# 2. count() METHOD
# ============================================================

"""
The count() method returns the number of times a specified
value appears in a tuple.

Syntax:

    tuple.count(value)

Example:

    numbers.count(20)

If 20 appears three times, the result will be 3.
"""

numbers = (10, 20, 30, 20, 40, 20)

result = numbers.count(20)

print("\nTuple:", numbers)
print("Count of 20:", result)


# ============================================================
# 3. count() WITH DUPLICATE VALUES
# ============================================================

"""
Tuples allow duplicate values.

count() is useful when we want to know how many times
a particular value occurs.
"""

numbers = (1, 2, 2, 3, 2, 4, 2, 5)

print("\nTuple:", numbers)

print("Count of 1:", numbers.count(1))
print("Count of 2:", numbers.count(2))
print("Count of 3:", numbers.count(3))
print("Count of 5:", numbers.count(5))


# ============================================================
# 4. count() WITH STRINGS
# ============================================================

"""
count() can also be used with strings stored in a tuple.
"""

languages = (
    "Python",
    "Java",
    "Python",
    "C++",
    "Python"
)

print("\nLanguages:", languages)

print("Python appears:", languages.count("Python"), "times")
print("Java appears:", languages.count("Java"), "time(s)")
print("PHP appears:", languages.count("PHP"), "time(s)")


# ============================================================
# 5. count() WITH DIFFERENT DATA TYPES
# ============================================================

"""
count() can work with different data types.

It checks for matching values.
"""

data = (
    10,
    "Python",
    10,
    True,
    10.0
)

print("\nData:", data)

print("Count of 10:", data.count(10))
print("Count of 'Python':", data.count("Python"))
print("Count of True:", data.count(True))


# ============================================================
# IMPORTANT NOTE
# ============================================================

"""
Python considers some values equal during comparison.

For example:

    10 == 10.0
    True == 1

Therefore, count() can sometimes produce results that
may initially look surprising.

Example:

    data = (10, 10.0, True)

    data.count(10)

The comparison rules of Python apply.
"""

comparison_data = (10, 10.0, True)

print("\nComparison Data:", comparison_data)
print("Count of 10:", comparison_data.count(10))


# ============================================================
# 6. index() METHOD
# ============================================================

"""
The index() method returns the index position of the
FIRST occurrence of a specified value.

Syntax:

    tuple.index(value)

Example:

    numbers.index(30)

If 30 is located at index 2, the result is 2.
"""

numbers = (10, 20, 30, 40, 50)

result = numbers.index(30)

print("\nTuple:", numbers)
print("Index of 30:", result)


# ============================================================
# 7. index() WITH DUPLICATE VALUES
# ============================================================

"""
If a value appears multiple times, index() returns the
position of the FIRST occurrence.
"""

numbers = (10, 20, 30, 20, 40, 20)

print("\nTuple:", numbers)

print("Index of 20:", numbers.index(20))


# ============================================================
# 8. index() WITH START POSITION
# ============================================================

"""
index() supports an optional start argument.

Syntax:

    tuple.index(value, start)

Python starts searching from the specified index.
"""

numbers = (10, 20, 30, 20, 40, 20)

print("\nTuple:", numbers)

# Start searching from index 2
result = numbers.index(20, 2)

print("Index of 20 starting from index 2:", result)


# ============================================================
# 9. index() WITH START AND STOP POSITION
# ============================================================

"""
index() can also accept a stop position.

Syntax:

    tuple.index(value, start, stop)

The search happens from:

    start

up to, but NOT including:

    stop
"""

numbers = (10, 20, 30, 20, 40, 20)

print("\nTuple:", numbers)

result = numbers.index(20, 2, 5)

print("Index of 20 between index 2 and 4:", result)


# ============================================================
# 10. VALUE NOT FOUND
# ============================================================

"""
If index() cannot find the requested value, Python raises:

    ValueError

Example:

    numbers.index(100)

The following statement is commented out to prevent
the program from stopping.
"""

numbers = (10, 20, 30, 40)

# print(numbers.index(100))    # ValueError


# ============================================================
# SAFE WAY TO USE index()
# ============================================================

"""
Before using index(), you can check whether the value
exists using the 'in' operator.
"""

numbers = (10, 20, 30, 40)

value = 30

if value in numbers:
    print("\nIndex of", value, ":", numbers.index(value))
else:
    print("\n", value, "is not present in the tuple.")


# ============================================================
# 11. count() vs index()
# ============================================================

"""
count()
-------
Purpose:
    Counts how many times a value occurs.

Example:

    numbers.count(20)

Returns:
    Number of occurrences


index()
-------
Purpose:
    Finds the position of the first occurrence.

Example:

    numbers.index(20)

Returns:
    Index position
"""

numbers = (10, 20, 30, 20, 40, 20)

print("\nTuple:", numbers)

print("count(20):", numbers.count(20))
print("index(20):", numbers.index(20))


# ============================================================
# 12. PRACTICAL EXAMPLE - STUDENT MARKS
# ============================================================

"""
Suppose a student's marks are stored in a tuple.

We can use count() to determine how many times
a particular mark appears.
"""

marks = (85, 90, 78, 85, 92, 85, 88)

print("\nStudent Marks:", marks)

print("85 appears:", marks.count(85), "times")


# ============================================================
# PRACTICAL EXAMPLE - FIND A LANGUAGE
# ============================================================

languages = (
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "Python"
)

language = "Python"

if language in languages:
    position = languages.index(language)

    print("\nLanguage:", language)
    print("First position:", position)
else:
    print("\nLanguage not found.")


# ============================================================
# 13. PRACTICAL EXAMPLE - CHECK DUPLICATES
# ============================================================

"""
count() can be used to check whether a particular value
appears more than once.
"""

numbers = (10, 20, 30, 20, 40)

value = 20

occurrences = numbers.count(value)

print("\nTuple:", numbers)
print("Value:", value)
print("Occurrences:", occurrences)

if occurrences > 1:
    print(value, "is duplicated.")
else:
    print(value, "is not duplicated.")


# ============================================================
# 14. PRACTICAL EXAMPLE - FIRST AND SECOND OCCURRENCE
# ============================================================

"""
We can use index() with a start position to find
later occurrences of a value.
"""

numbers = (10, 20, 30, 20, 40, 20)

first_index = numbers.index(20)

# Search after the first occurrence
second_index = numbers.index(20, first_index + 1)

print("\nTuple:", numbers)

print("First occurrence of 20 :", first_index)
print("Second occurrence of 20:", second_index)


# ============================================================
# 15. FIND ALL POSITIONS OF A VALUE
# ============================================================

"""
Using a loop and index(), we can find all positions
where a value occurs.

Note:
There are simpler approaches using enumerate(), but
this example demonstrates how index() can be used.
"""

numbers = (10, 20, 30, 20, 40, 20)

value = 20
positions = []

start = 0

while True:
    try:
        position = numbers.index(value, start)
        positions.append(position)
        start = position + 1

    except ValueError:
        break

print("\nTuple:", numbers)
print("Value:", value)
print("Positions:", positions)


# ============================================================
# 16. COMMON MISTAKES
# ============================================================

"""
MISTAKE 1:
Trying to use list methods on a tuple.

Example:

    numbers.append(50)

Tuples do not support append().


MISTAKE 2:
Assuming index() returns all positions.

index() returns only the FIRST matching position
unless a start position is provided.


MISTAKE 3:
Using index() without checking whether a value exists.

Example:

    numbers.index(100)

If 100 does not exist:

    ValueError

Safer approach:

    if 100 in numbers:
        print(numbers.index(100))


MISTAKE 4:
Confusing count() with index().

count() -> Number of occurrences
index() -> Position of first occurrence
"""


# ============================================================
# 17. QUICK REFERENCE
# ============================================================

"""
TUPLE METHODS QUICK REFERENCE
-----------------------------

1. count()

Syntax:
    tuple.count(value)

Purpose:
    Returns the number of occurrences.

Example:
    numbers = (10, 20, 20, 30)
    numbers.count(20)

Result:
    2


2. index()

Syntax:
    tuple.index(value)

Purpose:
    Returns the index of the first occurrence.

Example:
    numbers = (10, 20, 30)
    numbers.index(20)

Result:
    1


3. index() with start

Syntax:
    tuple.index(value, start)


4. index() with start and stop

Syntax:
    tuple.index(value, start, stop)


IMPORTANT:

    index() -> raises ValueError if value is not found.
    count() -> returns 0 if value is not found.
"""


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
KEY TAKEAWAYS

1. Tuples are immutable.
2. Tuples provide two main methods:
       - count()
       - index()

3. count(value):
       Counts occurrences of a value.

4. index(value):
       Returns the first index of a value.

5. index(value, start):
       Starts searching from a specified position.

6. index(value, start, stop):
       Searches within a specified range.

7. count() returns 0 when the value is absent.

8. index() raises ValueError when the value is absent.

9. count() and index() do not modify the tuple.

10. The original tuple remains unchanged.
"""
