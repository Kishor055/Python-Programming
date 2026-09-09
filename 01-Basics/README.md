# 🐍 Python Basics

> A structured, beginner-friendly introduction to Python fundamentals — with theory, practical examples, expected output, common mistakes, and exercises.

This module covers the essential concepts every Python programmer should understand before moving to operators, conditions, loops, functions, data structures, and object-oriented programming.

---

## 📚 Topics Covered

| #  | Topic          | File                                         |
| -- | -------------- | -------------------------------------------- |
| 01 | Hello World    | [`01_hello_world.py`](./01_hello_world.py)   |
| 02 | Comments       | [`02_comments.py`](./02_comments.py)         |
| 03 | Variables      | [`03_variables.py`](./03_variables.py)       |
| 04 | Data Types     | [`04_data_types.py`](./04_data_types.py)     |
| 05 | Input & Output | [`05_input_output.py`](./05_input_output.py) |
| 06 | Type Casting   | [`06_type_casting.py`](./06_type_casting.py) |

---

# 🎯 Learning Objectives

By completing this module, you should be able to:

* Understand what Python is.
* Write and execute a basic Python program.
* Understand Python syntax.
* Use comments effectively.
* Create and use variables.
* Understand Python's built-in data types.
* Take input from users.
* Display formatted output.
* Convert values from one data type to another.
* Identify common beginner errors.
* Write small Python programs independently.

---

# 1. Hello World

📄 **File:** [`01_hello_world.py`](./01_hello_world.py)

## 📖 Theory

The first program traditionally written when learning a programming language is a program that displays:

```text
Hello, World!
```

In Python, we can do this using the built-in `print()` function.

### Example

```python
print("Hello, World!")
```

### Output

```text
Hello, World!
```

### How it works

```text
print("Hello, World!")
  │
  ├── print → built-in Python function
  │
  └── "Hello, World!" → string passed to the function
```

`print()` sends the supplied value to the standard output, normally your terminal or console.

---

## Printing Multiple Values

```python
name = "Alice"
age = 25

print(name)
print(age)
```

Output:

```text
Alice
25
```

You can also print multiple values in one call:

```python
print("Name:", name, "Age:", age)
```

Output:

```text
Name: Alice Age: 25
```

---

## Printing Expressions

`print()` can also display the result of an expression.

```python
print(10 + 20)
```

Output:

```text
30
```

Another example:

```python
a = 10
b = 5

print(a + b)
print(a * b)
```

Output:

```text
15
50
```

---

## 💡 Key Takeaways

* `print()` is a built-in Python function.
* Text is usually written inside quotes.
* Numbers do not require quotes.
* `print()` can display values and expressions.
* Python statements normally do not require a semicolon.

---

# 2. Comments

📄 **File:** [`02_comments.py`](./02_comments.py)

## 📖 Theory

Comments are text written in source code to provide information to programmers.

Python does not execute comments as program instructions.

Comments are useful for:

* Explaining code
* Documenting decisions
* Making code easier to understand
* Temporarily disabling a line while debugging
* Helping other developers understand your program

---

## Single-Line Comments

A comment begins with `#`.

```python
# This is a comment

print("Hello, Python!")
```

Output:

```text
Hello, Python!
```

Python ignores:

```python
# This is a comment
```

and executes:

```python
print("Hello, Python!")
```

---

## Inline Comments

A comment can also appear after executable code.

```python
age = 25  # Store the user's age

print(age)
```

---

## Writing Good Comments

### ❌ Poor comment

```python
age = 25  # Assign 25 to age
```

The code already makes this obvious.

### ✅ Useful comment

```python
# Age is required to determine whether the user can register.
age = 25
```

A good comment explains **why**, not something obvious about **what**.

---

## Comments and Documentation

For functions, classes, and modules, Python commonly uses **docstrings** for documentation.

Example:

```python
def greet(name):
    """Return a greeting for the given name."""
    return f"Hello, {name}"
```

Docstrings are different from ordinary `#` comments because they can be accessed programmatically.

---

## 💡 Best Practices

Use comments when they add useful context.

Avoid:

```python
# Print hello
print("Hello")
```

Prefer:

```python
# Display a welcome message when the application starts.
print("Hello")
```

---

# 3. Variables

📄 **File:** [`03_variables.py`](./03_variables.py)

## 📖 Theory

A variable is a name that refers to a value/object.

Example:

