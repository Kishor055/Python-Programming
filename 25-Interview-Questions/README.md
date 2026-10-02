# 🐍 Python Interview Questions & Answers

A structured collection of **Python interview questions with clear answers, examples, and explanations** for beginners, students, and aspiring Python developers.

This section covers Python fundamentals, data structures, functions, OOP, exception handling, file handling, advanced concepts, and common coding interview problems.

---

## 📚 Table of Contents

* [1. Python Basics](#1-python-basics)
* [2. Data Types](#2-data-types)
* [3. Operators](#3-operators)
* [4. Strings](#4-strings)
* [5. Lists, Tuples, Sets & Dictionaries](#5-lists-tuples-sets--dictionaries)
* [6. Functions](#6-functions)
* [7. Object-Oriented Programming](#7-object-oriented-programming)
* [8. Exception Handling](#8-exception-handling)
* [9. File Handling](#9-file-handling)
* [10. Modules & Packages](#10-modules--packages)
* [11. Iterators & Generators](#11-iterators--generators)
* [12. Decorators](#12-decorators)
* [13. Memory Management](#13-memory-management)
* [14. Advanced Python](#14-advanced-python)
* [15. Coding Interview Questions](#15-coding-interview-questions)

---

# 1. Python Basics

## Q1. What is Python?

**Answer:**

Python is a **high-level, general-purpose, interpreted programming language** known for its simple syntax and readability.

It supports multiple programming paradigms, including:

* Procedural programming
* Object-oriented programming
* Functional programming

Python is widely used in:

* Web development
* Data science
* Machine learning
* Artificial intelligence
* Automation
* Scripting
* Scientific computing
* Software development

Example:

```python
print("Hello, Python!")
```

---

## Q2. What are the main features of Python?

**Answer:**

Important features of Python include:

1. **Easy to learn** — Simple and readable syntax.
2. **Interpreted** — Python code is executed by an interpreter.
3. **Dynamically typed** — Variable types are determined at runtime.
4. **Object-oriented** — Supports classes and objects.
5. **Portable** — Python programs can run on different operating systems.
6. **Open source** — Python is freely available.
7. **Large standard library** — Provides many built-in modules.
8. **Extensible** — Can work with code written in languages such as C and C++.
9. **Large ecosystem** — Has thousands of third-party packages.

---

## Q3. Is Python compiled or interpreted?

**Answer:**

Python is commonly described as an **interpreted language**, but the actual execution process is more nuanced.

In the standard implementation, **CPython**, Python source code is first compiled into **bytecode**, which is then executed by the Python virtual machine.

```text
Python Source Code
        ↓
     Bytecode
        ↓
Python Virtual Machine
        ↓
      Output
```

So saying that Python is simply "not compiled" is an oversimplification.

---

## Q4. What is dynamic typing in Python?

**Answer:**

Dynamic typing means that variable types are determined at **runtime**, and a variable can refer to objects of different types during its lifetime.

Example:

```python
x = 10
print(type(x))

x = "Python"
print(type(x))
```

Output:

```text
<class 'int'>
<class 'str'>
```

The variable `x` first refers to an integer and later refers to a string.

---

## Q5. What is PEP 8?

**Answer:**

PEP 8 is the **Python Enhancement Proposal that provides style guidelines for Python code**.

It recommends practices such as:

* Using 4 spaces for indentation
* Keeping lines reasonably short
* Using descriptive names
* Following consistent spacing
* Organizing imports properly

Example:

```python
def calculate_total(price, quantity):
    return price * quantity
```

Following PEP 8 improves code readability and consistency.

---

# 2. Data Types

## Q6. What are Python's built-in data types?

**Answer:**

Common built-in Python data types include:

| Category | Types                              |
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
price = 99.5
name = "Kishor"
skills = ["Python", "SQL"]
```

---

## Q7. What is the difference between mutable and immutable objects?

**Answer:**

A **mutable object** can be modified after it is created.

An **immutable object** cannot be modified after creation.

### Mutable examples

```python
list
dict
set
bytearray
```

### Immutable examples

```python
int
float
bool
str
tuple
frozenset
bytes
```

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

The list was modified, so lists are mutable.

---

## Q8. What is the difference between `==` and `is`?

**Answer:**

`==` checks whether two objects have **equal values**.

`is` checks whether two references point to the **same object**.

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

The lists contain the same values but are different objects.

---

## Q9. What is `None` in Python?

**Answer:**

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

It is commonly used as a default value or to indicate that a function does not return a meaningful result.

---

# 3. Operators

## Q10. What are the different types of operators in Python?

**Answer:**

Python provides several types of operators:

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

# 4. Strings

## Q11. What is a string in Python?

**Answer:**

A string is an **immutable sequence of Unicode characters**.

Strings can be created using single, double, or triple quotes.

```python
name = "Kishor"

message = 'Hello Python'

description = """This is
a multiline string."""
```

---

## Q12. How do you reverse a string?

**Answer:**

Python slicing can be used to reverse a string.

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

## Q13. Why are strings immutable?

**Answer:**

Once a string object is created, its contents cannot be changed.

For example:

```python
name = "Python"

# name[0] = "J"
```

This produces a `TypeError`.

Instead, a new string must be created:

```python
name = "Python"
name = "J" + name[1:]

print(name)
```

Output:

```text
Jython
```

---

# 5. Lists, Tuples, Sets & Dictionaries

## Q14. What is the difference between a list and a tuple?

**Answer:**

| List                                      | Tuple                                |
| ----------------------------------------- | ------------------------------------ |
| Mutable                                   | Immutable                            |
| Uses `[]`                                 | Uses `()`                            |
| Can be modified                           | Cannot be modified                   |
| Generally used for changeable collections | Generally used for fixed collections |

Example:

```python
numbers = [1, 2, 3]
coordinates = (10, 20)
```

---

## Q15. What is a set?

**Answer:**

A set is an **unordered collection of unique elements**.

Example:

```python
numbers = {1, 2, 2, 3, 3}

print(numbers)
```

Output:

```text
{1, 2, 3}
```

Sets are useful for:

* Removing duplicates
* Membership testing
* Mathematical set operations

---

## Q16. What is a dictionary?

**Answer:**

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

Dictionary keys must be **hashable**.

---

## Q17. What is list comprehension?

**Answer:**

List comprehension provides a concise way to create lists.

Normal approach:

```python
squares = []

for number in range(1, 6):
    squares.append(number ** 2)
```

Using list comprehension:

```python
squares = [number ** 2 for number in range(1, 6)]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

---

# 6. Functions

## Q18. What is a function?

**Answer:**

A function is a reusable block of code designed to perform a specific task.

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

Functions improve:

* Code reuse
* Organization
* Readability
* Maintainability

---

## Q19. What is the difference between parameters and arguments?

**Answer:**

A **parameter** is a variable defined in the function declaration.

An **argument** is the actual value passed when calling the function.

```python
def greet(name):      # name is a parameter
    print("Hello", name)


greet("Kishor")       # "Kishor" is an argument
```

---

## Q20. What are `*args` and `**kwargs`?

**Answer:**

`*args` allows a function to receive a variable number of **positional arguments**.

`**kwargs` allows a function to receive a variable number of **keyword arguments**.

Example:

```python
def example(*args, **kwargs):
    print(args)
    print(kwargs)


example(10, 20, 30, name="Kishor", age=21)
```

Output:

```text
(10, 20, 30)
{'name': 'Kishor', 'age': 21}
```

---

## Q21. What is a lambda function?

**Answer:**

A lambda is a small anonymous function written using the `lambda` keyword.

Example:

```python
square = lambda x: x ** 2

print(square(5))
```

Output:

```text
25
```

Lambda functions are commonly used with functions such as `map()`, `filter()`, and `sorted()`.

---

## Q22. What is recursion?

**Answer:**

Recursion occurs when a function calls itself.

A recursive function must have a **base case** to stop the recursion.

Example:

```python
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(5))
```

Output:

```text
120
```

---

# 7. Object-Oriented Programming

## Q23. What is OOP?

**Answer:**

Object-Oriented Programming is a programming paradigm based on **objects and classes**.

Important OOP concepts include:

* Class
* Object
* Encapsulation
* Inheritance
* Polymorphism
* Abstraction

---

## Q24. What is a class?

**Answer:**

A class is a blueprint for creating objects.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)
```

---

## Q25. What is an object?

**Answer:**

An object is an instance of a class.

```python
student = Student("Kishor")

student.display()
```

Here, `student` is an object of the `Student` class.

---

## Q26. What is `__init__()`?

**Answer:**

`__init__()` is an initializer method that is automatically called when an object is created.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name


student = Student("Kishor")

print(student.name)
```

Output:

```text
Kishor
```

---

## Q27. What is inheritance?

**Answer:**

Inheritance allows one class to acquire attributes and methods from another class.

Example:

```python
class Animal:

    def speak(self):
        print("Animal speaks")


class Dog(Animal):

    def bark(self):
        print("Dog barks")


dog = Dog()

dog.speak()
dog.bark()
```

Output:

```text
Animal speaks
Dog barks
```

---

## Q28. What is polymorphism?

**Answer:**

Polymorphism means that the same interface or method name can behave differently depending on the object.

Example:

```python
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


for animal in [Dog(), Cat()]:
    animal.sound()
```

Output:

```text
Bark
Meow
```

Both classes provide `sound()`, but the behavior is different.

---

## Q29. What is encapsulation?

**Answer:**

Encapsulation means bundling data and methods together and controlling how internal data is accessed.

Python does not enforce private fields in the same way as some languages, but naming conventions and mechanisms such as double underscores can be used.

Example:

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
```

---

## Q30. What is abstraction?

**Answer:**

Abstraction means exposing the important interface while hiding implementation details.

Python provides abstract base classes through the `abc` module.

Example:

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

A subclass must implement the abstract method.

---

# 8. Exception Handling

## Q31. What is an exception?

**Answer:**

An exception is an event that occurs during program execution and interrupts the normal flow of execution.

Example:

```python
number = 10 / 0
```

This raises:

```text
ZeroDivisionError
```

---

## Q32. How do you handle exceptions in Python?

**Answer:**

Python uses:

```python
try
except
else
finally
```

Example:

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print(result)

finally:
    print("Program completed.")
```

---

## Q33. What is the purpose of `finally`?

**Answer:**

The `finally` block is used for code that should normally execute whether an exception occurs or not.

It is commonly used for cleanup operations such as closing resources.

Example:

```python
try:
    file = open("data.txt")
finally:
    file.close()
```

In modern Python, using `with open(...)` is usually preferred for files.

---

# 9. File Handling

## Q34. How do you open a file in Python?

**Answer:**

Python provides the `open()` function.

```python
file = open("data.txt", "r")

content = file.read()

file.close()
```

Common modes include:

| Mode | Meaning      |
| ---- | ------------ |
| `r`  | Read         |
| `w`  | Write        |
| `a`  | Append       |
| `x`  | Create       |
| `rb` | Read binary  |
| `wb` | Write binary |

---

## Q35. Why is the `with` statement preferred for files?

**Answer:**

The `with` statement automatically manages the file resource and closes the file when the block finishes.

```python
with open("data.txt", "r") as file:
    content = file.read()

print(content)
```

This is safer and cleaner than manually calling `close()`.

---

# 10. Modules & Packages

## Q36. What is a module?

**Answer:**

A module is a Python file containing Python code such as:

* Functions
* Classes
* Variables
* Statements

For example, if `math_utils.py` contains:

```python
def add(a, b):
    return a + b
```

It can be imported:

```python
import math_utils

print(math_utils.add(10, 20))
```

---

## Q37. What is a package?

**Answer:**

A package is a way of organizing related Python modules into a directory structure.

A package can contain multiple modules and subpackages.

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

---

# 11. Iterators & Generators

## Q38. What is an iterator?

**Answer:**

An iterator is an object that provides elements one at a time using the iterator protocol.

It implements:

```python
__iter__()
__next__()
```

Example:

```python
numbers = iter([1, 2, 3])

print(next(numbers))
print(next(numbers))
print(next(numbers))
```

Output:

```text
1
2
3
```

---

## Q39. What is a generator?

**Answer:**

A generator is a special type of iterator that produces values lazily, usually using `yield`.

Example:

```python
def numbers():
    yield 1
    yield 2
    yield 3


for number in numbers():
    print(number)
```

Generators are useful when working with large sequences because they do not need to create the entire sequence in memory at once.

---

## Q40. What is the difference between `return` and `yield`?

**Answer:**

`return` ends the function and returns a value.

`yield` pauses the function and produces a value while preserving its execution state so it can continue later.

Example:

```python
def generate_numbers():
    yield 1
    yield 2
    yield 3
```

This function returns a generator.

---

# 12. Decorators

## Q41. What is a decorator?

**Answer:**

A decorator is a function that modifies or extends the behavior of another function without changing its source code.

Example:

```python
def decorator(func):

    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper


@decorator
def hello():
    print("Hello")


hello()
```

Output:

```text
Before function
Hello
After function
```

---

# 13. Memory Management

## Q42. How does Python manage memory?

**Answer:**

Python manages memory automatically.

In CPython, memory management involves:

* Private heap
* Reference counting
* Garbage collection
* Memory allocators

Programmers generally do not need to manually allocate and free memory as they would in languages such as C.

---

## Q43. What is garbage collection?

**Answer:**

Garbage collection is the process of identifying and reclaiming objects that are no longer accessible.

Python's memory management primarily uses reference counting in CPython, supplemented by a cyclic garbage collector to handle reference cycles.

Example:

```python
import gc

gc.collect()
```

---

## Q44. What is shallow copy vs deep copy?

**Answer:**

A **shallow copy** creates a new outer object but nested objects may still be shared.

A **deep copy** recursively copies nested objects.

Example:

```python
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)
```

Use `deepcopy()` when independent nested structures are required.

---

# 14. Advanced Python

## Q45. What are magic methods?

**Answer:**

Magic methods, also called **dunder methods**, are special methods whose names begin and end with double underscores.

Examples:

```python
__init__
__str__
__repr__
__len__
__eq__
__add__
```

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


student = Student("Kishor")

print(student)
```

---

## Q46. What is a context manager?

**Answer:**

A context manager manages resources and defines setup and cleanup behavior.

The `with` statement is commonly used with context managers.

Example:

```python
with open("data.txt", "r") as file:
    data = file.read()
```

The file is automatically closed after leaving the `with` block.

---

## Q47. What is a virtual environment?

**Answer:**

A virtual environment creates an isolated Python environment for a project.

This helps prevent dependency conflicts between projects.

Create one using:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

---

## Q48. What is the difference between `pass`, `continue`, and `break`?

**Answer:**

### `pass`

Does nothing.

```python
if True:
    pass
```

### `continue`

Skips the current loop iteration.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

### `break`

Terminates the loop.

```python
for i in range(5):
    if i == 2:
        break
    print(i)
```

---

# 15. Coding Interview Questions

## Q49. How do you check whether a number is even or odd?

**Answer:**

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

---

## Q50. How do you find the factorial of a number?

**Answer:**

Using a loop:

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

## Q51. How do you check whether a string is a palindrome?

**Answer:**

A palindrome reads the same forward and backward.

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

## Q52. How do you reverse a list?

**Answer:**

Using slicing:

```python
numbers = [1, 2, 3, 4, 5]

reversed_numbers = numbers[::-1]

print(reversed_numbers)
```

Output:

```text
[5, 4, 3, 2, 1]
```

Another option is:

```python
numbers.reverse()
```

which modifies the original list.

---

## Q53. How do you remove duplicates from a list?

**Answer:**

If preserving the original order is not important:

```python
numbers = [1, 2, 2, 3, 3, 4]

unique = list(set(numbers))

print(unique)
```

If order should be preserved:

```python
numbers = [1, 2, 2, 3, 3, 4]

unique = list(dict.fromkeys(numbers))

print(unique)
```

Output:

```text
[1, 2, 3, 4]
```

---

## Q54. How do you find the largest number in a list?

**Answer:**

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

## Q55. How do you count the frequency of elements in a list?

**Answer:**

The `Counter` class from the `collections` module can be used.

```python
from collections import Counter

numbers = [1, 2, 2, 3, 3, 3]

frequency = Counter(numbers)

print(frequency)
```

Output:

```text
Counter({3: 3, 2: 2, 1: 1})
```

---

## Q56. How do you check whether two strings are anagrams?

**Answer:**

Two strings are anagrams if they contain the same characters with the same frequencies.

```python
first = "listen"
second = "silent"

if sorted(first) == sorted(second):
    print("Anagrams")
else:
    print("Not anagrams")
```

Output:

```text
Anagrams
```

---

## Q57. How do you generate Fibonacci numbers?

**Answer:**

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

## Q58. How do you check whether a number is prime?

**Answer:**

A prime number has exactly two positive divisors: `1` and itself.

```python
number = 29

if number < 2:
    print("Not prime")
else:
    is_prime = True

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    print("Prime" if is_prime else "Not prime")
```

Output:

```text
Prime
```

Checking divisors only up to the square root is sufficient.

---

# 🎯 Frequently Asked Output Questions

## Q59. What is the output?

```python
x = [1, 2, 3]
y = x

y.append(4)

print(x)
```

### Answer

```text
[1, 2, 3, 4]
```

### Explanation

`x` and `y` refer to the **same list object**.

---

## Q60. What is the output?

```python
a = 10
b = 20

a, b = b, a

print(a, b)
```

### Answer

```text
20 10
```

Python supports multiple assignment, allowing values to be swapped without a temporary variable.

---

## Q61. What is the output?

```python
numbers = [1, 2, 3, 4, 5]

print(numbers[1:4])
```

### Answer

```text
[2, 3, 4]
```

The slice starts at index `1` and stops before index `4`.

---

# 🧠 Important Interview Concepts to Remember

| Concept        | Key Point                                |
| -------------- | ---------------------------------------- |
| Python         | High-level, general-purpose language     |
| Dynamic typing | Types are determined at runtime          |
| List           | Mutable sequence                         |
| Tuple          | Immutable sequence                       |
| Set            | Collection of unique elements            |
| Dictionary     | Key-value mapping                        |
| `==`           | Value equality                           |
| `is`           | Object identity                          |
| Function       | Reusable block of code                   |
| Class          | Blueprint for objects                    |
| Object         | Instance of a class                      |
| Inheritance    | Reuse/extend behavior from another class |
| Polymorphism   | Same interface, different behavior       |
| Generator      | Produces values lazily                   |
| Decorator      | Extends/modifies function behavior       |
| Exception      | Runtime error/event                      |
| `with`         | Context management                       |
| `yield`        | Produces a value from a generator        |

---

# 📈 Interview Preparation Roadmap

```text
Python Basics
      ↓
Data Types
      ↓
Strings & Collections
      ↓
Functions
      ↓
OOP
      ↓
Exception Handling
      ↓
File Handling
      ↓
Modules & Packages
      ↓
Iterators & Generators
      ↓
Decorators
      ↓
Memory Management
      ↓
Coding Problems
      ↓
Mock Interviews
```

---

# ✅ Interview Checklist

* [ ] Python fundamentals
* [ ] Variables and data types
* [ ] Mutable vs immutable
* [ ] `==` vs `is`
* [ ] Strings
* [ ] Lists
* [ ] Tuples
* [ ] Sets
* [ ] Dictionaries
* [ ] Functions
* [ ] `*args` and `**kwargs`
* [ ] Lambda functions
* [ ] Recursion
* [ ] OOP
* [ ] Inheritance
* [ ] Polymorphism
* [ ] Encapsulation
* [ ] Abstraction
* [ ] Exception handling
* [ ] File handling
* [ ] Modules and packages
* [ ] Iterators
* [ ] Generators
* [ ] Decorators
* [ ] Memory management
* [ ] Coding problems
* [ ] Output-based questions

---

# 🚀 Final Advice

Don't just memorize Python interview answers.

Use this approach:

```text
📖 Understand
      ↓
💻 Write Code
      ↓
🧪 Test
      ↓
🐛 Debug
      ↓
🗣️ Explain
      ↓
🔁 Practice Again
```

The goal is not only to **know the answer**, but to understand **why the answer is correct** and explain it clearly during an interview.

---

## 🌱 Keep Growing

> **Learn → Build → Practice → Explain → Grow 🚀**

This interview section is part of the **Python Programming** learning repository.

⭐ If this repository helps you learn Python, consider giving it a star.

---

## 🔗 Repository

[🐍 Python Programming Repository](https://github.com/Kishor055/Python-Programming)

**Keep coding. Keep learning. Keep growing. 🚀**
