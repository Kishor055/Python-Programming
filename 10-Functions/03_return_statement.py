"""
03 - Return Statement
=====================

The `return` statement is used to send a value from a function
back to the code that called the function.

Syntax:

    def function_name(parameters):
        # statements
        return value


Important:
----------
- `return` ends the execution of a function.
- It sends a value back to the caller.
- A function can return any Python data type.
- A function without a return statement returns None.
- A function can return multiple values.
"""


# ============================================================
# 1. Basic Return Statement
# ============================================================

def add(a, b):
    return a + b


result = add(10, 20)

print("Result:", result)


# ============================================================
# 2. Return vs Print
# ============================================================

def add_with_print(a, b):
    print(a + b)


def add_with_return(a, b):
    return a + b


# print() displays the result
add_with_print(10, 20)


# return sends the result back
result = add_with_return(10, 20)

print("Returned result:", result)


# A returned value can be reused.

result = add_with_return(10, 20)

print("Result × 2:", result * 2)


# ============================================================
# 3. Return Statement Ends Function Execution
# ============================================================

def check_number(number):

    if number > 0:
        return "Positive"

    print("This line runs only when number is not positive.")

    return "Zero or Negative"


print(check_number(10))


# Code after return is not executed.

def demo():
    print("Before return")

    return "Done"

    print("After return")   # Never executes


print(demo())


# ============================================================
# 4. Returning Different Data Types
# ============================================================

def get_number():
    return 100


def get_name():
    return "Kishor"


def get_status():
    return True


def get_numbers():
    return [10, 20, 30]


print(get_number())
print(get_name())
print(get_status())
print(get_numbers())


# ============================================================
# 5. Returning None
# ============================================================

def message():
    print("Hello Python")


result = message()

print("Returned value:", result)


# Output:
#
# Hello Python
# Returned value: None


# ============================================================
# 6. Returning a Calculation
# ============================================================

def square(number):
    return number ** 2


print("Square:", square(5))
print("Square:", square(10))
print("Square:", square(-4))


# ============================================================
# 7. Returning a Boolean
# ============================================================

def is_even(number):
    return number % 2 == 0


print(is_even(10))
print(is_even(7))


# The returned Boolean can be used directly in an if statement.

if is_even(20):
    print("20 is even")


# ============================================================
# 8. Returning a String
# ============================================================

def even_or_odd(number):

    if number % 2 == 0:
        return "Even"

    return "Odd"


print(even_or_odd(16))
print(even_or_odd(7))


# ============================================================
# 9. Multiple Return Values
# ============================================================

def calculate(a, b):

    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication


result = calculate(10, 5)

print("Results:", result)


# Python packs multiple returned values into a tuple.


# ============================================================
# 10. Unpacking Multiple Return Values
# ============================================================

addition, subtraction, multiplication = calculate(10, 5)

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)


# ============================================================
# 11. Returning a List
# ============================================================

def get_even_numbers(numbers):

    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = get_even_numbers(numbers)

print("Even numbers:", result)


# ============================================================
# 12. Returning a Dictionary
# ============================================================

def create_student(name, age, course):

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    return student


student = create_student(
    "Kishor",
    20,
    "Python"
)

print(student)


# Access returned dictionary values.

print("Name:", student["name"])
print("Course:", student["course"])


# ============================================================
# 13. Returning Multiple Values with Different Types
# ============================================================

def student_info():

    name = "Kishor"
    age = 20
    is_student = True

    return name, age, is_student


name, age, is_student = student_info()

print("Name:", name)
print("Age:", age)
print("Student:", is_student)


# ============================================================
# 14. Return from Conditional Statements
# ============================================================

def get_grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 75:
        return "B"

    elif marks >= 60:
        return "C"

    elif marks >= 40:
        return "D"

    else:
        return "F"


print("Grade:", get_grade(95))
print("Grade:", get_grade(78))
print("Grade:", get_grade(55))
print("Grade:", get_grade(30))


# ============================================================
# 15. Practical Example - Calculator
# ============================================================

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):

    if b == 0:
        return "Cannot divide by zero"

    return a / b


print("Addition:", add(20, 10))
print("Subtraction:", subtract(20, 10))
print("Multiplication:", multiply(20, 10))
print("Division:", divide(20, 10))
print("Division:", divide(20, 0))


# ============================================================
# 16. Return Value Used by Another Function
# ============================================================

def square(number):
    return number ** 2


def double(number):
    return number * 2


result = double(square(5))

print("Result:", result)


# Execution:
#
# square(5)
#     ↓
# 25
#     ↓
# double(25)
#     ↓
# 50


# ============================================================
# 17. Returning from a Loop
# ============================================================

def find_first_even(numbers):

    for number in numbers:

        if number % 2 == 0:
            return number

    return None


numbers = [1, 3, 7, 8, 11, 14]

result = find_first_even(numbers)

print("First even number:", result)


# `return` stops the function as soon as the first even
# number is found.


# ============================================================
# 18. Practical Example - Find Maximum
# ============================================================

def find_maximum(a, b, c):

    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    return c


print("Maximum:", find_maximum(10, 25, 15))


# ============================================================
# 19. Practical Example - Calculate Area
# ============================================================

def rectangle_area(length, width):
    return length * width


def circle_area(radius):

    pi = 3.14159

    return pi * radius ** 2


print("Rectangle:", rectangle_area(10, 5))
print("Circle:", circle_area(7))


# ============================================================
# 20. Return Value in an Expression
# ============================================================

def add(a, b):
    return a + b


result = add(10, 20) * 2

print("Result:", result)


# ============================================================
# 21. Function Calling Another Function
# ============================================================

def calculate_square(number):
    return number ** 2


def calculate_cube(number):
    return calculate_square(number) * number


print("Square:", calculate_square(5))
print("Cube:", calculate_cube(5))


# ============================================================
# 22. Common Mistake
# ============================================================

# Incorrect when we want to store the result:

def wrong_add(a, b):
    print(a + b)


result = wrong_add(10, 20)

print("Result:", result)

# Output:
#
# 30
# Result: None
#
# Why?
# Because the function prints the value but does not return it.


# Correct:

def correct_add(a, b):
    return a + b


result = correct_add(10, 20)

print("Result:", result)


# ============================================================
# 23. Mini Practice
# ============================================================

# Practice 1:
# Create a function that returns the cube of a number.


# Practice 2:
# Create a function that returns True if a number is positive.


# Practice 3:
# Create a function that returns the largest of three numbers.


# Practice 4:
# Create a function that returns the factorial of a number.


# Practice 5:
# Create a function that returns the sum and average of
# three numbers.


# Practice 6:
# Create a function that receives a list and returns
# the largest number.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

"""
1. `return` sends a value back to the caller.
2. `return` immediately ends the function.
3. A function can return numbers, strings, lists, dictionaries,
   booleans, tuples, and other objects.
4. A function without `return` returns None.
5. A function can return multiple values.
6. Multiple return values are packed into a tuple.
7. Returned values can be stored and reused.
8. Return values can be used inside expressions.
9. Return statements are useful with conditional logic.
10. Returning values makes functions reusable and composable.
"""