```python
name = "Alice"
```

Here:

```text
name  ───────►  "Alice"
```

The name `name` refers to a string object containing `"Alice"`.

---

## Creating Variables

Python does not require you to declare a variable's type separately.

```python
name = "Alice"
age = 25
height = 5.7
is_student = True
```

Python determines the type from the assigned value.

---

## Variable Assignment

The `=` symbol is the assignment operator.

```python
age = 25
```

Think of this as:

> Make the name `age` refer to the object `25`.

It is different from mathematical equality.

---

## Accessing Variables

```python
name = "Alice"

print(name)
```

Output:

```text
Alice
```

---

## Reassigning Variables

A variable can be assigned a different object later.

```python
score = 50

print(score)

score = 100

print(score)
```

Output:

```text
50
100
```

The name `score` now refers to the new value.

---

## Multiple Assignment

Python allows multiple variables to be assigned in one statement.

```python
name, age, city = "Alice", 25, "Pune"
```

This is equivalent to:

```python
name = "Alice"
age = 25
city = "Pune"
```

---

## Assigning the Same Value

```python
x = y = z = 0
```

Now all three names refer to the value `0`.

---

## Swapping Variables

Python makes swapping values simple:

```python
a = 10
b = 20

a, b = b, a

print(a)
print(b)
```

Output:

```text
20
10
```

No temporary variable is required.

---

# Variable Naming Rules

A Python identifier:

* Can contain letters.
* Can contain digits.
* Can contain underscores.
* Cannot begin with a digit.
* Cannot contain spaces.
* Cannot be a Python keyword.
* Is case-sensitive.

### Valid

```python
name = "Alice"
student_name = "Bob"
age2 = 20
_private_value = 100
```

### Invalid

```python
# 2name = "Alice"
# student-name = "Bob"
# student name = "Alice"
# class = "Python"
```

---

# Case Sensitivity

Python is case-sensitive.

These are different names:

```python
name = "Alice"
Name = "Bob"
NAME = "Charlie"
```

They refer to separate variables.

---

# Naming Convention

Python commonly uses `snake_case` for variables.

### Recommended

```python
first_name = "Alice"
student_age = 20
total_price = 500
```

### Avoid unclear names

```python
x = "Alice"
a = 20
p = 500
```

unless the context makes those names meaningful.

---

# Variables and Types

A variable does not permanently have one type.

```python
value = 100

print(type(value))

value = "Python"

print(type(value))
```

Output:

```text
<class 'int'>
<class 'str'>
```

This is one aspect of Python's **dynamic typing**.

---

## 💡 Key Takeaways

* Variables are names referring to objects.
* `=` performs assignment.
* Python does not require explicit variable declarations.
* Variable names are case-sensitive.
* Use descriptive names.
* Prefer `snake_case` for ordinary variables.
* Python supports multiple assignment.
* Variables can be reassigned.

---

# 4. Data Types

📄 **File:** [`04_data_types.py`](./04_data_types.py)

## 📖 Theory

A data type describes the kind of object/value a program is working with.

Python provides many built-in types.

Some fundamental types are:

| Type       | Example             | Description                 |
| ---------- | ------------------- | --------------------------- |
| `int`      | `10`                | Integer                     |
| `float`    | `10.5`              | Floating-point number       |
| `complex`  | `2 + 3j`            | Complex number              |
| `str`      | `"Python"`          | Text                        |
| `bool`     | `True`              | Boolean value               |
| `NoneType` | `None`              | Absence of a value          |
| `list`     | `[1, 2, 3]`         | Mutable sequence            |
| `tuple`    | `(1, 2, 3)`         | Immutable sequence          |
| `set`      | `{1, 2, 3}`         | Collection of unique values |
| `dict`     | `{"name": "Alice"}` | Key-value mapping           |

The collection types will be covered in greater detail later.

---

# Integer — `int`

Integers are whole numbers.

```python
age = 25
temperature = -10
count = 0
```

Example:

```python
x = 100

print(x)
print(type(x))
```

Output:

```text
100
<class 'int'>
```

---

# Floating Point — `float`

Floating-point numbers represent numbers with a fractional component.

```python
price = 99.99
temperature = 36.5
```

Example:

```python
x = 10.5

print(x)
print(type(x))
```

Output:

```text
10.5
<class 'float'>
```

---

# Complex — `complex`

Python supports complex numbers.

