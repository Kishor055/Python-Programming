# 🐍 Advanced Python

> **Master Python beyond the basics — advanced language features, powerful programming techniques, performance, concurrency, metaprogramming, and production-ready patterns.**

Welcome to **Advanced Python** 🚀

This section builds on the core Python concepts covered in the previous chapters and explores the features that make Python powerful for **professional software development, automation, backend engineering, data engineering, AI/ML, scripting, and system design**.

The goal is not simply to learn more syntax, but to understand **how Python works internally**, how to write expressive and maintainable code, and when advanced features should actually be used.

---

## 📚 Table of Contents

* [🎯 Learning Objectives](#-learning-objectives)
* [🧠 What Is Advanced Python?](#-what-is-advanced-python)
* [1. Iterators](#1-iterators)
* [2. Generators](#2-generators)
* [3. Generator Expressions](#3-generator-expressions)
* [4. Decorators](#4-decorators)
* [5. Closures](#5-closures)
* [6. Higher-Order Functions](#6-higher-order-functions)
* [7. Lambda Functions](#7-lambda-functions)
* [8. `*args` and `**kwargs`](#8-args-and-kwargs)
* [9. Context Managers](#9-context-managers)
* [10. `with` Statement](#10-with-statement)
* [11. Custom Context Managers](#11-custom-context-managers)
* [12. Comprehensions](#12-comprehensions)
* [13. Advanced Unpacking](#13-advanced-unpacking)
* [14. `map()`, `filter()`, and `reduce()`](#14-map-filter-and-reduce)
* [15. Functional Programming](#15-functional-programming)
* [16. `functools`](#16-functools)
* [17. `itertools`](#17-itertools)
* [18. `collections`](#18-collections)
* [19. Type Hints](#19-type-hints)
* [20. Dataclasses](#20-dataclasses)
* [21. Enums](#21-enums)
* [22. Properties and Descriptors](#22-properties-and-descriptors)
* [23. Dunder Methods](#23-dunder-methods)
* [24. Object Model and Attribute Lookup](#24-object-model-and-attribute-lookup)
* [25. Method Resolution Order](#25-method-resolution-order)
* [26. Multiple Inheritance](#26-multiple-inheritance)
* [27. Abstract Base Classes](#27-abstract-base-classes)
* [28. Protocols](#28-protocols)
* [29. Metaclasses](#29-metaclasses)
* [30. Monkey Patching](#30-monkey-patching)
* [31. Dynamic Attributes](#31-dynamic-attributes)
* [32. Reflection and Introspection](#32-reflection-and-introspection)
* [33. Shallow vs Deep Copy](#33-shallow-vs-deep-copy)
* [34. Memory Management](#34-memory-management)
* [35. Garbage Collection](#35-garbage-collection)
* [36. Performance Optimization](#36-performance-optimization)
* [37. Caching](#37-caching)
* [38. Concurrency](#38-concurrency)
* [39. Multithreading](#39-multithreading)
* [40. Multiprocessing](#40-multiprocessing)
* [41. Asynchronous Programming](#41-asynchronous-programming)
* [42. `async` and `await`](#42-async-and-await)
* [43. Async Context Managers](#43-async-context-managers)
* [44. Async Iterators and Generators](#44-async-iterators-and-generators)
* [45. Thread Safety](#45-thread-safety)
* [46. Locks and Synchronization](#46-locks-and-synchronization)
* [47. Serialization](#47-serialization)
* [48. Pickle](#48-pickle)
* [49. Abstract Syntax Trees](#49-abstract-syntax-trees)
* [50. Advanced Project Structure](#50-advanced-project-structure)
* [51. Design Patterns](#51-design-patterns)
* [52. Advanced Python Best Practices](#52-advanced-python-best-practices)
* [🧪 Practice Exercises](#-practice-exercises)
* [🚀 Advanced Projects](#-advanced-projects)
* [💼 Interview Questions](#-interview-questions)
* [⚡ Quick Revision](#-quick-revision)
* [🧭 Advanced Python Roadmap](#-advanced-python-roadmap)
* [📖 References](#-references)
* [➡️ Next Topic](#️-next-topic)

---

# 🎯 Learning Objectives

After completing this topic, you should be able to:

* Understand Python's iterator and generator protocols.
* Create and use decorators.
* Understand closures and higher-order functions.
* Use context managers correctly.
* Write efficient comprehensions.
* Use `functools`, `itertools`, and `collections`.
* Apply advanced type hints.
* Work with dataclasses and enums.
* Understand Python's object model.
* Implement custom dunder methods.
* Understand MRO and multiple inheritance.
* Use abstract classes and protocols.
* Understand descriptors and metaclasses.
* Perform introspection and reflection.
* Understand Python memory management.
* Optimize slow Python code.
* Use caching effectively.
* Understand threads, processes, and asynchronous programming.
* Build thread-safe applications.
* Work with serialization techniques.
* Understand advanced project architecture.
* Apply common design patterns appropriately.
* Write production-quality Python code.

---

# 🧠 What Is Advanced Python?

Advanced Python is not a separate programming language.

It refers to using Python's more powerful features to solve complex problems elegantly and efficiently.

A beginner might write:

```python
numbers = []

for number in range(10):
    if number % 2 == 0:
        numbers.append(number)
```

An experienced Python developer may write:

```python
numbers = [number for number in range(10) if number % 2 == 0]
```

But advanced Python goes much further.

For example:

```python
def timer(func):
    def wrapper(*args, **kwargs):
        print("Starting...")
        result = func(*args, **kwargs)
        print("Finished...")
        return result

    return wrapper
```

This introduces concepts such as:

* Higher-order functions
* Closures
* Decorators
* `*args`
* `**kwargs`
* Function objects

Advanced Python is primarily about understanding **why these features work and when to use them**.

---

# 1. Iterators

An **iterator** is an object that produces values one at a time.

Python uses two important methods:

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

After the final value:

```python
next(numbers)
```

raises:

```text
StopIteration
```

### Iterator Protocol

An iterator generally implements:

```python
__iter__()
__next__()
```

Example:

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
```

Usage:

```python
for number in Counter(5):
    print(number)
```

---

# 2. Generators

Generators provide a convenient way to create iterators.

They use:

```python
yield
```

Example:

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

Usage:

```python
for number in numbers():
    print(number)
```

Output:

```text
1
2
3
```

### Why Generators?

Generators are useful because they produce values lazily.

Instead of creating:

```python
numbers = [1, 2, 3, 4, 5, ...]
```

all at once, a generator produces one value at a time.

This can reduce memory usage when working with large data streams.

---

# 3. Generator Expressions

Generator expression:

```python
numbers = (x * 2 for x in range(10))
```

Compare:

```python
numbers = [x * 2 for x in range(10)]
```

The list comprehension creates the entire list.

The generator expression produces values lazily.

---

# 4. Decorators

A decorator modifies or extends the behavior of a function without changing its source code.

Example:

```python
def logger(func):
    def wrapper():
        print("Function started")
        func()
        print("Function finished")

    return wrapper
```

Using:

```python
@logger
def greet():
    print("Hello")
```

The following:

```python
@logger
def greet():
    print("Hello")
```

is conceptually similar to:

```python
greet = logger(greet)
```

### Practical Uses

Decorators are commonly used for:

* Logging
* Authentication
* Authorization
* Timing
* Caching
* Validation
* Retry mechanisms
* Transactions
* Web frameworks

---

# 5. Closures

A closure occurs when an inner function remembers values from its enclosing scope.

Example:

```python
def multiplier(factor):

    def multiply(number):
        return number * factor

    return multiply
```

Usage:

```python
double = multiplier(2)

print(double(10))
```

Output:

```text
20
```

The function `multiply()` remembers `factor`.

---

# 6. Higher-Order Functions

A higher-order function can:

* Accept another function as an argument.
* Return a function.

Example:

```python
def apply_operation(func, value):
    return func(value)

result = apply_operation(lambda x: x * 2, 10)

print(result)
```

Output:

```text
20
```

---

# 7. Lambda Functions

A lambda is a small anonymous function.

```python
square = lambda x: x * x

print(square(5))
```

Equivalent normal function:

```python
def square(x):
    return x * x
```

### Good Use

```python
students = [
    ("Alice", 90),
    ("Bob", 75),
    ("Charlie", 85)
]

students.sort(key=lambda student: student[1])
```

Avoid overly complex lambda expressions.

---

# 8. `*args` and `**kwargs`

## `*args`

Allows multiple positional arguments.

```python
def total(*args):
    return sum(args)

print(total(1, 2, 3, 4))
```

## `**kwargs`

Allows multiple keyword arguments.

```python
def display(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
```

Usage:

```python
display(name="Alice", age=25)
```

### Combined

```python
def function(*args, **kwargs):
    print(args)
    print(kwargs)
```

These are especially useful when building reusable APIs and decorators.

---

# 9. Context Managers

Context managers manage resources safely.

Common examples:

```python
with open("data.txt") as file:
    content = file.read()
```

The resource is automatically cleaned up.

Typical use cases:

* Files
* Database connections
* Locks
* Network resources
* Transactions

---

# 10. `with` Statement

The `with` statement works with context managers.

Conceptually, context managers implement:

```python
__enter__()
__exit__()
```

Example:

```python
class Demo:

    def __enter__(self):
        print("Entering")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")
```

Usage:

```python
with Demo():
    print("Inside")
```

---

# 11. Custom Context Managers

Python also provides:

```python
contextlib
```

Example:

```python
from contextlib import contextmanager

@contextmanager
def resource():
    print("Acquire")

    try:
        yield
    finally:
        print("Release")
```

Usage:

```python
with resource():
    print("Working")
```

The `finally` block ensures cleanup.

---

# 12. Comprehensions

Python provides several comprehension types.

### List

```python
squares = [x * x for x in range(10)]
```

### Set

```python
unique = {x % 3 for x in range(10)}
```

### Dictionary

```python
mapping = {x: x * x for x in range(5)}
```

### Nested comprehension

```python
matrix = [
    [1, 2],
    [3, 4]
]

flattened = [value for row in matrix for value in row]
```

Use comprehensions when they improve readability.

---

# 13. Advanced Unpacking

Python supports powerful unpacking.

```python
numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers

print(first)
print(middle)
print(last)
```

Output:

```text
1
[2, 3, 4]
5
```

Dictionary unpacking:

```python
first = {"name": "Alice"}
second = {"age": 25}

combined = {**first, **second}
```

---

# 14. `map()`, `filter()`, and `reduce()`

### `map()`

```python
numbers = [1, 2, 3]

result = map(lambda x: x * 2, numbers)

print(list(result))
```

### `filter()`

```python
numbers = [1, 2, 3, 4]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))
```

### `reduce()`

```python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, numbers)

print(result)
```

---

# 15. Functional Programming

Python supports several functional programming concepts:

* First-class functions
* Higher-order functions
* Closures
* Lambda expressions
* Immutability concepts
* Iterators
* Generators
* `map`
* `filter`
* `reduce`

Functional programming can be useful for data transformation and composable operations.

However, Python is **multi-paradigm**, so object-oriented and procedural approaches remain important.

---

# 16. `functools`

The `functools` module provides tools for functional programming.

Important utilities include:

```python
partial
reduce
lru_cache
cache
wraps
singledispatch
```

### `partial()`

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)

print(square(5))
```

### `wraps()`

When creating decorators:

```python
from functools import wraps

def decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
```

`wraps()` helps preserve metadata such as the original function's name and documentation.

---

# 17. `itertools`

`itertools` provides efficient iterator building blocks.

Useful functions include:

```python
count()
cycle()
repeat()
chain()
islice()
product()
permutations()
combinations()
groupby()
```

Example:

```python
from itertools import chain

result = chain([1, 2], [3, 4])

print(list(result))
```

Output:

```text
[1, 2, 3, 4]
```

---

# 18. `collections`

The `collections` module provides specialized containers.

Important classes include:

```python
Counter
defaultdict
deque
namedtuple
ChainMap
```

### Counter

```python
from collections import Counter

letters = Counter("banana")

print(letters)
```

### defaultdict

```python
from collections import defaultdict

groups = defaultdict(list)

groups["Python"].append("Alice")
groups["Python"].append("Bob")
```

### deque

```python
from collections import deque

queue = deque()

queue.append("A")
queue.append("B")

print(queue.popleft())
```

---

# 19. Type Hints

Type hints improve readability, tooling, and maintainability.

```python
def add(a: int, b: int) -> int:
    return a + b
```

Collections:

```python
def total(numbers: list[int]) -> int:
    return sum(numbers)
```

Optional values:

```python
def find_user(user_id: int) -> str | None:
    ...
```

Type hints are primarily used by tools such as type checkers and IDEs; Python does not generally enforce them at runtime.

---

# 20. Dataclasses

Dataclasses simplify classes that primarily store data.

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
```

Usage:

```python
user = User("Alice", 25)

print(user)
```

Dataclasses can automatically provide useful methods such as:

* `__init__`
* `__repr__`
* `__eq__`

depending on configuration.

---

# 21. Enums

Enums represent a fixed collection of named values.

```python
from enum import Enum

class Status(Enum):
    PENDING = 1
    ACTIVE = 2
    COMPLETED = 3
```

Usage:

```python
status = Status.ACTIVE

print(status)
```

Enums are useful for:

* Status values
* Configuration states
* Application modes
* Command types

---

# 22. Properties and Descriptors

Properties allow controlled access to attributes.

```python
class User:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")

        self._age = value
```

Usage:

```python
user = User(25)

print(user.age)

user.age = 30
```

Descriptors provide an even more powerful attribute-management mechanism.

They commonly implement:

```python
__get__()
__set__()
__delete__()
```

---

# 23. Dunder Methods

Dunder means **double underscore**.

Examples:

```python
__init__
__str__
__repr__
__len__
__iter__
__next__
__eq__
__lt__
__add__
__enter__
__exit__
```

Example:

```python
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ₹{self.price}"
```

Now:

```python
product = Product("Laptop", 50000)

print(product)
```

---

# 24. Object Model and Attribute Lookup

Python objects have attributes that Python resolves through a defined lookup process.

Understanding attribute lookup helps explain:

* Instance attributes
* Class attributes
* Inheritance
* Properties
* Descriptors
* Method lookup
* MRO

Example:

```python
class Parent:
    value = "parent"

class Child(Parent):
    pass

obj = Child()

print(obj.value)
```

Python searches appropriate namespaces and the class hierarchy to locate the attribute.

---

# 25. Method Resolution Order

MRO determines the order in which Python searches classes for methods and attributes.

Example:

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(C.mro())
```

MRO becomes particularly important with multiple inheritance.

---

# 26. Multiple Inheritance

A class can inherit from multiple classes.

```python
class A:
    def feature_a(self):
        print("A")

class B:
    def feature_b(self):
        print("B")

class C(A, B):
    pass
```

Usage:

```python
obj = C()

obj.feature_a()
obj.feature_b()
```

Multiple inheritance should be used carefully because complex hierarchies can reduce maintainability.

---

# 27. Abstract Base Classes

The `abc` module allows developers to define abstract interfaces.

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass
```

Concrete classes must implement the required behavior.

```python
class Dog(Animal):

    def speak(self):
        return "Bark"
```

---

# 28. Protocols

Protocols support structural typing.

Conceptually:

> If an object provides the required behavior, it can satisfy the protocol.

Example:

```python
from typing import Protocol

class Drawable(Protocol):

    def draw(self) -> None:
        ...
```

A class does not necessarily need to explicitly inherit from the protocol to satisfy the structural interface for static type checking.

---

# 29. Metaclasses

A metaclass controls class creation.

The default metaclass is:

```python
type
```

For example:

```python
class User:
    pass

print(type(User))
```

Output:

```text
<class 'type'>
```

Metaclasses are advanced and should generally be used only when simpler mechanisms are insufficient.

Potential use cases include:

* Framework internals
* Automatic class registration
* API enforcement
* Class customization

---

# 30. Monkey Patching

Monkey patching means changing behavior at runtime.

Example:

```python
class Calculator:

    def add(self, a, b):
        return a + b
```

A method can technically be replaced dynamically.

Although powerful, monkey patching can make software difficult to understand and maintain.

Use it carefully, particularly in testing.

---

# 31. Dynamic Attributes

Python allows dynamic attribute manipulation.

```python
class User:
    pass

user = User()

setattr(user, "name", "Alice")

print(getattr(user, "name"))
```

Other useful functions:

```python
hasattr()
getattr()
setattr()
delattr()
```

---

# 32. Reflection and Introspection

Python provides powerful introspection capabilities.

Useful functions include:

```python
type()
id()
dir()
help()
vars()
isinstance()
issubclass()
callable()
```

Example:

```python
class User:
    name = "Alice"

user = User()

print(type(user))
print(dir(user))
print(vars(user))
```

The `inspect` module provides even more advanced introspection functionality.

---

# 33. Shallow vs Deep Copy

Consider:

```python
import copy

original = [[1, 2], [3, 4]]
```

### Shallow Copy

```python
shallow = copy.copy(original)
```

The outer object is copied, but nested objects can still be shared.

### Deep Copy

```python
deep = copy.deepcopy(original)
```

Nested objects are recursively copied.

Understanding object references is essential when working with mutable structures.

---

# 34. Memory Management

Python manages memory automatically.

Important concepts include:

* Object allocation
* References
* Reference counting
* Garbage collection
* Object lifetime
* Mutable vs immutable objects
* Interning in some implementation scenarios

Example:

```python
a = []
b = a
```

Both variables refer to the same list.

```python
b.append(10)

print(a)
```

Output:

```text
[10]
```

---

# 35. Garbage Collection

Python automatically manages unreachable objects.

The `gc` module can be used to interact with the garbage collector.

```python
import gc

print(gc.isenabled())
```

Most applications should rely on Python's normal memory management rather than manually controlling garbage collection.

---

# 36. Performance Optimization

Optimization should begin with measurement.

Useful tools include:

```text
timeit
cProfile
profile
tracemalloc
```

Example:

```python
import timeit

result = timeit.timeit(
    "sum(range(1000))",
    number=10000
)

print(result)
```

### Optimization principle

> Measure first. Optimize second.

Avoid optimizing code simply because it appears slow.

---

# 37. Caching

Caching avoids repeatedly performing expensive operations.

Example:

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
```

Caching is useful for:

* Expensive calculations
* Repeated database lookups
* API responses
* Recursive algorithms
* Configuration data

But caching introduces trade-offs involving:

* Memory
* Stale data
* Cache invalidation
* Key design

---

# 38. Concurrency

Concurrency allows multiple tasks to make progress during overlapping periods.

Python provides several approaches:

```text
threading
multiprocessing
asyncio
concurrent.futures
```

The correct choice depends on the workload.

---

# 39. Multithreading

Threads are useful for many I/O-bound workloads.

Example:

```python
import threading

def task():
    print("Running task")

thread = threading.Thread(target=task)

thread.start()
thread.join()
```

Typical I/O-bound workloads include:

* Network requests
* File operations
* Waiting for external services

---

# 40. Multiprocessing

Multiprocessing uses separate processes.

This can be useful for CPU-intensive workloads because processes have separate Python interpreter states.

Example:

```python
from multiprocessing import Process

def task():
    print("Running process")

process = Process(target=task)

process.start()
process.join()
```

---

# 41. Asynchronous Programming

Asynchronous programming is useful when programs spend significant time waiting for I/O.

Python provides:

```python
asyncio
```

The main concepts include:

* Coroutines
* Event loops
* Tasks
* Futures
* Awaitables

---

# 42. `async` and `await`

Example:

```python
import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(greet())
```

`await` allows an asynchronous operation to yield control while waiting.

---

# 43. Async Context Managers

Asynchronous context managers use:

```python
__aenter__()
__aexit__()
```

Example:

```python
class AsyncResource:

    async def __aenter__(self):
        print("Acquire")
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        print("Release")
```

Usage:

```python
async with AsyncResource():
    print("Working")
```

---

# 44. Async Iterators and Generators

Async iteration uses:

```python
__aiter__()
__anext__()
```

Async generators can use:

```python
async def numbers():
    for number in range(5):
        yield number
```

Consumption:

```python
async for number in numbers():
    print(number)
```

These concepts are useful for streaming asynchronous data.

---

# 45. Thread Safety

Thread-safe code behaves correctly when accessed by multiple threads.

Potential problems include:

* Race conditions
* Shared mutable state
* Deadlocks
* Lost updates

Example problem:

```python
counter += 1
```

When multiple threads modify shared state, synchronization may be required.

---

# 46. Locks and Synchronization

Python provides synchronization primitives such as:

```python
Lock
RLock
Semaphore
Event
Condition
Barrier
```

Example:

```python
import threading

lock = threading.Lock()

with lock:
    # protected operation
    pass
```

Keep critical sections small and avoid unnecessary shared state.

---

# 47. Serialization

Serialization converts data into a representation that can be stored or transmitted.

Common formats include:

```text
JSON
Pickle
CSV
XML
MessagePack
Protocol Buffers
```

JSON example:

```python
import json

data = {
    "name": "Alice",
    "age": 25
}

text = json.dumps(data)

print(text)
```

---

# 48. Pickle

Python's `pickle` module can serialize Python objects.

```python
import pickle

data = {"name": "Alice"}

with open("data.pkl", "wb") as file:
    pickle.dump(data, file)
```

### ⚠️ Security Warning

Never unpickle untrusted data.

Unpickling can execute arbitrary code depending on the serialized content.

For data exchanged between untrusted systems, prefer safer formats such as JSON where appropriate.

---

# 49. Abstract Syntax Trees

Python can represent Python source code as an Abstract Syntax Tree.

The `ast` module provides access to this structure.

Example:

```python
import ast

tree = ast.parse("x = 10")

print(ast.dump(tree, indent=2))
```

ASTs are useful for:

* Static analysis
* Code transformation
* Linters
* Code formatters
* Developer tools
* Source analysis

---

# 50. Advanced Project Structure

A professional Python project may look like:

```text
my_project/
│
├── src/
│   └── my_project/
│       ├── __init__.py
│       ├── main.py
│       ├── models/
│       ├── services/
│       ├── repositories/
│       ├── utils/
│       └── config/
│
├── tests/
│   ├── unit/
│   └── integration/
│
├── docs/
├── scripts/
├── pyproject.toml
├── README.md
└── .gitignore
```

Good architecture separates responsibilities.

For example:

```text
models       → data/domain structures
services     → business logic
repositories → persistence/data access
utils        → reusable utilities
tests        → automated tests
```

---

# 51. Design Patterns

Design patterns are reusable approaches to common software design problems.

Important patterns to study in Python include:

### Creational

* Factory
* Abstract Factory
* Builder
* Singleton

### Structural

* Adapter
* Decorator
* Facade
* Proxy

### Behavioral

* Strategy
* Observer
* Command
* Template Method

Python's flexibility means many traditional patterns can often be implemented more simply using functions, first-class objects, or language features.

---

# 52. Advanced Python Best Practices

## 1. Prefer readability

Readable:

```python
total = price * quantity
```

Over unnecessarily clever expressions.

---

## 2. Use meaningful names

Prefer:

```python
customer_count
```

instead of:

```python
cc
```

---

## 3. Avoid unnecessary abstraction

Not every small problem requires:

* A class hierarchy
* A metaclass
* A design pattern
* A framework

Use the simplest solution that solves the problem well.

---

## 4. Use generators for large streams

Instead of:

```python
data = [process(x) for x in huge_dataset]
```

consider:

```python
data = (process(x) for x in huge_dataset)
```

when lazy processing is appropriate.

---

## 5. Measure performance

Use profiling rather than guessing.

---

## 6. Handle resources safely

Prefer:

```python
with open("data.txt") as file:
    ...
```

instead of manually managing file closure.

---

## 7. Keep functions focused

A function should generally have one clear responsibility.

---

## 8. Prefer composition when inheritance becomes complicated

Composition often produces more flexible systems.

---

## 9. Document public APIs

Use docstrings:

```python
def calculate_total(price: float, quantity: int) -> float:
    """Calculate the total purchase price."""
    return price * quantity
```

---

## 10. Avoid clever code

Advanced Python should improve software quality, not make code unnecessarily difficult to understand.

> **Advanced does not mean complicated.**

---

# 🧪 Practice Exercises

## 🟢 Beginner

### Exercise 1 — Generator

Create a generator that produces numbers from `1` to `100`.

### Exercise 2 — Decorator

Create a decorator that prints:

```text
Function started
Function completed
```

### Exercise 3 — Context Manager

Create a custom context manager that prints when entering and exiting.

### Exercise 4 — Counter

Use `collections.Counter` to count word frequencies.

---

## 🟡 Intermediate

### Exercise 5 — Cache

Implement Fibonacci using `lru_cache`.

### Exercise 6 — Iterator

Create a custom iterator for even numbers.

### Exercise 7 — Type Hints

Add complete type annotations to an existing Python project.

### Exercise 8 — Dataclass

Create a `Product` dataclass with:

```text
name
price
quantity
```

and a method to calculate total price.

---

## 🔴 Advanced

### Exercise 9 — Retry Decorator

Create a decorator that retries a failing function three times.

### Exercise 10 — Execution Timer

Create a decorator that measures function execution time.

### Exercise 11 — Thread Pool

Use `ThreadPoolExecutor` to process multiple I/O tasks.

### Exercise 12 — Process Pool

Use `ProcessPoolExecutor` for CPU-intensive calculations.

### Exercise 13 — Async Tasks

Create multiple asynchronous tasks and run them concurrently.

### Exercise 14 — Custom Descriptor

Create a descriptor that validates attribute values.

### Exercise 15 — Plugin System

Build a simple plugin architecture where modules can register functionality dynamically.

---

# 🚀 Advanced Projects

## 1. 🔥 Task Scheduler

Build a task scheduler supporting:

* Scheduled jobs
* Thread execution
* Logging
* Retry
* Error handling
* Task status
* Configuration

---

## 2. 🌐 Concurrent URL Checker

Build a tool that:

* Accepts multiple URLs
* Checks HTTP status
* Measures response time
* Uses concurrency
* Handles failures
* Produces a report

---

## 3. ⚡ Async API Client

Build an asynchronous client that:

* Sends multiple requests
* Handles timeouts
* Retries failures
* Limits concurrency
* Logs operations
* Handles API errors

---

## 4. 🧩 Plugin Architecture

Create a Python application where external modules can register plugins.

Example:

```text
plugins/
├── email_plugin.py
├── logging_plugin.py
└── notification_plugin.py
```

The main application dynamically discovers and loads plugins.

---

## 5. 📊 Data Processing Pipeline

Build a streaming pipeline:

```text
Input
  ↓
Validation
  ↓
Transformation
  ↓
Filtering
  ↓
Aggregation
  ↓
Output
```

Use:

* Generators
* Iterators
* Functional programming
* Dataclasses
* Type hints
* Logging

---

# 💼 Interview Questions

### Beginner → Intermediate

1. What is an iterator?
2. What is a generator?
3. What is the difference between `return` and `yield`?
4. What is a decorator?
5. What is a closure?
6. What are `*args` and `**kwargs`?
7. What is a context manager?
8. What is the purpose of `with`?
9. What is `functools`?
10. What is `itertools`?
11. What are dataclasses?
12. What are type hints?

### Advanced

13. How does a generator save memory?
14. How does a decorator work internally?
15. What is the difference between shallow and deep copy?
16. What is MRO?
17. How does multiple inheritance work?
18. What is a descriptor?
19. What is a metaclass?
20. What is monkey patching?
21. What is introspection?
22. What is the difference between threads and processes?
23. What is asynchronous programming?
24. What does `asyncio` provide?
25. What is an event loop?
26. What is a race condition?
27. What is a deadlock?
28. When should multiprocessing be preferred?
29. When should threading be preferred?
30. When should asynchronous programming be preferred?
31. What is caching?
32. How does `lru_cache` work conceptually?
33. What is serialization?
34. Why is untrusted pickle data dangerous?
35. What is an AST?
36. What is structural typing?
37. What is a Protocol?
38. What is the difference between an ABC and a Protocol?
39. How does Python manage memory?
40. How would you profile a slow Python program?

---

# ⚡ Quick Revision

| Concept         | Key Idea                                       |
| --------------- | ---------------------------------------------- |
| Iterator        | Produces values through iteration protocol     |
| Generator       | Lazy iterator using `yield`                    |
| Decorator       | Extends function/class behavior                |
| Closure         | Inner function remembers enclosing state       |
| Context Manager | Safely manages resources                       |
| Comprehension   | Compact collection construction                |
| `functools`     | Functional programming utilities               |
| `itertools`     | Iterator building blocks                       |
| `collections`   | Specialized containers                         |
| Type Hint       | Documents expected types                       |
| Dataclass       | Simplifies data-oriented classes               |
| Descriptor      | Controls attribute access                      |
| MRO             | Determines method lookup order                 |
| Metaclass       | Controls class creation                        |
| Introspection   | Examines objects/program structure             |
| Shallow Copy    | Copies outer object                            |
| Deep Copy       | Recursively copies nested objects              |
| Caching         | Reuses previous results                        |
| Threading       | Concurrent execution using threads             |
| Multiprocessing | Parallel work using processes                  |
| Asyncio         | Asynchronous I/O framework                     |
| Serialization   | Converts objects/data for storage or transport |
| AST             | Structured representation of source code       |

---

# 🧠 Important Mental Models

## Iterator

```text
Iterable
   ↓
iter()
   ↓
Iterator
   ↓
next()
   ↓
Value
```

---

## Generator

```text
Function
   ↓
yield
   ↓
Generator Object
   ↓
next()
   ↓
Next Value
```

---

## Decorator

```text
Original Function
       ↓
    Decorator
       ↓
Wrapped Function
```

---

## Context Manager

```text
__enter__()
     ↓
  Resource
     ↓
Application Code
     ↓
__exit__()
     ↓
Cleanup
```

---

## Concurrency

```text
                ┌── Thread
Task ───────────┼── Process
                └── Async
```

Choose the model according to the workload rather than using concurrency simply because it is available.

---

# 🧭 Advanced Python Roadmap

A useful progression is:

```text
Python Fundamentals
        ↓
Functions & OOP
        ↓
Modules & Packages
        ↓
Exceptions & File Handling
        ↓
Iterators & Generators
        ↓
Decorators & Closures
        ↓
Context Managers
        ↓
Functional Programming
        ↓
Type Hints & Dataclasses
        ↓
Descriptors & Protocols
        ↓
MRO & Object Model
        ↓
Metaprogramming
        ↓
Memory & Performance
        ↓
Threading
        ↓
Multiprocessing
        ↓
Asyncio
        ↓
Design Patterns
        ↓
Production Python
```

---

# 🏆 What You Should Be Able to Build

After mastering Advanced Python, you should be comfortable building:

* CLI applications
* Automation tools
* Data processing pipelines
* API clients
* Backend services
* Concurrent applications
* Async applications
* Plugin systems
* Developer tools
* Web scrapers
* Task schedulers
* Background workers
* Production Python packages

---

# 📖 References

* [Python Documentation](https://docs.python.org/3/?utm_source=chatgpt.com)
* [Python Language Reference](https://docs.python.org/3/reference/?utm_source=chatgpt.com)
* [Python Standard Library](https://docs.python.org/3/library/?utm_source=chatgpt.com)
* [Python `asyncio` Documentation](https://docs.python.org/3/library/asyncio.html?utm_source=chatgpt.com)
* [Python `functools` Documentation](https://docs.python.org/3/library/functools.html?utm_source=chatgpt.com)
* [Python `itertools` Documentation](https://docs.python.org/3/library/itertools.html?utm_source=chatgpt.com)
* [Python `collections` Documentation](https://docs.python.org/3/library/collections.html?utm_source=chatgpt.com)
* [Python `typing` Documentation](https://docs.python.org/3/library/typing.html?utm_source=chatgpt.com)

---

# 📂 Suggested Folder Structure

```text
21-Advanced-Python/
│
├── README.md
│
├── 01-Iterators/
├── 02-Generators/
├── 03-Decorators/
├── 04-Closures/
├── 05-Context-Managers/
├── 06-Comprehensions/
├── 07-Functools/
├── 08-ItTools/
├── 09-Collections/
├── 10-Type-Hints/
├── 11-Dataclasses/
├── 12-Descriptors/
├── 13-Dunder-Methods/
├── 14-MRO/
├── 15-Metaclasses/
├── 16-Introspection/
├── 17-Memory-Management/
├── 18-Performance/
├── 19-Caching/
├── 20-Threading/
├── 21-Multiprocessing/
├── 22-AsyncIO/
├── 23-Concurrency/
├── 24-Serialization/
├── 25-AST/
└── 26-Design-Patterns/
```

---

# 🔍 Professional Checklist

Before considering yourself comfortable with Advanced Python, you should be able to explain:

* [ ] Iterable vs iterator
* [ ] Iterator protocol
* [ ] Generator functions
* [ ] Generator expressions
* [ ] Decorators
* [ ] Closures
* [ ] Higher-order functions
* [ ] Context managers
* [ ] `contextlib`
* [ ] Comprehensions
* [ ] `functools`
* [ ] `itertools`
* [ ] `collections`
* [ ] Type hints
* [ ] Dataclasses
* [ ] Descriptors
* [ ] Dunder methods
* [ ] MRO
* [ ] Multiple inheritance
* [ ] Abstract base classes
* [ ] Protocols
* [ ] Metaclasses
* [ ] Introspection
* [ ] Shallow vs deep copy
* [ ] Memory management
* [ ] Profiling
* [ ] Caching
* [ ] Threading
* [ ] Multiprocessing
* [ ] Asyncio
* [ ] Race conditions
* [ ] Synchronization
* [ ] Serialization
* [ ] AST
* [ ] Design patterns

---

# 🎯 Final Takeaways

Advanced Python is about **depth, not complexity**.

The most important skills are not memorizing every Python feature, but knowing:

1. **How Python works**
2. **Which feature solves a particular problem**
3. **When an advanced feature is unnecessary**
4. **How to write readable code**
5. **How to measure performance**
6. **How to handle concurrency safely**
7. **How to design maintainable systems**
8. **How to use Python's standard library effectively**

A strong Python developer knows not only how to write:

```python
def solve():
    ...
```

but also understands what happens around that function:

```text
Source Code
     ↓
Parser / AST
     ↓
Compilation
     ↓
Python Runtime
     ↓
Objects & References
     ↓
Memory Management
     ↓
I/O / Threads / Processes / Async Tasks
```

> **Master the fundamentals first. Use advanced features only when they make the solution better.**

---

## 🚀 Continue Your Python Journey

Previous:

**20 — Logging**

Next:

**22 — Testing & Professional Python Development**

Keep learning. Keep building. Keep improving. 🐍🔥

---

### ⭐ If This Repository Helps You

Consider giving the repository a ⭐ on GitHub and using these examples to build your own projects.

**Learn → Practice → Build → Refactor → Test → Ship.**

This version is intentionally broad so `21-Advanced-Python` can serve as the **bridge from core Python into professional Python development**.
