# 🐍 Python Intermediate Interview Questions

A structured collection of **intermediate-level Python interview questions with clear answers, explanations, examples, and practical coding problems**.

This section is designed for learners who already understand Python fundamentals and want to prepare for technical interviews, internships, and entry-level developer roles.

---

## 📚 Table of Contents

* [1. What is list comprehension?](#1-what-is-list-comprehension)
* [2. What is dictionary comprehension?](#2-what-is-dictionary-comprehension)
* [3. What is set comprehension?](#3-what-is-set-comprehension)
* [4. What are `*args` and `**kwargs`?](#4-what-are-args-and-kwargs)
* [5. What are default arguments?](#5-what-are-default-arguments)
* [6. What are keyword arguments?](#6-what-are-keyword-arguments)
* [7. What is variable scope?](#7-what-is-variable-scope)
* [8. What is LEGB?](#8-what-is-legb)
* [9. What is a closure?](#9-what-is-a-closure)
* [10. What is a decorator?](#10-what-is-a-decorator)
* [11. What is an iterator?](#11-what-is-an-iterator)
* [12. What is a generator?](#12-what-is-a-generator)
* [13. `yield` vs `return`](#13-what-is-the-difference-between-yield-and-return)
* [14. What is a class?](#14-what-is-a-class)
* [15. What is an object?](#15-what-is-an-object)
* [16. What is inheritance?](#16-what-is-inheritance)
* [17. What is method overriding?](#17-what-is-method-overriding)
* [18. What is `super()`?](#18-what-is-super)
* [19. What is polymorphism?](#19-what-is-polymorphism)
* [20. What is encapsulation?](#20-what-is-encapsulation)
* [21. What is abstraction?](#21-what-is-abstraction)
* [22. Class variable vs instance variable](#22-class-variable-vs-instance-variable)
* [23. What are magic methods?](#23-what-are-magic-methods)
* [24. What is `__str__()`?](#24-what-is-str)
* [25. What is `__repr__()`?](#25-what-is-repr)
* [26. What is exception handling?](#26-what-is-exception-handling)
* [27. `raise` vs `assert`](#27-raise-vs-assert)
* [28. What is a custom exception?](#28-what-is-a-custom-exception)
* [29. What is a context manager?](#29-what-is-a-context-manager)
* [30. What is a module?](#30-what-is-a-module)
* [31. What is a package?](#31-what-is-a-package)
* [32. What is `__name__ == "__main__"`?](#32-what-is-name--main)
* [33. What is a virtual environment?](#33-what-is-a-virtual-environment)
* [34. What is shallow copy?](#34-what-is-shallow-copy)
* [35. What is deep copy?](#35-what-is-deep-copy)
* [36. What is garbage collection?](#36-what-is-garbage-collection)
* [37. What is duck typing?](#37-what-is-duck-typing)
* [38. What is method resolution order?](#38-what-is-method-resolution-order)
* [39. What is multiple inheritance?](#39-what-is-multiple-inheritance)
* [40. Coding interview problems](#40-coding-interview-problems)

---

# 1. What is List Comprehension?

### Answer

List comprehension provides a concise way to create a list from an iterable.

### Normal approach

```python
squares = []

for number in range(1, 6):
    squares.append(number ** 2)
```

### List comprehension

```python
squares = [number ** 2 for number in range(1, 6)]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

### With a condition

```python
even_numbers = [
    number
    for number in range(1, 11)
    if number % 2 == 0
]

print(even_numbers)
```

Output:

```text
[2, 4, 6, 8, 10]
```

---

# 2. What is Dictionary Comprehension?

### Answer

Dictionary comprehension provides a concise way to create dictionaries.

Example:

```python
squares = {
    number: number ** 2
    for number in range(1, 6)
}

print(squares)
```

Output:

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

# 3. What is Set Comprehension?

### Answer

Set comprehension creates a set using a compact syntax.

Example:

```python
squares = {
    number ** 2
    for number in range(1, 6)
}

print(squares)
```

Output:

```text
{1, 4, 9, 16, 25}
```

Like normal sets, the resulting collection contains unique elements.

---

# 4. What are `*args` and `**kwargs`?

### Answer

`*args` allows a function to accept a variable number of positional arguments.

`**kwargs` allows a function to accept a variable number of keyword arguments.

Example:

```python
def display(*args, **kwargs):
    print("Arguments:", args)
    print("Keyword arguments:", kwargs)


display(10, 20, 30, name="Kishor", age=21)
```

Output:

```text
Arguments: (10, 20, 30)
Keyword arguments: {'name': 'Kishor', 'age': 21}
```

---

# 5. What are Default Arguments?

### Answer

A default argument is a parameter that has a predefined value.

Example:

```python
def greet(name="Guest"):
    print("Hello", name)


greet()
greet("Kishor")
```

Output:

```text
Hello Guest
Hello Kishor
```

### Important

Default parameter values are evaluated when the function is defined. Avoid using mutable objects such as lists or dictionaries as defaults unless that shared-state behavior is intentional.

Prefer:

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

---

# 6. What are Keyword Arguments?

### Answer

Keyword arguments are passed using parameter names.

Example:

```python
def student(name, age):
    print(name, age)


student(age=21, name="Kishor")
```

Output:

```text
Kishor 21
```

Keyword arguments make function calls more readable and allow arguments to be supplied by name.

---

# 7. What is Variable Scope?

### Answer

Scope determines where a variable can be accessed.

Python commonly has:

* Local scope
* Enclosing scope
* Global scope
* Built-in scope

Example:

```python
name = "Global"


def show():
    name = "Local"
    print(name)


show()
print(name)
```

Output:

```text
Local
Global
```

---

# 8. What is LEGB?

### Answer

LEGB describes the order Python uses when resolving a name:

```text
L → Local
E → Enclosing
G → Global
B → Built-in
```

Example:

```python
x = "Global"


def outer():
    x = "Enclosing"

    def inner():
        x = "Local"
        print(x)

    inner()


outer()
```

Output:

```text
Local
```

Python searches the local scope first, followed by enclosing, global, and built-in scopes.

---

# 9. What is a Closure?

### Answer

A closure occurs when an inner function remembers and accesses variables from its enclosing function even after the enclosing function has finished executing.

Example:

```python
def multiplier(factor):

    def multiply(number):
        return number * factor

    return multiply


double = multiplier(2)

print(double(5))
```

Output:

```text
10
```

The `multiply()` function remembers the value of `factor`.

---

# 10. What is a Decorator?

### Answer

A decorator is a callable that takes another callable and returns a callable with modified or extended behavior.

Example:

```python
def logger(func):

    def wrapper():
        print("Function started")
        func()
        print("Function finished")

    return wrapper


@logger
def hello():
    print("Hello Python!")


hello()
```

Output:

```text
Function started
Hello Python!
Function finished
```

Decorators are commonly used for:

* Logging
* Authentication
* Timing
* Validation
* Caching

---

# 11. What is an Iterator?

### Answer

An iterator is an object that implements the iterator protocol.

It provides:

```python
__iter__()
__next__()
```

Example:

```python
numbers = iter([10, 20, 30])

print(next(numbers))
print(next(numbers))
print(next(numbers))
```

Output:

```text
10
20
30
```

When there are no more values, `next()` raises `StopIteration`.

---

# 12. What is a Generator?

### Answer

A generator is a special kind of iterator that produces values lazily, usually using `yield`.

Example:

```python
def numbers():
    for number in range(1, 4):
        yield number


for number in numbers():
    print(number)
```

Output:

```text
1
2
3
```

Generators are useful when working with large or potentially infinite sequences because values can be produced one at a time.

---

# 13. What is the Difference Between `yield` and `return`?

### Answer

`return` ends a function and sends back a result.

`yield` produces a value from a generator and pauses execution so the generator can continue later.

### `return`

```python
def get_number():
    return 10
```

### `yield`

```python
def get_numbers():
    yield 10
    yield 20
```

The second function returns a generator object.

---

# 14. What is a Class?

### Answer

A class is a blueprint for creating objects.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)
```

The class defines the data and behavior that its objects can have.

---

# 15. What is an Object?

### Answer

An object is an instance of a class.

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

Here, `student` is an object of the `Student` class.

---

# 16. What is Inheritance?

### Answer

Inheritance allows a class to derive behavior from another class.

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

# 17. What is Method Overriding?

### Answer

Method overriding occurs when a subclass provides its own implementation of a method inherited from its parent class.

Example:

```python
class Animal:

    def sound(self):
        print("Some sound")


class Dog(Animal):

    def sound(self):
        print("Bark")


dog = Dog()

dog.sound()
```

Output:

```text
Bark
```

---

# 18. What is `super()`?

### Answer

`super()` provides a convenient way to access methods or attributes from a parent class.

Example:

```python
class Animal:

    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


dog = Dog("Buddy", "Labrador")

print(dog.name)
print(dog.breed)
```

Output:

```text
Buddy
Labrador
```

---

# 19. What is Polymorphism?

### Answer

Polymorphism allows the same interface or operation to work with different types of objects.

Example:

```python
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
```

Output:

```text
Bark
Meow
```

The same method call, `sound()`, produces different behavior.

---

# 20. What is Encapsulation?

### Answer

Encapsulation means keeping data and behavior together and controlling how internal implementation details are accessed.

Python uses naming conventions and name mangling rather than strict private access modifiers.

Example:

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

print(account.get_balance())
```

Output:

```text
5000
```

The double underscore triggers name mangling for `__balance`.

---

# 21. What is Abstraction?

### Answer

Abstraction means defining an interface while hiding implementation details.

Python provides abstract base classes through the `abc` module.

Example:

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")


dog = Dog()
dog.sound()
```

Output:

```text
Bark
```

---

# 22. Class Variable vs Instance Variable

### Answer

A **class variable** belongs to the class and is shared by instances unless an instance provides its own attribute.

An **instance variable** belongs to a particular object.

Example:

```python
class Student:

    school = "ABC College"

    def __init__(self, name):
        self.name = name


student1 = Student("Kishor")
student2 = Student("Rahul")

print(student1.school)
print(student2.school)
```

Both objects can access the same class variable.

---

# 23. What are Magic Methods?

### Answer

Magic methods, also called **dunder methods**, have names beginning and ending with double underscores.

Examples:

```text
__init__
__str__
__repr__
__len__
__eq__
__add__
```

They allow objects to interact naturally with Python syntax and built-in operations.

---

# 24. What is `__str__()`?

### Answer

`__str__()` defines the human-readable string representation of an object.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student: {self.name}"


student = Student("Kishor")

print(student)
```

Output:

```text
Student: Kishor
```

---

# 25. What is `__repr__()`?

### Answer

`__repr__()` is intended to provide a useful representation of an object, often one that is helpful for debugging.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Student(name={self.name!r})"


student = Student("Kishor")

print(repr(student))
```

Output:

```text
Student(name='Kishor')
```

A common convention is for `__repr__()` to be more detailed and unambiguous than `__str__()`.

---

# 26. What is Exception Handling?

### Answer

Exception handling allows a program to respond to runtime errors without necessarily terminating unexpectedly.

Python provides:

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
    print("Result:", result)

finally:
    print("Execution completed.")
```

---

# 27. `raise` vs `assert`

### `raise`

`raise` explicitly raises an exception.

```python
age = -1

if age < 0:
    raise ValueError("Age cannot be negative")
```

### `assert`

`assert` checks a condition and raises `AssertionError` if the condition is false.

```python
age = 20

assert age >= 0
```

Assertions are mainly useful for debugging and internal assumptions. They can be disabled with Python's optimization options, so they should not replace normal runtime validation.

---

# 28. What is a Custom Exception?

### Answer

A custom exception is an exception class created by the programmer.

Example:

```python
class InsufficientBalanceError(Exception):
    pass


balance = 100
withdraw = 200

if withdraw > balance:
    raise InsufficientBalanceError("Insufficient balance")
```

Custom exceptions make application-specific errors clearer.

---

# 29. What is a Context Manager?

### Answer

A context manager manages setup and cleanup around a block of code.

The `with` statement is commonly used with context managers.

Example:

```python
with open("data.txt", "r") as file:
    content = file.read()
```

The file is automatically closed when the `with` block exits.

---

# 30. What is a Module?

### Answer

A module is a Python file containing reusable code.

Example:

```text
math_utils.py
```

```python
def add(a, b):
    return a + b
```

Another file can import it:

```python
import math_utils

print(math_utils.add(10, 20))
```

---

# 31. What is a Package?

### Answer

A package organizes related Python modules into a directory structure.

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

Packages help structure larger applications.

---

# 32. What is `__name__ == "__main__"`?

### Answer

When a Python file is executed directly, Python sets its `__name__` value to `"__main__"`.

This allows code to behave differently when:

* The file is executed directly.
* The file is imported as a module.

Example:

```python
def main():
    print("Program started")


if __name__ == "__main__":
    main()
```

When imported, the `main()` call does not execute automatically.

---

# 33. What is a Virtual Environment?

### Answer

A virtual environment creates an isolated Python environment for a project.

This allows different projects to use different dependency versions.

Create one:

```bash
python -m venv venv
```

Activate on Windows:

```bash
venv\Scripts\activate
```

Activate on macOS/Linux:

```bash
source venv/bin/activate
```

Deactivate:

```bash
deactivate
```

---

# 34. What is Shallow Copy?

### Answer

A shallow copy creates a new outer object, but nested objects may still be shared.

Example:

```python
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)

shallow[0].append(99)

print(original)
```

Output:

```text
[[1, 2, 99], [3, 4]]
```

The nested list is shared.

---

# 35. What is Deep Copy?

### Answer

A deep copy recursively copies nested objects.

Example:

```python
import copy

original = [[1, 2], [3, 4]]

deep = copy.deepcopy(original)

deep[0].append(99)

print(original)
print(deep)
```

Output:

```text
[[1, 2], [3, 4]]
[[1, 2, 99], [3, 4]]
```

The nested structures are independent.

---

# 36. What is Garbage Collection?

### Answer

Garbage collection is the process of reclaiming memory associated with objects that are no longer reachable.

In CPython, reference counting handles many objects immediately, while a cyclic garbage collector helps detect reference cycles.

Python generally handles memory management automatically.

Example:

```python
import gc

gc.collect()
```

---

# 37. What is Duck Typing?

### Answer

Duck typing focuses on what an object **can do** rather than its exact type.

The idea is commonly summarized as:

> If an object supports the required operation, it can be used.

Example:

```python
class Dog:

    def speak(self):
        print("Bark")


class Person:

    def speak(self):
        print("Hello")


def make_speak(obj):
    obj.speak()


make_speak(Dog())
make_speak(Person())
```

Output:

```text
Bark
Hello
```

The function does not require a specific class; it only requires an object that provides `speak()`.

---

# 38. What is Method Resolution Order?

### Answer

Method Resolution Order (MRO) is the order Python follows when searching for methods and attributes in a class hierarchy.

You can inspect it using:

```python
ClassName.mro()
```

Example:

```python
class A:
    pass


class B(A):
    pass


print(B.mro())
```

Output:

```text
[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
```

Python uses the **C3 linearization algorithm** to determine MRO.

---

# 39. What is Multiple Inheritance?

### Answer

Multiple inheritance occurs when a class inherits from more than one parent class.

Example:

```python
class Father:

    def skills(self):
        print("Driving")


class Mother:

    def talent(self):
        print("Cooking")


class Child(Father, Mother):
    pass


child = Child()

child.skills()
child.talent()
```

Output:

```text
Driving
Cooking
```

When multiple inheritance is used, understanding MRO is important.

---

# 40. Coding Interview Problems

## Q40.1 Reverse a String

### Problem

Reverse a string without using a dedicated reverse function.

### Solution

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

## Q40.2 Remove Duplicates From a List

### Solution

If preserving insertion order is important:

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

## Q40.3 Count Character Frequency

### Solution

```python
from collections import Counter

text = "python"

frequency = Counter(text)

print(frequency)
```

Output:

```text
Counter({'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1})
```

---

## Q40.4 Find the Second Largest Number

### Solution

```python
numbers = [10, 20, 5, 40, 30]

unique_numbers = sorted(set(numbers))

second_largest = unique_numbers[-2]

print(second_largest)
```

Output:

```text
30
```

This approach treats duplicate values as one value.

---

## Q40.5 Check Whether Two Strings Are Anagrams

### Solution

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

## Q40.6 Find Common Elements in Two Lists

### Solution

```python
first = [1, 2, 3, 4]
second = [3, 4, 5, 6]

common = list(set(first) & set(second))

print(common)
```

Output:

```text
[3, 4]
```

For applications where order matters, a different approach may be preferable.

---

## Q40.7 Find the Most Frequent Element

### Solution

```python
from collections import Counter

numbers = [1, 2, 2, 3, 2, 4]

most_common = Counter(numbers).most_common(1)[0]

print(most_common)
```

Output:

```text
(2, 3)
```

The tuple contains:

```text
(element, frequency)
```

---

## Q40.8 Flatten a Nested List

### Solution

For a list containing one level of nested lists:

```python
nested = [[1, 2], [3, 4], [5, 6]]

flat = [
    item
    for group in nested
    for item in group
]

print(flat)
```

Output:

```text
[1, 2, 3, 4, 5, 6]
```

---

## Q40.9 Find Missing Number

### Problem

Given numbers from `1` to `n` with one number missing, find the missing number.

### Solution

```python
numbers = [1, 2, 3, 5, 6]

n = 6

expected = n * (n + 1) // 2
actual = sum(numbers)

missing = expected - actual

print(missing)
```

Output:

```text
4
```

---

## Q40.10 Find Word Frequency

### Solution

```python
from collections import Counter

text = "python is easy and python is powerful"

words = text.split()

frequency = Counter(words)

print(frequency)
```

Output:

```text
Counter({
    'python': 2,
    'is': 2,
    'easy': 1,
    'and': 1,
    'powerful': 1
})
```

---

# 🎯 Common Intermediate Interview Comparisons

| Concept                    | Difference                                                |
| -------------------------- | --------------------------------------------------------- |
| List vs Tuple              | Mutable vs immutable                                      |
| `==` vs `is`               | Value equality vs object identity                         |
| `return` vs `yield`        | Ends function vs produces generator values                |
| Iterator vs Generator      | Generator is a convenient way to create an iterator       |
| Shallow vs Deep Copy       | Nested objects may be shared vs recursively copied        |
| `raise` vs `assert`        | Explicit exception vs debugging/internal assumption check |
| Class vs Object            | Blueprint vs instance                                     |
| Instance vs Class Variable | Object-specific vs class-level                            |
| `__str__` vs `__repr__`    | Human-readable vs developer/debug representation          |
| Module vs Package          | Python file vs organized collection of modules            |
| `break` vs `continue`      | Exit loop vs skip current iteration                       |

---

# 🧠 Intermediate Interview Tips

### 1. Understand the "Why"

Don't only memorize syntax.

For example, don't just memorize:

```python
yield
```

Understand that generators allow values to be produced lazily.

### 2. Practice Output Questions

Interviewers often test understanding using short programs involving:

* References
* Mutability
* Scope
* Loops
* Functions
* Classes

### 3. Explain Your Code

For coding questions, explain:

```text
Problem
   ↓
Approach
   ↓
Implementation
   ↓
Complexity
   ↓
Edge Cases
```

### 4. Know Common Python Tools

Be comfortable with:

```python
enumerate()
zip()
map()
filter()
sorted()
sum()
min()
max()
any()
all()
```

### 5. Practice Without IDE Assistance

Try solving small problems using only:

* Python interpreter
* Text editor
* Whiteboard/paper

This improves interview problem-solving skills.

---

# 📈 Intermediate Preparation Path

```text
Beginner Python
       ↓
Collections
       ↓
Functions
       ↓
Comprehensions
       ↓
Scope & Closures
       ↓
Decorators
       ↓
OOP
       ↓
Exceptions
       ↓
Iterators & Generators
       ↓
Context Managers
       ↓
Memory Management
       ↓
Coding Problems
       ↓
Advanced Python
```

---

# ✅ Intermediate Interview Checklist

* [ ] List comprehensions
* [ ] Dictionary comprehensions
* [ ] Set comprehensions
* [ ] `*args`
* [ ] `**kwargs`
* [ ] Default arguments
* [ ] Keyword arguments
* [ ] Variable scope
* [ ] LEGB
* [ ] Closures
* [ ] Decorators
* [ ] Iterators
* [ ] Generators
* [ ] `yield`
* [ ] Classes
* [ ] Objects
* [ ] Inheritance
* [ ] Method overriding
* [ ] `super()`
* [ ] Polymorphism
* [ ] Encapsulation
* [ ] Abstraction
* [ ] Magic methods
* [ ] Exception handling
* [ ] Custom exceptions
* [ ] Context managers
* [ ] Modules
* [ ] Packages
* [ ] Virtual environments
* [ ] Shallow copy
* [ ] Deep copy
* [ ] Garbage collection
* [ ] Duck typing
* [ ] MRO
* [ ] Multiple inheritance
* [ ] Coding problems

---

# 🚀 Keep Growing

```text
📖 Learn
   ↓
💻 Code
   ↓
🧪 Test
   ↓
🐛 Debug
   ↓
🧠 Understand
   ↓
🗣️ Explain
   ↓
🚀 Build
```

> **Don't memorize Python. Understand how Python works.**

---

## 🔗 Navigation

⬅️ **Previous:** [`beginner.md`](./beginner.md)

➡️ **Next:** [`advanced.md`](./advanced.md)

🏠 **Back to Interview Questions:** [`README.md`](./README.md)

---

⭐ **Keep Learning Python. Keep Practicing. Keep Growing. 🚀**