```python
z = 2 + 3j

print(z)
print(type(z))
```

Output:

```text
(2+3j)
<class 'complex'>
```

Here:

* `2` is the real part.
* `3` is the imaginary part.

---

# String — `str`

Strings represent text.

```python
name = "Alice"
language = 'Python'
```

Single or double quotes can be used.

```python
name1 = "Alice"
name2 = 'Alice'
```

Both create strings containing the same text.

### String example

```python
message = "Welcome to Python"

print(message)
print(type(message))
```

Output:

```text
Welcome to Python
<class 'str'>
```

---

# Boolean — `bool`

Boolean values represent truth values.

Python has two Boolean values:

```python
True
False
```

Example:

```python
is_logged_in = True
is_admin = False

print(is_logged_in)
print(type(is_logged_in))
```

Output:

```text
True
<class 'bool'>
```

Booleans are heavily used with conditions and logical operations.

---

# None — `NoneType`

`None` represents the absence of a value.

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

`None` is not the same as:

```python
0
False
""
```

It specifically represents no value in contexts where that distinction matters.

---

# Checking Types with `type()`

The built-in `type()` function tells you the type of an object.

```python
print(type(10))
print(type(10.5))
print(type("Python"))
print(type(True))
print(type(None))
```

Output:

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
<class 'NoneType'>
```

---

# Dynamic Typing

Python is dynamically typed.

```python
value = 10

print(type(value))

value = "Hello"

print(type(value))
```

Output:

```text
<class 'int'>
<class 'str'>
```

The same variable name can refer to objects of different types at different points in the program.

---

## 💡 Key Takeaways

Remember these fundamental types first:

```text
int       → whole numbers
float     → decimal numbers
complex   → complex numbers
str       → text
bool      → True / False
NoneType  → absence of a value
```

---

# 5. Input & Output

📄 **File:** [`05_input_output.py`](./05_input_output.py)

## 📖 Theory

Most programs need two fundamental capabilities:

```text
Input  → receive information
Output → display information
```

Python provides built-in functions for both.

```python
input()
print()
```

---

# Taking Input

The `input()` function reads a line of text from the user.

```python
name = input("Enter your name: ")

print("Hello", name)
```

Example:

```text
Enter your name: Alice
Hello Alice
```

---

## Important: `input()` Returns a String

Consider:

```python
age = input("Enter your age: ")

print(type(age))
```

If the user enters:

```text
25
```

the type is:

```text
<class 'str'>
```

Even though the user entered digits, `input()` returns text.

This is a very important concept for beginners.

---

# Taking Numeric Input

If you need an integer, convert the input:

```python
age = int(input("Enter your age: "))

print(age)
```

For decimal values:

```python
price = float(input("Enter the price: "))

print(price)
```

---

# Output with `print()`

Basic output:

```python
print("Hello, Python!")
```

You can print multiple values:

```python
name = "Alice"
age = 25

print("Name:", name)
print("Age:", age)
```

Output:

```text
Name: Alice
Age: 25
```

---

# Custom Separator

`print()` allows you to specify how multiple arguments are separated.

```python
print("Python", "Java", "C++", sep=" | ")
```

Output:

```text
Python | Java | C++
```

---

# Custom Ending

By default, `print()` ends with a newline.

You can change this using `end`.

```python
print("Hello", end=" ")
print("World")
```

Output:

```text
Hello World
```

---

# Formatted Output with f-Strings

f-strings are a clean way to insert values into strings.

```python
name = "Alice"
age = 25

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Alice and I am 25 years old.
```

You can also evaluate expressions:

```python
a = 10
b = 20

print(f"Sum = {a + b}")
```

Output:

```text
Sum = 30
```

---

# Complete Input/Output Example

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print()
print("----- Profile -----")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
```

Example:

```text
Enter your name: Alice
Enter your age: 25
Enter your city: Pune

----- Profile -----
Name: Alice
Age: 25
City: Pune
```

---

## 💡 Key Takeaways

* `input()` receives user input.
* `input()` returns a string.
* Use `int()` for integer input.
* Use `float()` for decimal input.
* `print()` displays output.
* `sep` controls the separator between printed values.
* `end` controls what is printed after the output.
* f-strings are useful for readable formatted output.

---

# 6. Type Casting

📄 **File:** [`06_type_casting.py`](./06_type_casting.py)

## 📖 Theory

Type casting, also called **type conversion**, means converting a value from one data type to another.

