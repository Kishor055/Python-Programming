"""
01 - Function Basics
====================

A function is a reusable block of code that performs a specific task.

Why use functions?
------------------
1. Code Reusability
2. Modularity
3. Readability
4. Maintainability
5. Easier Testing and Debugging

Basic Syntax
------------

def function_name(parameters):
    # function body
    statements
    return value
"""


# ============================================================
# 1. Defining a Simple Function
# ============================================================

def welcome():
    """Print a welcome message."""
    print("Welcome to Python Functions!")


# ============================================================
# 2. Calling a Function
# ============================================================

# Defining a function does not execute it.
# We need to call the function.

welcome()


# A function can be called multiple times.

welcome()
welcome()


# ============================================================
# 3. Function with a Parameter
# ============================================================

def greet(name):
    """Greet a person using the given name."""
    print("Hello,", name)


greet("Kishor")
greet("Python")


# Parameter vs Argument:
#
# def greet(name):
#            ^^^^
#          Parameter
#
# greet("Kishor")
#       ^^^^^^^^
#        Argument


# ============================================================
# 4. Function with Multiple Parameters
# ============================================================

def add(a, b):
    """Print the sum of two numbers."""
    print("Sum:", a + b)


add(10, 20)
add(100, 200)


# ============================================================
# 5. Returning a Value
# ============================================================

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


result = multiply(10, 5)

print("Multiplication:", result)


# The returned value can be used in another expression.

answer = multiply(10, 5) + 100

print("Answer:", answer)


# ============================================================
# 6. print() vs return
# ============================================================

def add_with_print(a, b):
    """Display the result directly."""
    print(a + b)


def add_with_return(a, b):
    """Return the result to the caller."""
    return a + b


# print() displays the result.
add_with_print(10, 20)


# return gives the result back to the caller.
result = add_with_return(10, 20)

print("Returned value:", result)


# Because the value was returned, we can use it again.

result = add_with_return(10, 20)

print("Result × 2:", result * 2)


# ============================================================
# 7. Function Without a Return Statement
# ============================================================

def message():
    print("This function does not return a value.")


result = message()

print("Returned value:", result)

# Output:
# This function does not return a value.
# Returned value: None


# ============================================================
# 8. Returning Multiple Values
# ============================================================

def calculate(a, b):
    """Return addition, subtraction, and multiplication."""
    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication


result = calculate(10, 5)

print("All results:", result)


# Values can also be unpacked.

addition, subtraction, multiplication = calculate(10, 5)

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)


# ============================================================
# 9. Default Parameter
# ============================================================

def greet_user(name="Guest"):
    """Greet a user with a default name."""
    print("Hello,", name)


# Uses the default value.
greet_user()

# Uses the provided value.
greet_user("Kishor")


# ============================================================
# 10. Positional Arguments
# ============================================================

def student(name, age):
    print("Name:", name)
    print("Age:", age)


# Arguments are assigned according to their position.
student("Kishor", 20)


# ============================================================
# 11. Keyword Arguments
# ============================================================

# Arguments can also be passed using parameter names.

student(name="Kishor", age=20)

# Order can be changed when using keyword arguments.
student(age=20, name="Kishor")


# ============================================================
# 12. Practical Example - Even or Odd
# ============================================================

def even_or_odd(number):
    """Return whether a number is even or odd."""

    if number % 2 == 0:
        return "Even"

    return "Odd"


print(even_or_odd(16))
print(even_or_odd(7))
print(even_or_odd(100))


# ============================================================
# 13. Practical Example - Square
# ============================================================

def square(number):
    """Return the square of a number."""
    return number ** 2


print("Square:", square(5))
print("Square:", square(10))


# ============================================================
# 14. Practical Example - Calculate Area
# ============================================================

def rectangle_area(length, width):
    """Return the area of a rectangle."""
    return length * width


length = 10
width = 5

area = rectangle_area(length, width)

print("Rectangle area:", area)


# ============================================================
# 15. Function Execution Flow
# ============================================================

def calculate_sum(a, b):
    result = a + b
    return result


# Step 1: Function is called
# Step 2: a receives 10
# Step 3: b receives 20
# Step 4: result becomes 30
# Step 5: return sends 30 back
# Step 6: answer stores 30

answer = calculate_sum(10, 20)

print("Final answer:", answer)


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# 1. Use `def` to define a function.
# 2. Call a function using function_name().
# 3. Parameters receive input values.
# 4. Arguments are values passed during a function call.
# 5. `return` sends a value back to the caller.
# 6. A function without a return statement returns None.
# 7. Functions can have default parameters.
# 8. Arguments can be positional or keyword-based.
# 9. Functions make code reusable and easier to maintain.
