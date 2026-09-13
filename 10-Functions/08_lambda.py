"""
08 - Lambda Functions
=====================

A lambda function is a small anonymous function.

Unlike a normal function created with `def`, a lambda
function is usually written in a single line.

Syntax:

    lambda arguments: expression


Example:

    square = lambda x: x ** 2

    print(square(5))

Output:
    25


Important:
----------
lambda functions are useful for short, simple operations.

Use `def` when the function contains more complex logic.
"""


# ============================================================
# 1. Basic Lambda Function
# ============================================================

square = lambda x: x ** 2

print(square(5))
print(square(10))


# ============================================================
# 2. Lambda with One Argument
# ============================================================

double = lambda x: x * 2

print(double(5))
print(double(10))
print(double(25))


# ============================================================
# 3. Lambda with Two Arguments
# ============================================================

add = lambda a, b: a + b

print(add(10, 20))
print(add(100, 200))


# ============================================================
# 4. Lambda with Multiple Arguments
# ============================================================

calculate = lambda a, b, c: a + b + c

print(calculate(10, 20, 30))


# ============================================================
# 5. Lambda vs Normal Function
# ============================================================

# Normal function

def square_function(x):
    return x ** 2


print(square_function(5))


# Lambda function

square_lambda = lambda x: x ** 2

print(square_lambda(5))


"""
Both produce the same result.

Normal function:

    def square_function(x):
        return x ** 2


Lambda:

    lambda x: x ** 2
"""


# ============================================================
# 6. Lambda with No Arguments
# ============================================================

message = lambda: "Hello, Python!"

print(message())


# ============================================================
# 7. Lambda with Strings
# ============================================================

greet = lambda name: "Hello, " + name

print(greet("Kishor"))
print(greet("Rahul"))


# ============================================================
# 8. Lambda with String Length
# ============================================================

length = lambda text: len(text)

print(length("Python"))
print(length("Functions"))


# ============================================================
# 9. Lambda for Even and Odd
# ============================================================

even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"

print(even_odd(10))
print(even_odd(7))


# ============================================================
# 10. Lambda with Conditional Expression
# ============================================================

check_age = lambda age: "Adult" if age >= 18 else "Minor"

print(check_age(20))
print(check_age(15))


# ============================================================
# 11. Lambda for Maximum
# ============================================================

maximum = lambda a, b: a if a > b else b

print(maximum(10, 20))
print(maximum(50, 30))


# ============================================================
# 12. Lambda for Minimum
# ============================================================

minimum = lambda a, b: a if a < b else b

print(minimum(10, 20))
print(minimum(50, 30))


# ============================================================
# 13. Lambda with Default Argument
# ============================================================

greet = lambda name="Kishor": "Hello " + name

print(greet())
print(greet("Rahul"))


# ============================================================
# 14. Lambda with Multiple Operations
# ============================================================

calculate = lambda a, b: (a + b) * 2

print(calculate(10, 20))


# ============================================================
# 15. Lambda with Built-in Functions
# ============================================================

numbers = [1, 2, 3, 4, 5]

squared = list(
    map(lambda x: x ** 2, numbers)
)

print(squared)


# ============================================================
# 16. Lambda with map()
# ============================================================

"""
map() applies a function to every item in an iterable.

Syntax:

    map(function, iterable)
"""


numbers = [1, 2, 3, 4, 5]

doubled = list(
    map(lambda x: x * 2, numbers)
)

print(doubled)


# Output:
#
# [2, 4, 6, 8, 10]


# ============================================================
# 17. Lambda with map() - Strings
# ============================================================

names = [
    "kishor",
    "rahul",
    "priya"
]

uppercase_names = list(
    map(lambda name: name.upper(), names)
)

print(uppercase_names)


# ============================================================
# 18. Lambda with map() - Add Two Lists
# ============================================================

numbers1 = [1, 2, 3, 4]
numbers2 = [10, 20, 30, 40]