Common conversion functions include:

```python
int()
float()
str()
bool()
```

---

# String → Integer

```python
age = "25"

age = int(age)

print(age)
print(type(age))
```

Output:

```text
25
<class 'int'>
```

---

# Integer → Float

```python
number = 10

result = float(number)

print(result)
print(type(result))
```

Output:

```text
10.0
<class 'float'>
```

---

# Float → Integer

```python
number = 10.8

result = int(number)

print(result)
```

Output:

```text
10
```

### Important

Converting a float to an integer with `int()` **truncates the fractional part**. It does not round to the nearest integer.

```python
int(10.9)
```

produces:

```text
10
```

---

# Integer → String

```python
age = 25

text = str(age)

print(text)
print(type(text))
```

Output:

```text
25
<class 'str'>
```

This is useful when combining values with strings in situations where an f-string is not being used.

---

# String → Float

```python
price = "99.99"

price = float(price)

print(price)
print(type(price))
```

Output:

```text
99.99
<class 'float'>
```

---

# Value → Boolean

The `bool()` function converts a value to `True` or `False`.

```python
print(bool(1))
print(bool(0))
```

Output:

```text
True
False
```

Some common falsy values include:

```python
False
None
0
0.0
""
```

Empty collections such as `[]`, `{}`, and `()` are also falsy.

Many other values are truthy.

---

# Type Casting with Input

This is one of the most common uses of type conversion.

### Without conversion

```python
a = input("Enter first number: ")
b = input("Enter second number: ")

print(a + b)
```

If the user enters:

```text
10
20
```

the output is:

```text
1020
```

Why?

Because both values are strings:

```text
"10" + "20"
```

produces:

```text
"1020"
```

---

## Correct Version

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)
```

Input:

```text
10
20
```

Output:

```text
30
```

---

# Failed Type Conversion

Not every string can be converted to every type.

This works:

```python
int("100")
```

This does not:

```python
int("hello")
```

It raises:

```text
ValueError
```

Similarly:

```python
float("10.5")
```

works, while:

```python
float("Python")
```

does not.

Error handling will be covered later in the repository.

---

# Explicit vs Implicit Conversion

Python can perform some conversions automatically in expressions.

For example:

```python
result = 10 + 2.5

print(result)
print(type(result))
```

Output:

```text
12.5
<class 'float'>
```

The integer participates in the numeric operation with the float, and the result is a float.

Explicit conversion is when you request a conversion yourself:

```python
x = "100"

number = int(x)
```

---

## 💡 Key Takeaways

Remember the most common conversions:

```text
int()    → integer
float()  → floating-point number
str()    → string
bool()   → Boolean
```

And remember:

```python
input()
```

returns a string.

---

# 🧠 Common Beginner Mistakes

## 1. Forgetting that `input()` returns a string

### ❌

```python
age = input("Age: ")

print(age + 5)
```

### ✅

```python
age = int(input("Age: "))

print(age + 5)
```

---

## 2. Using quotes around numbers unnecessarily

### String

```python
age = "25"
```

### Integer

```python
age = 25
```

These are different types.

---

## 3. Using invalid variable names

### ❌

```python
student-name = "Alice"
```

### ✅

```python
student_name = "Alice"
```

---

## 4. Confusing `=` and `==`

Assignment:

```python
x = 10
```

Equality comparison:

```python
x == 10
```

`==` will be covered in detail in the Operators section.

---

## 5. Expecting `int()` to round

```python
int(9.99)
```

produces:

```text
9
```

It does not produce `10`.

---

# 🧪 Practice Problems

Try solving these without looking at a solution.

## Beginner

### 1. Hello User

Ask for the user's name and print:

```text
Hello, <name>!
```

---

### 2. Personal Information

Ask for:

* Name
* Age
* City

Display all three values.

---

### 3. Add Two Numbers

Take two integers from the user and print their sum.

Example:

```text
Enter first number: 10
Enter second number: 20

