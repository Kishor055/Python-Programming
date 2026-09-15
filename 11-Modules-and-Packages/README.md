# 📦 11 — Modules and Packages

> **Organize Python code into reusable, maintainable, and scalable components.**

Modules and Packages are essential for writing **clean, reusable, maintainable, and production-ready Python applications**.

As Python programs become larger, keeping everything inside a single file becomes difficult. Python solves this problem by allowing developers to divide code into **modules** and organize related modules into **packages**.

---

## 🎯 Learning Objectives

By the end of this chapter, you will understand:

* What is a Python module?
* Why modules are useful
* How to create custom modules
* How to import modules
* Different `import` statements
* Importing specific functions and variables
* Using aliases with `as`
* Python built-in modules
* Understanding `__name__`
* The `if __name__ == "__main__"` pattern
* What is a Python package?
* Package directory structure
* `__init__.py`
* Subpackages
* Absolute imports
* Relative imports
* Module vs Package
* Creating reusable Python code
* Organizing larger Python projects

---

# 🧠 1. What is a Module?

A **module** is simply a Python file (`.py`) containing Python code such as:

* Variables
* Functions
* Classes
* Constants
* Statements

For example:

```text
calculator.py
```

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b
```

This file is a **module**.

You can reuse it from another Python program:

```python
import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
```

### Output

```text
15
5
```

> 💡 A module allows you to write code once and reuse it wherever required.

Python's official tutorial defines a module as a file containing Python definitions and statements that can be imported into other programs. ([Python documentation][2])

---

# 🚀 2. Why Use Modules?

Modules provide several advantages:

| Benefit            | Description                                      |
| ------------------ | ------------------------------------------------ |
| ♻️ Reusability     | Write code once and reuse it                     |
| 🧹 Maintainability | Keep related functionality together              |
| 📦 Organization    | Divide large applications into files             |
| 🧪 Testing         | Test components independently                    |
| 🔒 Namespace       | Avoid naming conflicts                           |
| 👥 Collaboration   | Multiple developers can work on separate modules |

Instead of:

```text
main.py
  └── 5000 lines of code
```

Prefer:

```text
project/
├── main.py
├── users.py
├── database.py
├── authentication.py
└── utilities.py
```

---

# 🛠️ 3. Creating a Custom Module

Create:

```text
math_utils.py
```

```python
PI = 3.14159


def square(number):
    return number ** 2


def cube(number):
    return number ** 3
```

Now create:

```text
main.py
```

```python
import math_utils

print(math_utils.PI)
print(math_utils.square(5))
print(math_utils.cube(3))
```

### Output

```text
3.14159
25
27
```

---

# 📥 4. Importing a Module

The simplest syntax is:

```python
import module_name
```

Example:

```python
import math

print(math.sqrt(25))
```

### Output

```text
5.0
```

---

# 🎯 5. Import Specific Functions

Instead of importing the complete module:

```python
from math import sqrt

print(sqrt(25))
```

You can import multiple objects:

```python
from math import sqrt, factorial

print(sqrt(16))
print(factorial(5))
```

---

# 🏷️ 6. Import Using an Alias

Use `as` to create a shorter or more convenient name.

```python
import math as m

print(m.sqrt(25))
```

Another example:

```python
import datetime as dt

print(dt.datetime.now())
```

---

# 📚 7. Import Everything

Python also supports:

```python
from module_name import *
```

Example:

```python
from math import *

print(sqrt(25))
print(pow(2, 3))
```

### ⚠️ Best Practice

Avoid wildcard imports in production code:

```python
from math import *
```

Prefer explicit imports:

```python
from math import sqrt, pow
```

This makes code easier to understand and prevents namespace conflicts.

---

# 🐍 8. Python Standard Library Modules

Python comes with a large **Standard Library** containing many useful modules.

Some commonly used modules:

| Module        | Purpose                           |
| ------------- | --------------------------------- |
| `math`        | Mathematical operations           |
| `random`      | Random numbers                    |
| `datetime`    | Date and time                     |
| `os`          | Operating-system interaction      |
| `sys`         | Python runtime/system information |
| `json`        | JSON processing                   |
| `re`          | Regular expressions               |
| `statistics`  | Statistical calculations          |
| `pathlib`     | File-system paths                 |
| `collections` | Specialized containers            |

Example:

```python
import random

number = random.randint(1, 10)

print(number)
```

---

# 🔍 9. `dir()` Function

The `dir()` function can be used to inspect the names available inside a module or object.

```python
import math

print(dir(math))
```

This is useful when exploring unfamiliar modules.

---

# 🧩 10. The `__name__` Variable

Every Python module has a special variable:

```python
__name__
```

When a file is executed directly:

```python
print(__name__)
```

Output:

```text
__main__
```

When the same file is imported:

```python
__name__
```

contains the module's name.

---

# ⭐ 11. `if __name__ == "__main__"`

One of the most important Python patterns is:

```python
if __name__ == "__main__":
    print("Program started")
```

Example:

```python
def greet():
    print("Hello, Python!")