result = list(
    map(
        lambda a, b: a + b,
        numbers1,
        numbers2
    )
)

print(result)


# ============================================================
# 19. Lambda with filter()
# ============================================================

"""
filter() selects elements for which a function returns True.

Syntax:

    filter(function, iterable)
"""


numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(
    filter(
        lambda x: x % 2 == 0,
        numbers
    )
)

print(even_numbers)


# ============================================================
# 20. Filter Odd Numbers
# ============================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

odd_numbers = list(
    filter(
        lambda x: x % 2 != 0,
        numbers
    )
)

print(odd_numbers)


# ============================================================
# 21. Filter Numbers Greater Than 10
# ============================================================

numbers = [5, 12, 8, 20, 3, 25]

greater_than_10 = list(
    filter(
        lambda x: x > 10,
        numbers
    )
)

print(greater_than_10)


# ============================================================
# 22. Filter Strings
# ============================================================

names = [
    "Kishor",
    "Rahul",
    "Amit",
    "Priya"
]

long_names = list(
    filter(
        lambda name: len(name) > 5,
        names
    )
)

print(long_names)


# ============================================================
# 23. Lambda with sorted()
# ============================================================

"""
sorted() can use a lambda function as its `key`.

This is one of the most common real-world uses of lambda.
"""


numbers = [40, 10, 30, 20, 50]

result = sorted(
    numbers,
    key=lambda x: x
)

print(result)


# ============================================================
# 24. Sort by Absolute Value
# ============================================================

numbers = [-10, 5, -3, 8, -1]

result = sorted(
    numbers,
    key=lambda x: abs(x)
)

print(result)


# ============================================================
# 25. Sort Strings by Length
# ============================================================

words = [
    "Python",
    "AI",
    "Programming",
    "Code",
    "Function"
]

result = sorted(
    words,
    key=lambda word: len(word)
)

print(result)


# ============================================================
# 26. Sort Strings in Reverse by Length
# ============================================================

words = [
    "Python",
    "AI",
    "Programming",
    "Code",
    "Function"
]

result = sorted(
    words,
    key=lambda word: len(word),
    reverse=True
)

print(result)


# ============================================================
# 27. Lambda with List of Tuples
# ============================================================

students = [
    ("Kishor", 85),
    ("Rahul", 92),
    ("Priya", 78),
    ("Amit", 88)
]

students_sorted = sorted(
    students,
    key=lambda student: student[1]
)

print(students_sorted)


# ============================================================
# 28. Sort Students by Marks - Highest First
# ============================================================

students = [
    ("Kishor", 85),
    ("Rahul", 92),
    ("Priya", 78),
    ("Amit", 88)
]

students_sorted = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print(students_sorted)


# ============================================================
# 29. Sort Students by Name
# ============================================================

students = [
    ("Kishor", 85),
    ("Rahul", 92),
    ("Priya", 78),
    ("Amit", 88)
]

students_sorted = sorted(
    students,
    key=lambda student: student[0]
)

print(students_sorted)


# ============================================================
# 30. Lambda with Dictionaries
# ============================================================

students = [
    {"name": "Kishor", "marks": 85},
    {"name": "Rahul", "marks": 92},
    {"name": "Priya", "marks": 78}
]

students_sorted = sorted(
    students,
    key=lambda student: student["marks"]
)

print(students_sorted)


# ============================================================
# 31. Sort Dictionary Data by Marks
# ============================================================

students = [
    {"name": "Kishor", "marks": 85},
    {"name": "Rahul", "marks": 92},
    {"name": "Priya", "marks": 78}
]

students_sorted = sorted(
    students,
    key=lambda student: student["marks"],
    reverse=True
)

for student in students_sorted:
    print(student)


# ============================================================
# 32. Lambda with max()
# ============================================================

numbers = [10, 50, 20, 40, 30]

largest = max(
    numbers,
    key=lambda x: x
)

print(largest)