Sum: 30
```

---

### 4. Rectangle Area

Take length and width from the user.

Calculate:

```text
Area = length × width
```

---

### 5. Temperature Conversion

Take a temperature in Celsius and convert it to Fahrenheit.

Formula:

```text
F = (C × 9/5) + 32
```

---

## Intermediate

### 6. Student Profile

Create a program that accepts:

```text
Name
Age
Course
Marks
City
```

Display a formatted student profile.

---

### 7. Simple Bill

Ask for:

```text
Product name
Price
Quantity
```

Calculate:

```text
Total = price × quantity
```

Display the result using an f-string.

---

### 8. Type Inspector

Create variables containing:

```text
Integer
Float
String
Boolean
None
```

Print both the value and its type.

---

# 🎯 Mini Project

## Personal Profile Generator

Combine everything learned in this module.

Your program should:

1. Ask the user for their name.
2. Ask for their age.
3. Ask for their city.
4. Ask for their favorite programming language.
5. Display the information in a clean profile.

Example:

```text
===== Personal Profile =====

Name      : Alice
Age       : 25
City      : Pune
Language  : Python

============================
```

### Concepts Used

```text
Variables
Input
Output
Strings
Integers
Type Casting
f-strings
Comments
```

---

# 💼 Interview Concepts

Before moving forward, make sure you can answer these questions.

### Q1. What is a variable in Python?

A variable is a name that refers to an object/value.

### Q2. Is Python statically or dynamically typed?

Python is dynamically typed. A name can refer to objects of different types during execution.

### Q3. What does `input()` return?

`input()` returns a string.

### Q4. How do you convert a string to an integer?

```python
int("100")
```

### Q5. What is the difference between `"10"` and `10`?

```text
"10" → string
10   → integer
```

### Q6. What does `type()` do?

It returns the type of an object.

### Q7. What is `None`?

`None` is a singleton object commonly used to represent the absence of a value.

### Q8. What is type casting?

Type casting/type conversion is converting a value from one type to another.

### Q9. Is Python case-sensitive?

Yes.

```python
name
Name
NAME
```

are different identifiers.

### Q10. Why does this produce `1020`?

```python
a = input()
b = input()

print(a + b)
```

Because `input()` returns strings, so `"10" + "20"` produces `"1020"`.

---

# 📌 Quick Reference

## Output

```python
print("Hello")
```

## Input

```python
name = input("Enter name: ")
```

## Integer Input

```python
age = int(input("Enter age: "))
```

## Float Input

```python
price = float(input("Enter price: "))
```

## Variable

```python
name = "Alice"
```

## Type

```python
type(name)
```

## Type Conversion

```python
int(value)
float(value)
str(value)
bool(value)
```

## Formatted Output

```python
print(f"Hello, {name}")
```

---

# 🗺️ Learning Path

The recommended progression through this repository is:

```text
01 Basics
   │
   ├── Hello World
   ├── Comments
   ├── Variables
   ├── Data Types
   ├── Input & Output
   └── Type Casting
          │
          ▼
02 Operators
          │
          ▼
03 Conditional Statements
          │
          ▼
04 Loops
          │
          ▼
05 Strings
          │
          ▼
06 Lists
          │
          ▼
07 Tuples
          │
          ▼
08 Sets
          │
          ▼
09 Dictionaries
          │
          ▼
10 Functions
          │
          ▼
11 Modules & Packages
          │
          ▼
12 File Handling
          │
          ▼
13 Exception Handling
          │
          ▼
14 Object-Oriented Programming
          │
          ▼
15 Advanced Python
          │
          ▼
16 DSA with Python
          │
          ▼
17 Python Libraries
          │
          ▼
18 Projects
```

---

# ✅ Completion Checklist

### Fundamentals

* [ ] I can run a Python program.
* [ ] I understand `print()`.
* [ ] I can write comments.
* [ ] I understand variables.
* [ ] I know Python naming rules.
* [ ] I understand common data types.
* [ ] I can use `type()`.
* [ ] I understand `None`.
* [ ] I can take user input.
* [ ] I understand that `input()` returns a string.
* [ ] I can convert strings to numbers.
* [ ] I can use f-strings.
* [ ] I understand basic type conversion.
* [ ] I can identify common beginner errors.
* [ ] I completed the practice problems.
* [ ] I completed the mini project.

---

# 🚀 What's Next?

Once you are comfortable with these fundamentals, continue to:

## [`02-Operators`](../02-Operators/)

You will learn:

* Arithmetic operators
* Assignment operators
* Comparison operators
* Logical operators
* Identity operators
* Membership operators
* Bitwise operators
* Operator precedence
* Expressions

> **Learning tip:** Don't just read the examples. Type them yourself, run them, change the values, intentionally break the code, read the error, and fix it. Programming becomes easier when you actively experiment with the code.
