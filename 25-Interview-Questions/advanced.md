# 🐍 Advanced Python Interview Questions

> 🚀 **Advanced Python Interview Preparation**
> A practical collection of advanced Python interview questions covering **internals, memory management, OOP, decorators, generators, concurrency, asynchronous programming, metaprogramming, typing, performance, and advanced coding problems.**

---

## 📚 Table of Contents

* [1. What is Python's GIL?](#1-what-is-pythons-gil)
* [2. What is Garbage Collection?](#2-what-is-garbage-collection)
* [3. Reference Counting](#3-reference-counting)
* [4. `__slots__`](#4-__slots__)
* [5. `@property`](#5-property)
* [6. Static Method vs Class Method](#6-static-method-vs-class-method)
* [7. Abstract Base Classes](#7-abstract-base-classes)
* [8. Metaclasses](#8-metaclasses)
* [9. Descriptors](#9-descriptors)
* [10. `__new__()` vs `__init__()`](#10-new-vs-init)
* [11. Method Resolution Order](#11-method-resolution-order)
* [12. Monkey Patching](#12-monkey-patching)
* [13. First-Class Functions](#13-first-class-functions)
* [14. Higher-Order Functions](#14-higher-order-functions)
* [15. Closures and Late Binding](#15-closures-and-late-binding)
* [16. Advanced Decorators](#16-advanced-decorators)
* [17. Generator Expressions](#17-generator-expressions)
* [18. `yield from`](#18-yield-from)
* [19. Iterators vs Generators](#19-iterators-vs-generators)
* [20. Context Managers](#20-context-managers)
* [21. Async Programming](#21-async-programming)
* [22. `async` and `await`](#22-async-and-await)
* [23. Threading vs Multiprocessing](#23-threading-vs-multiprocessing)
* [24. Concurrent Futures](#24-concurrent-futures)
* [25. Pickling](#25-pickling)
* [26. Serialization vs Deserialization](#26-serialization-vs-deserialization)
* [27. Type Hints](#27-type-hints)
* [28. Dataclasses](#28-dataclasses)
* [29. Pattern Matching](#29-pattern-matching)
* [30. Walrus Operator](#30-walrus-operator)
* [31. Memoization](#31-memoization)
* [32. LRU Cache](#32-lru-cache)
* [33. Performance Optimization](#33-performance-optimization)
* [34. Memory Profiling](#34-memory-profiling)
* [35. Python Interning](#35-python-interning)
* [36. Mutable Default Arguments](#36-mutable-default-arguments)
* [37. `is` vs `==`](#37-is-vs-)
* [38. Dependency Injection](#38-dependency-injection)
* [39. SOLID Principles](#39-solid-principles)
* [40. Advanced Coding Problems](#40-advanced-coding-problems)

---

# 🧠 Core Python Internals

## 1. What is Python's GIL?

**GIL** stands for **Global Interpreter Lock**.

In traditional CPython implementations, the GIL ensures that only one thread executes Python bytecode at a time within a process.

### Example

```python
import threading

def task():
    for _ in range(1000000):
        pass

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()
```

### Interview Point

The GIL does **not** mean Python cannot perform concurrent work.

Threads can still be useful for:

* 🌐 Network operations
* 📁 File I/O
* 🗄️ Database operations
* ⏳ Waiting operations

For CPU-heavy workloads, multiprocessing or suitable native/parallel libraries may be more appropriate.

---

## 2. What is Garbage Collection?

Python automatically manages memory.

It primarily uses:

1. **Reference counting**
2. **Cyclic garbage collection**

### Example

```python
class Node:
    pass

a = Node()
b = Node()

a.other = b
b.other = a

del a
del b
```

The objects can form a reference cycle, which cyclic garbage collection can detect and reclaim.

### Useful Module

```python
import gc

print(gc.get_count())
```

---

## 3. What is Reference Counting?

Reference counting tracks how many references point to an object.

```python
import sys

value = []

print(sys.getrefcount(value))
```

When an object's reference count reaches zero, CPython can generally reclaim its memory immediately.

### Important

Reference counting alone cannot handle cycles such as:

```text
A → B
↑   ↓
└───┘
```

Python's cyclic garbage collector handles such cases.

---

# 🏗️ Advanced Object-Oriented Python

## 4. What is `__slots__`?

`__slots__` allows a class to explicitly define its allowed instance attributes.

### Example

```python
class Student:
    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Now:

```python
student = Student("Kishor", 21)

print(student.name)
```

### Benefits

* Can reduce per-instance memory overhead.
* Prevents arbitrary new instance attributes.
* Can be useful when creating many objects.

### Limitation

```python
student.city = "Pune"
```

This may fail because `city` is not defined in `__slots__`.

---

## 5. What is `@property`?

`@property` allows a method to be accessed like an attribute.

### Example

```python
class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if value < 0:
            raise ValueError("Marks cannot be negative")
        self._marks = value


student = Student(80)

print(student.marks)

student.marks = 90
print(student.marks)
```

### Output

```text
80
90
```

### Why use it?

It provides controlled access to object attributes without changing the public interface.

---

## 6. Static Method vs Class Method

### Static Method

Does not automatically receive the instance or class.

```python
class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(10, 20))
```

### Class Method

Receives the class as `cls`.

```python
class Student:

    school = "ABC School"

    @classmethod
    def change_school(cls, name):
        cls.school = name


Student.change_school("XYZ School")

print(Student.school)
```

### Comparison

| Feature            | Static Method      | Class Method                         |
| ------------------ | ------------------ | ------------------------------------ |
| Decorator          | `@staticmethod`    | `@classmethod`                       |
| First argument     | None automatically | `cls`                                |
| Access class state | Not automatic      | Yes                                  |
| Common use         | Utility methods    | Alternative constructors/class state |

---

## 7. What are Abstract Base Classes?

Abstract Base Classes define a common interface that subclasses should implement.

Python provides the `abc` module.

### Example

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        return "Bark"


dog = Dog()

print(dog.sound())
```

### Output

```text
Bark
```

An abstract class containing abstract methods generally cannot be instantiated until those methods are implemented.

---

## 8. What is a Metaclass?

A **metaclass** is a class whose instances are classes.

A common default metaclass in Python is `type`.

```python
class Student:
    pass

print(type(Student))
```

### Output

```text
<class 'type'>
```

You can define a custom metaclass:

```python
class Meta(type):
    def __new__(cls, name, bases, namespace):
        print(f"Creating {name}")
        return super().__new__(cls, name, bases, namespace)


class Student(metaclass=Meta):
    pass
```

Metaclasses are powerful but should generally be used only when simpler mechanisms are insufficient.

---

## 9. What are Descriptors?

A descriptor is an object that defines one or more of:

```python
__get__()
__set__()
__delete__()
```

### Example

```python
class PositiveNumber:

    def __get__(self, instance, owner):
        return instance._value

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value must be positive")
        instance._value = value


class Product:
    price = PositiveNumber()

    def __init__(self, price):
        self.price = price


product = Product(100)

print(product.price)
```

Descriptors are heavily used by Python frameworks and features such as properties.

---

## 10. What is the difference between `__new__()` and `__init__()`?

### `__new__()`

Creates the object.

### `__init__()`

Initializes the object after creation.

```python
class Student:

    def __new__(cls, name):
        print("Creating object")
        return super().__new__(cls)

    def __init__(self, name):
        print("Initializing object")
        self.name = name


student = Student("Kishor")
```

### Output

```text
Creating object
Initializing object
```

### Interview Rule

```text
__new__() → creates
__init__() → initializes
```

---

# 🔄 Advanced Inheritance

## 11. What is Method Resolution Order?

**MRO** determines the order in which Python searches classes for methods and attributes.

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(C.mro())
```

### Output

```text
[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
```

Python uses the **C3 linearization** algorithm to determine MRO.

---

## 12. What is Monkey Patching?

Monkey patching means changing or replacing behavior at runtime.

```python
class Student:

    def greet(self):
        return "Hello"


def new_greet(self):
    return "Welcome"


Student.greet = new_greet

student = Student()

print(student.greet())
```

### Output

```text
Welcome
```

It can be useful in testing or controlled environments, but excessive use can make code difficult to understand and maintain.

---

# 🧩 Functional Programming

## 13. What are First-Class Functions?

In Python, functions are objects.

They can be:

* Stored in variables
* Passed as arguments
* Returned from functions
* Stored in collections

### Example

```python
def greet():
    return "Hello"


message = greet

print(message())
```

### Output

```text
Hello
```

---

## 14. What is a Higher-Order Function?

A higher-order function accepts another function as an argument or returns a function.

```python
def calculate(operation, a, b):
    return operation(a, b)


def add(x, y):
    return x + y


print(calculate(add, 10, 20))
```

### Output

```text
30
```

---

## 15. What is a Closure?

A closure is an inner function that remembers values from its enclosing scope even after the outer function has finished.

```python
def multiplier(x):

    def multiply(y):
        return x * y

    return multiply


double = multiplier(2)

print(double(5))
```

### Output

```text
10
```

Here, `multiply()` remembers `x`.

---

# 🎯 Decorators

## 16. What are Advanced Decorators?

A decorator modifies or extends the behavior of another function.

### Example

```python
from functools import wraps

def logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print("Finished")
        return result

    return wrapper


@logger
def add(a, b):
    return a + b


print(add(10, 20))
```

### Output

```text
Calling add
Finished
30
```

`functools.wraps()` preserves metadata such as the original function's name and documentation.

---

# ⚡ Generators and Iterators

## 17. What is a Generator Expression?

A generator expression creates values lazily.

```python
numbers = (x * x for x in range(5))

print(next(numbers))
print(next(numbers))
```

### Output

```text
0
1
```

Unlike a list comprehension, values are generated when requested.

---

## 18. What is `yield from`?

`yield from` delegates iteration to another iterable or generator.

```python
def numbers():
    yield from [1, 2, 3]


for number in numbers():
    print(number)
```

### Output

```text
1
2
3
```

It is particularly useful when composing generators.

---

## 19. Iterator vs Generator

| Feature    | Iterator                    | Generator                     |
| ---------- | --------------------------- | ----------------------------- |
| Protocol   | `__iter__()` + `__next__()` | Usually created with `yield`  |
| State      | Maintains iteration state   | Automatically maintains state |
| Memory     | Depends on implementation   | Usually memory efficient      |
| Complexity | Can require more code       | Often simpler                 |

### Iterator

```python
numbers = iter([1, 2, 3])

print(next(numbers))
```

### Generator

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

---

# 🔐 Context Managers

## 20. What is a Context Manager?

A context manager manages setup and cleanup operations.

The `with` statement is commonly used with context managers.

```python
with open("data.txt", "r") as file:
    content = file.read()
```

The file is automatically closed after leaving the block.

### Custom Context Manager

```python
class Database:

    def __enter__(self):
        print("Connection opened")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Connection closed")


with Database():
    print("Working")
```

### Output

```text
Connection opened
Working
Connection closed
```

---

# ⚡ Asynchronous Programming

## 21. What is Async Programming?

Asynchronous programming allows a program to perform other work while waiting for an operation to complete.

It is particularly useful for I/O-bound tasks.

Common applications include:

* 🌐 HTTP requests
* 🗄️ Database operations
* 📡 Network services
* 🔌 APIs
* 💬 WebSockets

---

## 22. What are `async` and `await`?

`async` defines a coroutine.

`await` pauses the coroutine until an awaitable operation completes.

```python
import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


asyncio.run(greet())
```

### Output

```text
Hello
World
```

### Important

`asyncio` is designed primarily around asynchronous I/O and cooperative concurrency.

---

# 🧵 Concurrency and Parallelism

## 23. Threading vs Multiprocessing

| Feature            | Threading             | Multiprocessing                      |
| ------------------ | --------------------- | ------------------------------------ |
| Execution unit     | Thread                | Process                              |
| Memory             | Shared within process | Separate process memory              |
| Best for           | I/O-bound work        | CPU-bound work                       |
| GIL considerations | Relevant in CPython   | Each process has its own interpreter |
| Communication      | Easier shared memory  | Requires IPC/mechanisms              |

### Threading

```python
import threading

def task():
    print("Running")


thread = threading.Thread(target=task)
thread.start()
thread.join()
```

### Multiprocessing

```python
from multiprocessing import Process

def task():
    print("Running")


process = Process(target=task)
process.start()
process.join()
```

---

## 24. What is `concurrent.futures`?

`concurrent.futures` provides high-level APIs for asynchronous execution.

It provides:

* `ThreadPoolExecutor`
* `ProcessPoolExecutor`

### Example

```python
from concurrent.futures import ThreadPoolExecutor

def square(n):
    return n * n


with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(square, [1, 2, 3, 4])

    print(list(results))
```

### Output

```text
[1, 4, 9, 16]
```

---

# 📦 Serialization

## 25. What is Pickling?

Pickling converts Python objects into a byte stream that can later be reconstructed.

```python
import pickle

data = {
    "name": "Kishor",
    "age": 21
}

with open("data.pkl", "wb") as file:
    pickle.dump(data, file)
```

To load:

```python
with open("data.pkl", "rb") as file:
    data = pickle.load(file)

print(data)
```

### ⚠️ Security Note

Never unpickle untrusted data. Pickle is not designed as a secure interchange format.

---

## 26. Serialization vs Deserialization

### Serialization

Object → storable/transmittable representation

```text
Python Object → JSON
```

### Deserialization

Stored/transmitted representation → object

```text
JSON → Python Object
```

### Example

```python
import json

data = {
    "name": "Kishor",
    "age": 21
}

text = json.dumps(data)

print(text)
```

---

# 📝 Type Hints and Modern Python

## 27. What are Type Hints?

Type hints communicate expected types.

```python
def add(a: int, b: int) -> int:
    return a + b
```

Type hints improve:

* 📖 Readability
* 🛠️ IDE support
* 🔍 Static analysis
* 🧹 Maintainability

Python generally does not enforce these annotations at runtime by itself.

---

## 28. What are Dataclasses?

`dataclasses` simplifies classes primarily used to store data.

```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int


student = Student("Kishor", 21)

print(student)
```

### Output

```text
Student(name='Kishor', age=21)
```

A dataclass can automatically provide methods such as:

* `__init__`
* `__repr__`
* `__eq__`

depending on configuration.

---

## 29. What is Structural Pattern Matching?

Python provides `match` and `case` for structural pattern matching.

```python
def check(value):

    match value:
        case 0:
            return "Zero"
        case int():
            return "Integer"
        case str():
            return "String"
        case _:
            return "Other"


print(check(10))
```

### Output

```text
Integer
```

Pattern matching can be useful when handling structured data and multiple cases.

---

## 30. What is the Walrus Operator?

The `:=` operator assigns a value as part of an expression.

### Example

```python
if (length := len("Python")) > 5:
    print(length)
```

### Output

```text
6
```

Use it when it improves clarity rather than simply shortening code.

---

# 🚀 Performance and Optimization

## 31. What is Memoization?

Memoization stores previously calculated results so repeated calls can reuse them.

### Example

```python
cache = {}

def square(n):

    if n not in cache:
        cache[n] = n * n

    return cache[n]


print(square(10))
print(square(10))
```

The second call can reuse the stored result.

---

## 32. What is `lru_cache`?

`functools.lru_cache` provides built-in memoization.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):

    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
```

### Output

```text
55
```

You can inspect cache statistics:

```python
print(fibonacci.cache_info())
```

---

## 33. How do you optimize Python code?

Common techniques include:

### 1. Choose appropriate data structures

```python
# Fast membership testing in many cases
items = {1, 2, 3, 4}

print(3 in items)
```

### 2. Avoid unnecessary work

### 3. Use generators for large streams

```python
numbers = (x * x for x in range(1000000))
```

### 4. Use built-in operations

Python's built-ins are often implemented efficiently.

### 5. Profile before optimizing

Do not optimize based only on assumptions.

---

## 34. What is Memory Profiling?

Memory profiling helps identify where a program consumes memory.

A simple built-in option is:

```python
import tracemalloc

tracemalloc.start()

data = [x for x in range(100000)]

current, peak = tracemalloc.get_traced_memory()

print("Current:", current)
print("Peak:", peak)

tracemalloc.stop()
```

Memory profiling can help identify inefficient allocations and memory-heavy operations.

---

## 35. What is Python Interning?

Python may reuse certain immutable objects instead of creating separate objects every time.

For example, implementations commonly intern some strings and small integers.

```python
a = 10
b = 10

print(a is b)
```

Possible output:

```text
True
```

### Important

Do **not** rely on interning behavior for normal equality checks.

Use:

```python
a == b
```

for value comparison.

---

# ⚠️ Advanced Python Pitfalls

## 36. What is the Mutable Default Argument Problem?

Consider:

```python
def add_item(item, items=[]):
    items.append(item)
    return items


print(add_item("A"))
print(add_item("B"))
```

The same default list is reused between calls.

### Better Approach

```python
def add_item(item, items=None):

    if items is None:
        items = []

    items.append(item)

    return items
```

This creates a new list when no list is provided.

---

## 37. What is the difference between `is` and `==`?

### `==`

Checks whether values are equal.

### `is`

Checks whether two references point to the same object.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

### Output

```text
True
False
```

### Rule

Use:

```python
==
```

for value equality.

Use:

```python
is
```

for object identity, commonly:

```python
if value is None:
    ...
```

---

# 🧱 Software Design

## 38. What is Dependency Injection?

Dependency Injection means providing an object's dependencies from outside rather than creating them internally.

### Without Dependency Injection

```python
class Service:

    def __init__(self):
        self.database = Database()
```

### With Dependency Injection

```python
class Service:

    def __init__(self, database):
        self.database = database
```

Now:

```python
database = Database()
service = Service(database)
```

### Benefits

* 🧪 Easier testing
* 🔄 Flexible implementations
* 🧩 Lower coupling
* 🛠️ Better maintainability

---

## 39. What are SOLID Principles?

SOLID is a set of object-oriented design principles.

### S — Single Responsibility Principle

A class should have one primary responsibility.

### O — Open/Closed Principle

Software entities should generally be open for extension but closed for modification.

### L — Liskov Substitution Principle

Subtypes should be usable wherever their base types are expected without breaking correctness.

### I — Interface Segregation Principle

Clients should not be forced to depend on interfaces they do not use.

### D — Dependency Inversion Principle

High-level modules should depend on abstractions rather than concrete implementations.

---

# 💻 40. Advanced Coding Problems

## Problem 1: Implement a Custom Iterator

```python
class Counter:

    def __init__(self, limit):
        self.current = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):

        if self.current >= self.limit:
            raise StopIteration

        self.current += 1
        return self.current


counter = Counter(3)

for number in counter:
    print(number)
```

### Output

```text
1
2
3
```

---

## Problem 2: Implement a Generator

```python
def even_numbers(limit):

    for number in range(limit + 1):

        if number % 2 == 0:
            yield number


for number in even_numbers(10):
    print(number)
```

### Output

```text
0
2
4
6
8
10
```

---

## Problem 3: Create a Timing Decorator

```python
import time
from functools import wraps

def timer(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()

        print(f"Execution time: {end - start:.6f} seconds")

        return result

    return wrapper


@timer
def calculate():
    return sum(range(100000))


print(calculate())
```

---

## Problem 4: Implement a Singleton

A simple singleton-style implementation can be created using `__new__()`:

```python
class Singleton:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance


a = Singleton()
b = Singleton()

print(a is b)
```

### Output

```text
True
```

---

## Problem 5: Find Duplicate Values

```python
numbers = [1, 2, 3, 2, 4, 5, 3]

seen = set()
duplicates = set()

for number in numbers:

    if number in seen:
        duplicates.add(number)
    else:
        seen.add(number)

print(duplicates)
```

### Output

```text
{2, 3}
```

---

## Problem 6: Find the First Non-Repeating Character

```python
from collections import Counter

text = "swiss"

counts = Counter(text)

for char in text:

    if counts[char] == 1:
        print(char)
        break
```

### Output

```text
w
```

---

## Problem 7: Implement a Simple LRU Cache

```python
from functools import lru_cache

@lru_cache(maxsize=3)
def square(number):
    return number * number


print(square(2))
print(square(3))
print(square(4))

print(square.cache_info())
```

This tests your understanding of caching and decorators.

---

## Problem 8: Flatten a Nested List

```python
def flatten(items):

    result = []

    for item in items:

        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result


data = [1, [2, [3, 4]], 5]

print(flatten(data))
```

### Output

```text
[1, 2, 3, 4, 5]
```

---

## Problem 9: Find the Missing Number

Given:

```python
numbers = [1, 2, 3, 5, 6]
```

Find the missing number.

```python
numbers = [1, 2, 3, 5, 6]

n = len(numbers) + 1

expected = n * (n + 1) // 2

actual = sum(numbers)

print(expected - actual)
```

### Output

```text
4
```

---

## Problem 10: Implement a Retry Decorator

```python
from functools import wraps

def retry(attempts):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            for attempt in range(attempts):

                try:
                    return func(*args, **kwargs)

                except Exception:

                    if attempt == attempts - 1:
                        raise

        return wrapper

    return decorator


@retry(3)
def operation():
    return "Success"


print(operation())
```

---

# 📊 Advanced Python Comparison Table

| Concept         | Key Idea                          |
| --------------- | --------------------------------- |
| `__new__()`     | Creates an object                 |
| `__init__()`    | Initializes an object             |
| `__str__()`     | User-friendly representation      |
| `__repr__()`    | Developer-oriented representation |
| Iterator        | Implements iteration protocol     |
| Generator       | Produces values lazily            |
| Decorator       | Extends function/class behavior   |
| Closure         | Remembers enclosing scope         |
| Descriptor      | Controls attribute access         |
| Metaclass       | Controls class creation           |
| Context Manager | Handles setup and cleanup         |
| Threading       | Concurrent threads                |
| Multiprocessing | Separate processes                |
| `asyncio`       | Asynchronous programming          |
| Pickle          | Python object serialization       |
| Dataclass       | Simplifies data-oriented classes  |
| `lru_cache`     | Memoization cache                 |
| `__slots__`     | Restricts instance attributes     |

---

# 🧠 Advanced Interview Tips

### 1. Understand the "Why"

Do not only memorize definitions.

Understand:

```text
What?
Why?
How?
When?
Trade-offs?
```

---

### 2. Explain With Examples

For example:

> A generator produces values lazily using `yield`, which can reduce memory usage when processing large sequences.

Then demonstrate it with code.

---

### 3. Know Python Internals

For advanced interviews, understand concepts such as:

* 🧠 Object model
* 🔢 Reference counting
* ♻️ Garbage collection
* 🔐 GIL
* 🧩 Descriptors
* 🏗️ Metaclasses
* 🔄 MRO
* 💾 Memory management

---

### 4. Understand Complexity

Know common Big-O complexities:

| Operation                   | Typical Complexity |
| --------------------------- | -----------------: |
| List indexing               |             `O(1)` |
| List search                 |             `O(n)` |
| Dictionary lookup           |     `O(1)` average |
| Set lookup                  |     `O(1)` average |
| Sorting                     |       `O(n log n)` |
| List append                 |   `O(1)` amortized |
| List insertion at beginning |             `O(n)` |

Actual performance can depend on implementation and workload.

---

# 🧪 Advanced Interview Checklist

Before an advanced Python interview, make sure you can explain:

* [ ] GIL
* [ ] Reference counting
* [ ] Garbage collection
* [ ] `__slots__`
* [ ] Properties
* [ ] Static methods
* [ ] Class methods
* [ ] Abstract classes
* [ ] Metaclasses
* [ ] Descriptors
* [ ] `__new__()` and `__init__()`
* [ ] MRO
* [ ] Closures
* [ ] Decorators
* [ ] Generators
* [ ] Iterators
* [ ] Context managers
* [ ] Async programming
* [ ] Threading
* [ ] Multiprocessing
* [ ] `concurrent.futures`
* [ ] Serialization
* [ ] Type hints
* [ ] Dataclasses
* [ ] Pattern matching
* [ ] Memoization
* [ ] Caching
* [ ] Memory profiling
* [ ] Mutable default arguments
* [ ] Identity vs equality
* [ ] Dependency injection
* [ ] SOLID principles
* [ ] Advanced coding problems

---

# 🗺️ Advanced Interview Preparation Path

```text
🐍 Python Basics
      ↓
📦 Data Structures
      ↓
🧩 Functions & OOP
      ↓
🔄 Iterators & Generators
      ↓
🎯 Decorators & Closures
      ↓
🧠 Python Internals
      ↓
⚡ Concurrency & Async
      ↓
🏗️ Advanced OOP
      ↓
🚀 Performance Optimization
      ↓
💻 Coding Problems
      ↓
🎯 Mock Interviews
```

---

# 📚 Recommended Repository Navigation

### 🟢 Beginner

[`beginner.md`](./beginner.md)

Learn Python fundamentals and common entry-level interview questions.

### 🟡 Intermediate

[`intermediate.md`](./intermediate.md)

Practice OOP, generators, decorators, exceptions, modules, and intermediate coding problems.

### 🔴 Advanced

**You are here — `advanced.md`**

Master Python internals, concurrency, asynchronous programming, metaprogramming, optimization, and advanced coding problems.

### 📖 Main Interview Guide

[`README.md`](./README.md)

Complete Python interview preparation roadmap.

---

# 🚀 Final Reminder

> **Don't just memorize Python interview answers — understand how Python works.**

```text
📚 Learn
   ↓
🧪 Practice
   ↓
💻 Code
   ↓
🔍 Debug
   ↓
🧠 Understand
   ↓
🎯 Interview
```

### 🌱 Keep Learning. Keep Building. Keep Growing. 🚀

**Python → Practice → Projects → Problem Solving → Interviews → Growth**