# ============================================================
# 33. Lambda with min()
# ============================================================

numbers = [10, 50, 20, 40, 30]

smallest = min(
    numbers,
    key=lambda x: x
)

print(smallest)


# ============================================================
# 34. Find Student with Highest Marks
# ============================================================

students = [
    ("Kishor", 85),
    ("Rahul", 92),
    ("Priya", 78)
]

top_student = max(
    students,
    key=lambda student: student[1]
)

print(top_student)


# ============================================================
# 35. Find Student with Lowest Marks
# ============================================================

students = [
    ("Kishor", 85),
    ("Rahul", 92),
    ("Priya", 78)
]

lowest_student = min(
    students,
    key=lambda student: student[1]
)

print(lowest_student)


# ============================================================
# 36. Lambda with reduce()
# ============================================================

"""
reduce() is available from functools.

It repeatedly applies a function to the elements.

Example:

    1 + 2 + 3 + 4

First:
    1 + 2 = 3

Then:
    3 + 3 = 6

Then:
    6 + 4 = 10
"""

from functools import reduce


numbers = [1, 2, 3, 4, 5]

total = reduce(
    lambda a, b: a + b,
    numbers
)

print(total)


# ============================================================
# 37. reduce() for Multiplication
# ============================================================

numbers = [1, 2, 3, 4, 5]

product = reduce(
    lambda a, b: a * b,
    numbers
)

print(product)


# ============================================================
# 38. Lambda with reduce() - Maximum
# ============================================================

numbers = [10, 50, 20, 40, 30]

largest = reduce(
    lambda a, b: a if a > b else b,
    numbers
)

print(largest)


# ============================================================
# 39. Lambda Inside a Function
# ============================================================

def create_multiplier(number):

    return lambda x: x * number


double = create_multiplier(2)
triple = create_multiplier(3)

print(double(10))
print(triple(10))


"""
The lambda remembers `number`.

This is an example of a closure.
"""


# ============================================================
# 40. Practical Example - Tax Calculator
# ============================================================

tax = lambda price: price * 0.18

print("Tax:", tax(1000))
print("Tax:", tax(5000))


# ============================================================
# 41. Practical Example - Discount Calculator
# ============================================================

discount = lambda price, percentage: (
    price - (price * percentage / 100)
)

print(discount(1000, 10))
print(discount(5000, 20))


# ============================================================
# 42. Practical Example - Grade
# ============================================================

grade = lambda marks: (
    "A" if marks >= 90
    else "B" if marks >= 75
    else "C" if marks >= 60
    else "D"
)

print(grade(95))
print(grade(82))
print(grade(65))
print(grade(40))


# ============================================================
# 43. Practical Example - Login Status
# ============================================================

login_status = lambda logged_in: (
    "Welcome!" if logged_in else "Please login."
)

print(login_status(True))
print(login_status(False))


# ============================================================
# 44. Practical Example - Product Prices
# ============================================================

prices = [100, 200, 300, 400]

discounted_prices = list(
    map(
        lambda price: price * 0.90,
        prices
    )
)

print(discounted_prices)


# ============================================================
# 45. Practical Example - Filter Expensive Products
# ============================================================

prices = [100, 500, 1200, 300, 2000, 750]

expensive = list(
    filter(
        lambda price: price >= 1000,
        prices
    )
)

print(expensive)


# ============================================================
# 46. Practical Example - Employee Salaries
# ============================================================

employees = [
    ("Kishor", 50000),
    ("Rahul", 70000),
    ("Priya", 60000),
    ("Amit", 45000)
]

employees_sorted = sorted(
    employees,
    key=lambda employee: employee[1],
    reverse=True
)

print(employees_sorted)


# ============================================================
# 47. Lambda with Conditional Logic
# ============================================================

number_type = lambda x: (
    "Positive" if x > 0
    else "Negative" if x < 0
    else "Zero"
)

print(number_type(10))
print(number_type(-5))
print(number_type(0))


