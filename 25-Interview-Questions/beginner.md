# 🐍 Python Beginner Interview Questions

A collection of frequently asked **beginner-level Python interview questions with clear answers, explanations, and practical examples**.

This section is designed for students and beginners preparing for their first Python technical interview.

---

## 📚 Table of Contents

1. [What is Python?](#1-what-is-python)
2. [Why is Python popular?](#2-why-is-python-popular)
3. [What are Python's features?](#3-what-are-pythons-features)
4. [Is Python compiled or interpreted?](#4-is-python-compiled-or-interpreted)
5. [What is a variable?](#5-what-is-a-variable)
6. [What is dynamic typing?](#6-what-is-dynamic-typing)
7. [What are Python data types?](#7-what-are-python-data-types)
8. [What is the difference between mutable and immutable objects?](#8-what-is-the-difference-between-mutable-and-immutable-objects)
9. [What is `None`?](#9-what-is-none)
10. [What is type casting?](#10-what-is-type-casting)
11. [What is the difference between `==` and `is`?](#11-what-is-the-difference-between--and-is)
12. [What are Python operators?](#12-what-are-python-operators)
13. [What is indentation?](#13-what-is-indentation)
14. [What are comments?](#14-what-are-comments)
15. [What is a string?](#15-what-is-a-string)
16. [What is a list?](#16-what-is-a-list)
17. [What is a tuple?](#17-what-is-a-tuple)
18. [What is a set?](#18-what-is-a-set)
19. [What is a dictionary?](#19-what-is-a-dictionary)
20. [List vs Tuple](#20-what-is-the-difference-between-a-list-and-a-tuple)
21. [What is a function?](#21-what-is-a-function)
22. [Parameter vs Argument](#22-what-is-the-difference-between-a-parameter-and-an-argument)
23. [What is `return`?](#23-what-is-return)
24. [What is a lambda function?](#24-what-is-a-lambda-function)
25. [What is a loop?](#25-what-is-a-loop)
26. [What is `break`?](#26-what-is-break)
27. [What is `continue`?](#27-what-is-continue)
28. [What is `pass`?](#28-what-is-pass)
29. [What is an exception?](#29-what-is-an-exception)
30. [How is exception handling done?](#30-how-is-exception-handling-done)
31. [What is a module?](#31-what-is-a-module)
32. [What is a package?](#32-what-is-a-package)
33. [How do you take user input?](#33-how-do-you-take-user-input)
34. [How do you check the type of a variable?](#34-how-do-you-check-the-type-of-a-variable)
35. [How do you reverse a string?](#35-how-do-you-reverse-a-string)
36. [How do you check for a palindrome?](#36-how-do-you-check-for-a-palindrome)
37. [How do you find the largest number?](#37-how-do-you-find-the-largest-number)
38. [How do you check whether a number is even or odd?](#38-how-do-you-check-whether-a-number-is-even-or-odd)
39. [How do you calculate factorial?](#39-how-do-you-calculate-factorial)
40. [How do you generate Fibonacci numbers?](#40-how-do-you-generate-fibonacci-numbers)

---

# 1. What is Python?

### Answer

Python is a **high-level, general-purpose programming language** known for its readable syntax and large ecosystem.

It supports several programming styles, including:

* Procedural programming
* Object-oriented programming
* Functional programming

Python is commonly used for:

* Web development
* Data analysis
* Machine learning
* Artificial intelligence
* Automation
* Scripting
* Scientific computing

### Example

```python
print("Hello, Python!")
```

---

# 2. Why is Python popular?

### Answer

Python is popular because it has:

* Simple and readable syntax
* A large standard library
* A large ecosystem of third-party packages
* Support for multiple programming paradigms
* Strong community support
* Applications across many domains

For example, Python is used with frameworks and libraries such as Django, Flask, NumPy, pandas, and PyTorch.

---

# 3. What are Python's features?

### Answer

Important Python features include:

1. **Easy to learn**
2. **Readable syntax**
3. **Dynamically typed**
4. **Object-oriented**
5. **Interpreted through a runtime**
6. **Cross-platform**
7. **Open source**
8. **Large standard library**
9. **Extensible**
10. **Large package ecosystem**

---

# 4. Is Python compiled or interpreted?

### Answer

Python is commonly called an **interpreted language**, but this description is simplified.

In **CPython**, Python source code is compiled into bytecode, which is then executed by the Python virtual machine.

```text
Python Source Code
        ↓
     Bytecode
        ↓
Python Virtual Machine
        ↓
      Output
```

Therefore, Python uses both a compilation step and an interpreter/runtime execution model.

---

# 5. What is a variable?

### Answer

A variable is a **name that refers to an object**.

Example:

```python
name = "Kishor"
age = 21
```

Here:

* `name` refers to a string object.
* `age` refers to an integer object.

Python does not require you to declare the variable's type separately.

---

# 6. What is dynamic typing?

### Answer

Dynamic typing means that the type associated with an object is determined at runtime, and a name can later refer to an object of another type.

Example:

```python
value = 10

print(type(value))

value = "Python"

print(type(value))
```

Output:

```text
<class 'int'>
<class 'str'>
```

---

# 7. What are Python data types?

### Answer

Python provides many built-in data types.

| Category | Examples                           |
| -------- | ---------------------------------- |
| Numeric  | `int`, `float`, `complex`          |
| Boolean  | `bool`                             |
| Text     | `str`                              |
| Sequence | `list`, `tuple`, `range`           |
| Set      | `set`, `frozenset`                 |
| Mapping  | `dict`                             |
| Binary   | `bytes`, `bytearray`, `memoryview` |
| Special  | `NoneType`                         |

Example:

```python
age = 21
price = 99.99
name = "Kishor"
skills = ["Python", "SQL"]
```

---

# 8. What is the difference between mutable and immutable objects?

### Answer

A **mutable object** can be changed after it is created.

An **immutable object** cannot be changed after it is created.

### Mutable

* `list`
* `dict`
* `set`
* `bytearray`

### Immutable

* `int`
* `float`
* `bool`
* `str`
* `tuple`
* `frozenset`
* `bytes`

Example:

```python
numbers = [1, 2, 3]

numbers.append(4)

print(numbers)
```

Output:

```text
[1, 2, 3, 4]
```

The list was modified, so it is mutable.

---

# 9. What is `None`?

### Answer

`None` represents the absence of a value.

Its type is `NoneType`.

Example:

```python
result = None

print(result)
print(type(result))
```

Output:

```text
None
<class 'NoneType'>
```

---

# 10. What is type casting?

### Answer

Type casting means converting a value from one data type to another.

Example:

```python
number = "100"

integer_number = int(number)

print(integer_number)
print(type(integer_number))
```

Output:

```text
100
<class 'int'>
```

Common conversion functions include:

```python
int()
float()
str()
bool()
list()
tuple()
set()
```

---

# 11. What is the difference between `==` and `is`?

### Answer

`==` checks **value equality**.

`is` checks **object identity**.

Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

Output:

```text
True
False
```

The lists contain the same values but are separate objects.

---

# 12. What are Python operators?

### Answer

Operators are symbols or keywords used to perform operations.

### Arithmetic

```python
+  -  *  /  //  %  **
```

### Comparison

```python
==  !=  >  <  >=  <=
```

### Logical

```python
and
or
not
```

### Assignment

```python
=  +=  -=  *=  /=  //=  %=  **=
```

### Membership

```python
in
not in
```

### Identity

```python
is
is not
```

### Bitwise

```python
&  |  ^  ~  <<  >>
```

---

# 13. What is indentation?

### Answer

Indentation is the whitespace used to define blocks of code in Python.

Python uses indentation instead of braces such as `{}`.

Example:

```python
age = 20

if age >= 18:
    print("Adult")
```

The indented line belongs to the `if` block.

Incorrect indentation can result in an `IndentationError`.

---

# 14. What are comments?

### Answer

Comments are notes in source code that are ignored by the Python interpreter.

A single-line comment starts with `#`.

```python
# This is a comment

print("Hello")
```

Comments help explain code and improve readability.

---

# 15. What is a string?

### Answer

A string is an **immutable sequence of Unicode characters**.

Example:

```python
name = "Kishor"
message = 'Hello Python'
```

Strings can be indexed:

```python
text = "Python"

print(text[0])
```

Output:

```text
P
```

---

# 16. What is a list?

### Answer

A list is an **ordered, mutable collection** that can contain multiple values.

Example:

```python
numbers = [10, 20, 30, 40]

numbers.append(50)

print(numbers)
```

Output:

```text
[10, 20, 30, 40, 50]
```

Lists can contain different data types:

```python
items = [10, "Python", 3.14, True]
```

---

# 17. What is a tuple?

### Answer

A tuple is an **ordered, immutable collection**.

Example:

```python
coordinates = (10, 20)

print(coordinates[0])
```

Output:

```text
10
```

Because tuples are immutable, their elements cannot be reassigned.

---

# 18. What is a set?

### Answer

A set is a collection of **unique elements**.

Example:

```python
numbers = {1, 2, 2, 3, 3}

print(numbers)
```

Output:

```text
{1, 2, 3}
```

Sets are useful for removing duplicates and performing set operations.

---

# 19. What is a dictionary?

### Answer

A dictionary stores data as **key-value pairs**.

Example:

```python
student = {
    "name": "Kishor",
    "age": 21,
    "course": "Python"
}

print(student["name"])
```

Output:

```text
Kishor
```

Dictionary keys must be hashable.

---

# 20. What is the difference between a list and a tuple?

### Answer

| List                              | Tuple                          |
| --------------------------------- | ------------------------------ |
| Mutable                           | Immutable                      |
| Uses `[]`                         | Uses `()`                      |
| Can be modified                   | Cannot be modified             |
| Suitable for changing collections | Suitable for fixed collections |

Example:

```python
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
```

---

# 21. What is a function?

### Answer

A function is a reusable block of code that performs a specific task.

Example:

```python
def add(a, b):
    return a + b


result = add(10, 20)

print(result)
```

Output:

```text
30
```

Functions improve code reuse and organization.

---

# 22. What is the difference between a parameter and an argument?

### Answer

A **parameter** is a variable defined in a function.

An **argument** is the actual value passed to the function.

```python
def greet(name):       # name is a parameter
    print("Hello", name)


greet("Kishor")        # "Kishor" is an argument
```

---

# 23. What is `return`?

### Answer

The `return` statement sends a value back from a function and ends that function's execution.

Example:

```python
def square(number):
    return number ** 2


result = square(5)

print(result)
```

Output:

```text
25
```

---

# 24. What is a lambda function?

### Answer

A lambda function is a small anonymous function created using the `lambda` keyword.

Syntax:

```python
lambda arguments: expression
```

Example:

```python
square = lambda x: x ** 2

print(square(5))
```

Output:

```text
25
```

Lambda functions are useful for short operations, particularly as arguments to functions such as `sorted()`, `map()`, and `filter()`.

---

# 25. What is a loop?

### Answer

A loop repeatedly executes a block of code.

Python provides:

* `for`
* `while`

### `for` loop

```python
for number in range(1, 6):
    print(number)
```

### `while` loop

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

---

# 26. What is `break`?

### Answer

`break` immediately terminates the nearest enclosing loop.

Example:

```python
for number in range(1, 6):

    if number == 3:
        break

    print(number)
```

Output:

```text
1
2
```

---

# 27. What is `continue`?

### Answer

`continue` skips the rest of the current loop iteration and moves to the next iteration.

Example:

```python
for number in range(1, 6):

    if number == 3:
        continue

    print(number)
```

Output:

```text
1
2
4
5
```

---

# 28. What is `pass`?

### Answer

`pass` is a statement that does nothing.

It is useful when Python requires a statement syntactically, but you do not want to execute any code yet.

Example:

```python
def future_function():
    pass
```

---

# 29. What is an exception?

### Answer

An exception is an event that occurs during program execution and disrupts the normal flow of the program.

Example:

```python
number = 10 / 0
```

This raises:

```text
ZeroDivisionError
```

Other common exceptions include:

* `ValueError`
* `TypeError`
* `IndexError`
* `KeyError`
* `FileNotFoundError`

---

# 30. How is exception handling done?

### Answer

Python uses `try` and `except` blocks to handle exceptions.

Example:

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Python also supports:

```python
try:
    ...
except:
    ...
else:
    ...
finally:
    ...
```

---

# 31. What is a module?

### Answer

A module is a Python file containing reusable code such as functions, classes, and variables.

For example, `math_utils.py`:

```python
def add(a, b):
    return a + b
```

It can be imported into another file:

```python
import math_utils

print(math_utils.add(10, 20))
```

---

# 32. What is a package?

### Answer

A package is a directory used to organize related Python modules and subpackages.

Example:

```text
project/
│
├── main.py
│
└── utilities/
    ├── __init__.py
    ├── math_utils.py
    └── string_utils.py
```

Packages help organize larger Python projects.

---

# 33. How do you take user input?

### Answer

Python uses the `input()` function.

Example:

```python
name = input("Enter your name: ")

print("Hello", name)
```

Important: `input()` returns a string.

If you need an integer:

```python
age = int(input("Enter your age: "))
```

---

# 34. How do you check the type of a variable?

### Answer

Use the built-in `type()` function.

Example:

```python
value = 100

print(type(value))
```

Output:

```text
<class 'int'>
```

For type checks in conditional code, `isinstance()` is often more appropriate:

```python
value = 100

print(isinstance(value, int))
```

Output:

```text
True
```

---

# 35. How do you reverse a string?

### Answer

Python slicing can reverse a string.

```python
text = "Python"

reversed_text = text[::-1]

print(reversed_text)
```

Output:

```text
nohtyP
```

---

# 36. How do you check for a palindrome?

### Answer

A palindrome reads the same forward and backward.

Example:

```python
text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
```

Output:

```text
Palindrome
```

---

# 37. How do you find the largest number?

### Answer

Python provides the built-in `max()` function.

```python
numbers = [10, 25, 5, 40, 15]

largest = max(numbers)

print(largest)
```

Output:

```text
40
```

---

# 38. How do you check whether a number is even or odd?

### Answer

Use the modulo operator `%`.

```python
number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Output:

```text
Even
```

If the remainder after division by `2` is zero, the number is even.

---

# 39. How do you calculate factorial?

### Answer

The factorial of a non-negative integer `n` is:

```text
n! = n × (n-1) × (n-2) × ... × 1
```

Example:

```python
number = 5
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(factorial)
```

Output:

```text
120
```

---

# 40. How do you generate Fibonacci numbers?

### Answer

The Fibonacci sequence starts with `0` and `1`, and each following number is the sum of the previous two.

Example:

```python
a = 0
b = 1

for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
```

Output:

```text
0 1 1 2 3 5 8 13 21 34
```

---

# 🎯 Quick Revision

| Question        | Key Answer                                       |
| --------------- | ------------------------------------------------ |
| What is Python? | High-level, general-purpose programming language |
| Variable        | Name referring to an object                      |
| Dynamic typing  | Type association is determined at runtime        |
| List            | Mutable ordered collection                       |
| Tuple           | Immutable ordered collection                     |
| Set             | Collection of unique elements                    |
| Dictionary      | Key-value mapping                                |
| String          | Immutable Unicode text sequence                  |
| `==`            | Compares values                                  |
| `is`            | Checks object identity                           |
| Function        | Reusable block of code                           |
| Parameter       | Variable in function definition                  |
| Argument        | Value passed to function                         |
| `return`        | Sends a value back from a function               |
| Lambda          | Small anonymous function                         |
| `break`         | Terminates a loop                                |
| `continue`      | Skips current iteration                          |
| `pass`          | Does nothing                                     |
| Exception       | Runtime event/error                              |
| Module          | Python file containing reusable code             |
| Package         | Collection/organization of modules               |
| `input()`       | Reads user input                                 |
| `type()`        | Returns an object's type                         |

---

# 🧠 Beginner Interview Tips

When answering a Python interview question:

### 1. Start with the definition

Give a short and direct explanation.

### 2. Explain the important concept

Mention the key difference or purpose.

### 3. Give an example

Use a small Python program when appropriate.

### 4. Explain the output

If the interviewer asks a coding question, explain **why** the code produces that result.

### 5. Avoid memorizing blindly

Understand the concept so you can answer variations of the same question.

---

# 🚀 Beginner Preparation Path

```text
Python Basics
      ↓
Variables & Data Types
      ↓
Operators
      ↓
Strings
      ↓
Lists / Tuples / Sets / Dictionaries
      ↓
Conditions
      ↓
Loops
      ↓
Functions
      ↓
Exceptions
      ↓
Modules & Packages
      ↓
Basic Coding Problems
      ↓
Intermediate Python
```

---

## 🌱 Keep Growing

> **Understand the concept → Write the code → Test it → Explain it → Practice again.**

**Next:** [`intermediate.md`](./intermediate.md)

**Back:** [`README.md`](./README.md)

---

⭐ **Keep Learning Python. Keep Building. Keep Growing. 🚀**