if __name__ == "__main__":
    greet()
```

This allows code to behave differently when:

* The file is executed directly
* The file is imported as a module

### Why is this useful?

It prevents test/demo code from automatically running when another program imports the module.

---

# 📦 12. What is a Package?

A **package** is a way to organize related Python modules into a directory hierarchy.

For example:

```text
shopping/
├── __init__.py
├── cart.py
├── products.py
└── customers.py
```

Here:

```text
shopping
```

is the package, while:

```text
cart.py
products.py
customers.py
```

are modules.

Python uses packages to organize module namespaces and create hierarchical structures. ([GitHub][3])

---

# 🗂️ 13. Package Structure

A simple package can look like:

```text
my_project/
│
├── main.py
│
└── utilities/
    ├── __init__.py
    ├── math_utils.py
    └── string_utils.py
```

### `math_utils.py`

```python
def add(a, b):
    return a + b
```

### `string_utils.py`

```python
def reverse(text):
    return text[::-1]
```

### `main.py`

```python
from utilities.math_utils import add
from utilities.string_utils import reverse

print(add(10, 20))
print(reverse("Python"))
```

### Output

```text
30
nohtyP
```

---

# 🧱 14. `__init__.py`

Traditionally, `__init__.py` is used to indicate that a directory should be treated as a Python package.

Example:

```text
utilities/
├── __init__.py
├── math_utils.py
└── string_utils.py
```

`__init__.py` can also contain package-level initialization code or expose selected objects.

For example:

```python
from .math_utils import add
```

Modern Python also supports namespace packages without requiring `__init__.py`, but it remains common and useful in regular package structures. The Python Packaging User Guide recommends understanding `__init__.py` when building conventional packages. ([Python Packaging][4])

---

# 🔗 15. Absolute Import

An absolute import specifies the complete package path.

```python
from utilities.math_utils import add
```

Structure:

```text
project/
├── main.py
└── utilities/
    ├── __init__.py
    └── math_utils.py
```

---

# ↩️ 16. Relative Import

Relative imports use:

```python
.
..
```

Example:

```python
from .math_utils import add
```

Meaning:

```text
.   → current package
..  → parent package
```

Relative imports are particularly useful inside larger package structures.

---

# 🌳 17. Nested Packages

Packages can contain other packages.

```text
application/
│
├── main.py
│
└── app/
    ├── __init__.py
    │
    ├── database/
    │   ├── __init__.py
    │   └── connection.py
    │
    ├── services/
    │   ├── __init__.py
    │   └── user_service.py
    │
    └── utils/
        ├── __init__.py
        └── helpers.py
```

This creates a hierarchical structure:

```text
application
    └── app
        ├── database
        ├── services
        └── utils
```

---

# ⚖️ 18. Module vs Package

| Feature                  | Module          | Package               |
| ------------------------ | --------------- | --------------------- |
| Definition               | Python file     | Collection of modules |
| Extension                | `.py`           | Directory             |
| Purpose                  | Organize code   | Organize modules      |
| Example                  | `math_utils.py` | `utilities/`          |
| Can contain modules?     | ❌               | ✅                     |
| Can contain subpackages? | ❌               | ✅                     |

### Simple rule

```text
Module  → File
Package → Directory
```

---

# 🏗️ 19. Real-World Project Structure

A larger Python application may look like:

```text
my_application/
│
├── main.py
├── requirements.txt
├── README.md
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── database/
│   ├── __init__.py
│   ├── connection.py
│   └── models.py
│
├── services/
│   ├── __init__.py
│   ├── authentication.py
│   └── user_service.py
│
├── utils/
│   ├── __init__.py
│   ├── validators.py
│   └── helpers.py
│
└── tests/
    ├── test_authentication.py
    └── test_users.py
```

This type of organization makes applications easier to scale and maintain.

---

# 🔥 20. Practical Example — Calculator Package

### Project Structure

```text
calculator/
│
├── main.py
│
└── operations/
    ├── __init__.py
    ├── arithmetic.py
    └── advanced.py
```

### `arithmetic.py`

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b
```

### `advanced.py`

```python
def square(number):
    return number ** 2


def cube(number):
    return number ** 3
```

### `main.py`

```python
from operations.arithmetic import add, multiply
from operations.advanced import square

print(add(10, 20))
print(multiply(5, 4))
print(square(6))
```

### Output

```text
30
20
36
```

---

# 🧠 21. Important Concepts to Remember

```text
Python File
    ↓
Module
    ↓
Multiple Modules
    ↓
Package
    ↓
Subpackages
    ↓
Large Application
```

Think of it like:

```text
📁 Package
   │
   ├── 📄 Module
   ├── 📄 Module
   ├── 📁 Subpackage
   │      ├── 📄 Module
   │      └── 📄 Module
   │
   └── 📄 Module
```

---

# ⚠️ 22. Common Mistakes

### ❌ Wrong import path

```python
from math_utils import add
```

when the module actually exists inside:

```text
utilities/math_utils.py
```