# ============================================================
# 48. Lambda Can Be Immediately Called
# ============================================================

result = (lambda x: x * 2)(10)

print(result)


# The lambda is created and called immediately.


# ============================================================
# 49. Lambda vs def - Readability
# ============================================================

# Lambda is good for short operations:

double = lambda x: x * 2

print(double(5))


# def is better for complex logic:

def calculate_result(number):

    if number > 0:
        return number * 2

    return 0


print(calculate_result(10))


# ============================================================
# 50. When NOT to Use Lambda
# ============================================================

"""
Avoid complicated lambda expressions.

Bad style:

    result = lambda x: (
        x * 2 if x > 10
        else x + 5 if x > 5
        else x - 2
    )


For complex logic, use def:

    def calculate(x):
        if x > 10:
            return x * 2

        if x > 5:
            return x + 5

        return x - 2


Rule of thumb:

    Simple operation -> lambda
    Complex logic   -> def
"""


# ============================================================
# 51. Common Mistake - Forgetting the Expression
# ============================================================

# Correct:

square = lambda x: x ** 2


# A lambda must contain an expression.


# ============================================================
# 52. Common Mistake - Lambda with Statements
# ============================================================

"""
Lambda functions are designed for expressions.

You cannot write normal statements such as:

    lambda x:
        if x > 10:
            return x

Use `def` for this kind of logic.
"""


# ============================================================
# 53. Lambda with map(), filter() and sorted()
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

# map()

squares = list(
    map(lambda x: x ** 2, numbers)
)

print("Squares:", squares)


# filter()

evens = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print("Even:", evens)


# sorted()

descending = sorted(
    numbers,
    key=lambda x: x,
    reverse=True
)

print("Descending:", descending)


# ============================================================
# 54. Quick Reference
# ============================================================

"""
Lambda syntax:

    lambda arguments: expression


Examples:

    lambda x: x * 2

    lambda a, b: a + b

    lambda x: x ** 2

    lambda x: "Even" if x % 2 == 0 else "Odd"


Common uses:

    map()
    filter()
    sorted()
    min()
    max()
    reduce()


Lambda returns:

    One expression result.


Lambda is:

    Anonymous
    Small
    Usually one-line
    Useful for short operations


Lambda is NOT:

    A replacement for every normal function.
"""


# ============================================================
# 55. Mini Practice
# ============================================================

# Practice 1:
# Create a lambda function that returns the cube of a number.


# Practice 2:
# Create a lambda function that checks whether a number
# is positive or negative.


# Practice 3:
# Use map() and lambda to double every number in a list.


# Practice 4:
# Use filter() and lambda to find numbers greater than 50.


# Practice 5:
# Use sorted() and lambda to sort words by length.


# Practice 6:
# Given:
#
# students = [
#     ("Kishor", 85),
#     ("Rahul", 92),
#     ("Priya", 78)
# ]
#
# Sort students by marks from highest to lowest.


# Practice 7:
# Use reduce() and lambda to calculate the product of
# all numbers.


# Practice 8:
# Create a lambda that calculates a 10% discount.


# Practice 9:
# Create a lambda that returns:
#
# "Pass" if marks >= 40
# "Fail" otherwise.


# Practice 10:
# Create a lambda that returns the larger of two numbers.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
1. A lambda is a small anonymous function.

2. Syntax:

       lambda arguments: expression

3. Lambda can accept multiple arguments.

4. Lambda returns the result of its expression.

5. Lambda is useful for short, simple operations.

6. Lambda is commonly used with:
       map()
       filter()
       sorted()
       min()
       max()
       reduce()

7. `*` and `**` are NOT required for normal lambda usage.

8. For complex logic, prefer `def`.

9. Lambda functions can be stored in variables.

10. Lambda functions can be returned from other functions.

11. Lambda functions can be used as callback/key functions.

12. Lambda functions can make short operations concise,
    but readability should always come first.
"""