Use:

```python
from utilities.math_utils import add
```

---

### ❌ Naming your file after a standard library module

Avoid names such as:

```text
random.py
math.py
json.py
os.py
```

These can shadow Python's standard library modules.

Prefer:

```text
random_utils.py
math_utils.py
json_helper.py
```

---

### ❌ Circular imports

Avoid structures where:

```text
A imports B
B imports A
```

Circular dependencies can make applications difficult to maintain.

---

# 🧪 23. Practice Exercises

### Beginner

1. Create a module containing a function to calculate the square of a number.
2. Import the function into another Python file.
3. Create a module containing constants for mathematical values.
4. Import `sqrt` from the `math` module.
5. Use the `random` module to generate 10 random numbers.

### Intermediate

6. Create a `calculator` package.
7. Create separate modules for addition, subtraction, multiplication, and division.
8. Import functions from different modules.
9. Create a package containing string utility functions.
10. Practice absolute and relative imports.

### Advanced

11. Build a multi-package Python application.
12. Use `__init__.py` to expose package-level functions.
13. Implement `if __name__ == "__main__"`.
14. Identify and eliminate circular imports.
15. Design a reusable utility package.

---

# 💼 24. Interview Questions

### Basic

**Q1. What is a module in Python?**

A Python file containing reusable Python definitions and statements.

**Q2. What is a package?**

A package organizes related Python modules into a hierarchical namespace.

**Q3. What is the difference between a module and a package?**

A module is generally a Python file, while a package organizes modules into a directory hierarchy.

**Q4. What does `import` do?**

It makes definitions from another module available to the importing code.

**Q5. What is `__name__`?**

It is a special module attribute containing the module's name.

---

### Intermediate

**Q6. Why use `if __name__ == "__main__"`?**

To execute specific code only when the file is run directly.

**Q7. What is `__init__.py`?**

A package initialization file commonly used to define package behavior or expose package-level objects.

**Q8. What is an absolute import?**

An import that specifies the complete package/module path.

**Q9. What is a relative import?**

An import that refers to modules relative to the current package.

**Q10. What is a circular import?**

A situation where modules depend on each other directly or indirectly.

---

# 📝 25. Quick Revision

```text
Module
   ↓
Python file containing reusable code

Package
   ↓
Directory organizing modules

import
   ↓
Import a module

from ... import
   ↓
Import specific objects

as
   ↓
Create an alias

__name__
   ↓
Identifies the current module

__main__
   ↓
Indicates direct execution

__init__.py
   ↓
Package initialization / package structure

Absolute Import
   ↓
Complete import path

Relative Import
   ↓
Import relative to current package
```

---

# 🚀 26. What You Should Build

To master Modules & Packages, build:

### 🧮 Calculator Package

```text
calculator/
├── __init__.py
├── arithmetic.py
├── scientific.py
└── main.py
```

### 🛒 Shopping Package

```text
shopping/
├── __init__.py
├── products.py
├── cart.py
├── customers.py
└── main.py
```

### 👨‍💻 Utility Package

```text
utilities/
├── __init__.py
├── math_utils.py
├── string_utils.py
├── file_utils.py
└── validation.py
```

---

# 📚 Official References

* [Python Tutorial — Modules](https://docs.python.org/3/tutorial/modules.html)
* [Python Language Reference — Import System](https://docs.python.org/3/reference/import.html)
* [Python Standard Library](https://docs.python.org/3/library/)
* [Python Packaging User Guide](https://packaging.python.org/)

Python's official documentation provides the core reference for modules and the import system, while the Python Packaging User Guide covers creating and distributing packages. ([Python documentation][2])

---

# 🎯 Key Takeaway

> **Modules help you organize reusable code. Packages help you organize modules into scalable application structures.**

A strong Python developer should not only know how to write functions, but also know how to **structure, reuse, import, and maintain code across a real project**.

---

## ⏭️ Next Topic

➡️ **[12 — File Handling](../12-File-Handling/)**

Continue the Python learning journey:

```text
Functions
    ↓
Modules & Packages
    ↓
File Handling
    ↓
Exception Handling
    ↓
OOP
    ↓
Advanced Python
```

---

⭐ **Keep coding. Keep building. Keep learning Python.**

[1]: https://github.com/Kishor055/Python-Programming "GitHub - Kishor055/Python-Programming: Learn Python from Basics to Advanced with Theory, Practical Code, Outputs, DSA, Projects, and Interview Preparation. · GitHub"
[2]: https://docs.python.org/3.14/tutorial/modules.html?utm_source=chatgpt.com "6. Modules — Python 3.14.6 documentation"
[3]: https://github.com/python/cpython/blob/main/Doc/tutorial/modules.rst?plain=1&utm_source=chatgpt.com "cpython/Doc/tutorial/modules.rst at main · python/cpython · GitHub"
[4]: https://packaging.python.org/en/latest/tutorials/packaging-projects/?utm_source=chatgpt.com "Packaging Python Projects - Python Packaging User Guide"
