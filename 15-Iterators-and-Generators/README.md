# 🔄 Iterators and Generators in Python

> **Python Programming — Advanced Core Concepts**

Iterators and generators are powerful Python features used to process data **one item at a time** instead of loading an entire collection into memory.

They are especially useful when working with:

* Large datasets
* Files and streams
* APIs
* Data pipelines
* Infinite sequences
* Memory-efficient applications

---

## 📚 Table of Contents

* [Learning Objectives](#-learning-objectives)
* [What Are Iterators?](#-what-are-iterators)
* [Iterable vs Iterator](#-iterable-vs-iterator)
* [The Iterator Protocol](#-the-iterator-protocol)
* [iter() and next()](#-iter-and-next)
* [StopIteration](#-stopiteration)
* [Creating a Custom Iterator](#-creating-a-custom-iterator)
* [Generators](#-generators)
* [yield Keyword](#-yield-keyword)
* [Generator vs Normal Function](#-generator-vs-normal-function)
* [Generator Expressions](#-generator-expressions)
* [Generator with for Loop](#-generator-with-for-loop)
* [Generator State](#-generator-state)
* [send(), throw(), and close()](#-send-throw-and-close)
* [Infinite Generators](#-infinite-generators)
* [Memory Efficiency](#-memory-efficiency)
* [Real-World Examples](#-real-world-examples)
* [Iterator vs Generator](#-iterator-vs-generator)
* [Common Mistakes](#-common-mistakes)
* [Practice Exercises](#-practice-exercises)
* [Mini Project](#-mini-project)
* [Interview Questions](#-interview-questions)
* [Quick Revision](#-quick-revision)
* [Best Practices](#-best-practices)
* [References](#-references)
* [Next Topic](#-next-topic)

---

# 🎯 Learning Objectives

After completing this topic, you should be able to:

* Understand iterables and iterators
* Understand Python's iterator protocol
* Use `iter()` and `next()`
* Understand `StopIteration`
* Create custom iterators
* Understand generators
* Use the `yield` keyword
* Create generator expressions
* Build infinite generators
* Understand lazy evaluation
* Compare iterators and generators
* Write memory-efficient Python programs

---

# 🧠 What Are Iterators?

An **iterator** is an object that allows you to access elements of a collection **one at a time**.

Instead of accessing all elements simultaneously, an iterator keeps track of its current position.

### Example

```python
numbers = [10, 20, 30, 40]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

### Output

```text
10
20
30
```

The iterator remembers where it stopped.

```python
print(next(iterator))
```

Output:

```text
40
```

---

# 🔗 Iterable vs Iterator

These two concepts are related but different.

## Iterable

An **iterable** is an object that can return an iterator.

Examples:

```python
list
tuple
string
set
dictionary
range
```

Example:

```python
numbers = [1, 2, 3, 4]

for number in numbers:
    print(number)
```

A list is iterable.

---

## Iterator

An iterator is an object that produces values one at a time.

```python
numbers = [1, 2, 3]

iterator = iter(numbers)

print(next(iterator))
```

Output:

```text
1
```

### Simple Relationship

```text
Iterable
   │
   │ iter()
   ▼
Iterator
   │
   │ next()
   ▼
Next Value
```

---

# ⚙️ The Iterator Protocol

Python iterators follow a protocol based on two special methods:

```python
__iter__()
__next__()
```

An iterator must implement:

### `__iter__()`

Returns the iterator object itself.

### `__next__()`

Returns the next value.

When there are no more values, `__next__()` raises:

```python
StopIteration
```

---

# 🔁 `iter()` and `next()`

Python provides two built-in functions for working with iterators.

## `iter()`

Converts an iterable into an iterator.

```python
numbers = [10, 20, 30]

iterator = iter(numbers)
```

## `next()`

Retrieves the next value.

```python
print(next(iterator))
```

Output:

```text
10
```

Another call:

```python
print(next(iterator))
```

Output:

```text
20
```

---

# 🛑 StopIteration

When an iterator has no more values, Python raises:

```python
StopIteration
```

Example:

```python
numbers = [1, 2]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

The third `next()` raises:

```text
StopIteration
```

Normally, `for` loops handle this automatically.

---

# 🔄 How a `for` Loop Works Internally

Consider:

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

Conceptually, Python performs something similar to:

```python
iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        break
```

This is one of the key ideas behind Python iteration.

---

# 🏗️ Creating a Custom Iterator

You can create your own iterator using a class.

```python
class CountUp:
    def __init__(self, max_value):
        self.current = 1
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max_value:
            value = self.current
            self.current += 1
            return value

        raise StopIteration
```

Usage:

```python
counter = CountUp(5)

for number in counter:
    print(number)
```

Output:

```text
1
2
3
4
5
```

---

# 🧩 Understanding the Custom Iterator

The important methods are:

```python
def __iter__(self):
    return self
```

and:

```python
def __next__(self):
    ...
```

The iterator maintains its state using:

```python
self.current
```

Every call to `next()` updates that state.

---

# ⚡ Generators

A **generator** is a special type of iterator that makes it easier to create lazy sequences.

Generators are usually created using:

```python
yield
```

Instead of manually implementing:

```python
__iter__()
__next__()
```

you can often use a generator function.

---

# 🏭 Generator Functions

A function containing `yield` becomes a generator function.

Example:

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

Calling the function does not immediately execute all of its code.

```python
generator = numbers()

print(generator)
```

The result is a generator object.

---

# 🔑 `yield` Keyword

The `yield` keyword temporarily pauses a generator and produces a value.

Example:

```python
def count():
    yield 1
    yield 2
    yield 3
```

Usage:

```python
for number in count():
    print(number)
```

Output:

```text
1
2
3
```

---

# 🆚 Generator vs Normal Function

### Normal Function

```python
def get_numbers():
    return [1, 2, 3]
```

The entire list is created immediately.

### Generator Function

```python
def get_numbers():
    yield 1
    yield 2
    yield 3
```

Values are produced one at a time.

### Key Difference

```text
return
   ↓
Produces a result and ends the function

yield
   ↓
Produces a value and pauses the function
```

---

# ⏸️ Generator State

Generators remember their execution state.

Example:

```python
def numbers():
    print("Start")
    yield 1

    print("Middle")
    yield 2

    print("End")
    yield 3
```

```python
generator = numbers()

print(next(generator))
print(next(generator))
print(next(generator))
```

Output:

```text
Start
1
Middle
2
End
3
```

The generator resumes exactly where it previously paused.

---

# 🧮 Generator Expressions

Generator expressions provide a concise way to create generators.

### List Comprehension

```python
numbers = [x * x for x in range(5)]
```

This creates a list immediately.

### Generator Expression

```python
numbers = (x * x for x in range(5))
```

This produces values lazily.

Usage:

```python
for number in numbers:
    print(number)
```

---

# 💾 Memory Efficiency

One of the biggest advantages of generators is **memory efficiency**.

Consider:

```python
numbers = [x * x for x in range(1000000)]
```

The entire list is stored in memory.

With a generator:

```python
numbers = (x * x for x in range(1000000))
```

values are generated only when required.

### Concept

```text
List
┌──────────────────────────┐
│ All values stored in RAM │
└──────────────────────────┘

Generator
┌──────────────┐
│ Generate one │
│ value at a   │
│ time         │
└──────────────┘
```

This is particularly useful for large datasets.

---

# 🔁 Generator with `for` Loop

Generators work naturally with `for` loops.

```python
def even_numbers(limit):
    for number in range(limit + 1):
        if number % 2 == 0:
            yield number
```

Usage:

```python
for number in even_numbers(10):
    print(number)
```

Output:

```text
0
2
4
6
8
10
```

---

# ♾️ Infinite Generators

Generators can represent sequences that never end.

Example:

```python
def counter():
    number = 1

    while True:
        yield number
        number += 1
```

Usage:

```python
numbers = counter()

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

The generator can continue indefinitely.

### Important

When working with infinite generators, always have a stopping condition.

```python
for number in counter():
    if number > 5:
        break

    print(number)
```

---

# 📤 `send()`, `throw()`, and `close()`

Generators support advanced control methods.

## `send()`

Allows a value to be sent into a suspended generator.

```python
def receiver():
    value = yield
    print("Received:", value)

generator = receiver()

next(generator)

generator.send("Hello")
```

Output:

```text
Received: Hello
```

---

## `close()`

Stops a generator.

```python
def numbers():
    yield 1
    yield 2
    yield 3

generator = numbers()

print(next(generator))

generator.close()
```

---

## `throw()`

Raises an exception at the generator's suspended point.

```python
def generator_function():
    try:
        yield 1
        yield 2
    except ValueError:
        print("ValueError handled")

generator = generator_function()

next(generator)

generator.throw(ValueError)
```

---

# 📄 Real-World Example: Reading a Large File

Suppose a file contains millions of lines.

Instead of:

```python
with open("large_file.txt") as file:
    lines = file.readlines()

for line in lines:
    print(line)
```

you can process lines lazily:

```python
def read_lines(filename):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            yield line
```

Usage:

```python
for line in read_lines("large_file.txt"):
    print(line)
```

Only the required data is processed at a time.

---

# 🌐 Real-World Example: Data Processing

Generators are useful in data pipelines.

```python
def numbers():
    for number in range(1, 11):
        yield number
```

Transform the data:

```python
def squares(numbers):
    for number in numbers:
        yield number ** 2
```

Use the pipeline:

```python
result = squares(numbers())

for value in result:
    print(value)
```

### Pipeline

```text
Source
  ↓
Generator
  ↓
Transformation
  ↓
Generator
  ↓
Consumer
```

This approach is useful for scalable data processing.

---

# 🔢 Generator Pipeline Example

```python
def numbers():
    for number in range(1, 11):
        yield number


def even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number


def squares(numbers):
    for number in numbers:
        yield number ** 2


pipeline = squares(even_numbers(numbers()))

for value in pipeline:
    print(value)
```

Output:

```text
4
16
36
64
100
```

Each stage processes values lazily.

---

# 🆚 Iterator vs Generator

| Feature          | Iterator               | Generator              |
| ---------------- | ---------------------- | ---------------------- |
| Implementation   | Usually class-based    | Usually function-based |
| `__iter__()`     | Required               | Provided automatically |
| `__next__()`     | Required               | Provided automatically |
| `yield`          | Not required           | Commonly used          |
| State management | Manual                 | Automatic              |
| Code complexity  | Higher                 | Lower                  |
| Memory efficient | Yes                    | Yes                    |
| Lazy evaluation  | Yes                    | Yes                    |
| Best for         | Custom iteration logic | Simple lazy sequences  |

### Simple Rule

> **Every generator is an iterator, but not every iterator is a generator.**

---

# 🧠 Lazy Evaluation

Generators use **lazy evaluation**.

Instead of calculating everything immediately:

```text
Traditional approach:

Input → Calculate Everything → Store Everything → Use


Generator:

Input → Calculate → Use
          ↓
       Next Value
          ↓
       Calculate → Use
```

This can significantly reduce memory usage.

---

# 🛠️ Useful Built-in Functions

Python provides several functions that work with iterables and iterators.

## `enumerate()`

```python
names = ["Alice", "Bob", "Charlie"]

for index, name in enumerate(names):
    print(index, name)
```

---

## `zip()`

```python
names = ["Alice", "Bob"]
ages = [25, 30]

for name, age in zip(names, ages):
    print(name, age)
```

---

## `map()`

```python
numbers = [1, 2, 3, 4]

result = map(lambda x: x * 2, numbers)

for value in result:
    print(value)
```

---

## `filter()`

```python
numbers = [1, 2, 3, 4, 5]

result = filter(lambda x: x % 2 == 0, numbers)

for value in result:
    print(value)
```

These functions return iterator-like lazy objects in modern Python.

---

# 🔍 Checking Iterable and Iterator

You can inspect an object using:

```python
numbers = [1, 2, 3]

print(iter(numbers))
```

You can also check whether an object has the iterator protocol:

```python
print(hasattr(numbers, "__iter__"))
print(hasattr(numbers, "__next__"))
```

For a list:

```text
__iter__ → True
__next__ → False
```

For a list iterator:

```python
iterator = iter(numbers)

print(hasattr(iterator, "__iter__"))
print(hasattr(iterator, "__next__"))
```

Output:

```text
True
True
```

---

# ⚠️ Common Mistakes

## 1. Calling `next()` after exhaustion

```python
iterator = iter([1])

print(next(iterator))
print(next(iterator))
```

The second call raises:

```text
StopIteration
```

---

## 2. Forgetting that generators are consumed

```python
generator = (x for x in range(3))

print(list(generator))
print(list(generator))
```

The second result is:

```python
[]
```

A generator generally cannot be restarted after it has been exhausted.

---

## 3. Converting huge generators into lists

Avoid:

```python
list(huge_generator)
```

if the data is extremely large.

This defeats the memory-saving benefit of the generator.

---

## 4. Creating an accidental infinite loop

Be careful with:

```python
def infinite():
    number = 0

    while True:
        yield number
        number += 1
```

Always consume infinite generators with a stopping condition.

---

# 🧪 Practice Exercises

### Beginner

1. Create an iterator from a list.
2. Use `next()` to retrieve elements.
3. Handle `StopIteration`.
4. Create a generator that yields numbers from 1 to 10.
5. Create a generator that yields even numbers.
6. Create a generator expression for squares.

### Intermediate

7. Create a custom countdown iterator.
8. Create a generator for Fibonacci numbers.
9. Create a generator that yields prime numbers.
10. Create a generator that reads a file line by line.
11. Create a generator that filters positive numbers.
12. Build a generator pipeline.

### Advanced

13. Create an infinite Fibonacci generator.
14. Use `send()` with a generator.
15. Build a lazy data-processing pipeline.
16. Compare memory usage of a list and generator.
17. Create a custom iterator for pagination.
18. Build a log-file processing generator.

---

# 🚀 Mini Project — Lazy Data Processor

Build a program that processes a large collection of numbers using generators.

### Requirements

Create:

```python
def read_numbers():
    ...


def filter_even(numbers):
    ...


def square(numbers):
    ...


def calculate_total(numbers):
    ...
```

### Pipeline

```text
Input
  ↓
Read Numbers
  ↓
Filter Even
  ↓
Square
  ↓
Calculate Result
```

### Example

```python
def numbers():
    for number in range(1, 21):
        yield number


def even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield number


def squares(numbers):
    for number in numbers:
        yield number ** 2


result = squares(even_numbers(numbers()))

print(sum(result))
```

This demonstrates:

* Generators
* `yield`
* Lazy evaluation
* Generator pipelines
* Memory-efficient processing

---

# 💼 Interview Questions

### 1. What is an iterator?

An iterator is an object that produces values one at a time using the iterator protocol.

---

### 2. What is an iterable?

An iterable is an object that can return an iterator.

Examples include lists, tuples, strings, sets, dictionaries, and ranges.

---

### 3. What is the iterator protocol?

The iterator protocol is based primarily on:

```python
__iter__()
__next__()
```

---

### 4. What is `StopIteration`?

`StopIteration` signals that an iterator has no more values.

---

### 5. What is a generator?

A generator is a convenient way to create an iterator, commonly using the `yield` keyword.

---

### 6. What is the difference between `return` and `yield`?

`return` ends a function and returns a result.

`yield` produces a value and pauses the generator, allowing it to resume later.

---

### 7. Why are generators memory efficient?

Because they generate values lazily instead of storing the entire sequence in memory.

---

### 8. Can a generator be reused?

Generally, no. Once exhausted, a generator cannot simply be restarted.

---

### 9. What happens when `next()` is called on an exhausted iterator?

It raises:

```python
StopIteration
```

---

### 10. Are generators iterators?

Yes.

> Every generator is an iterator, but not every iterator is a generator.

---

### 11. What is lazy evaluation?

Lazy evaluation means a value is calculated only when it is needed.

---

### 12. What does `yield` do?

It produces a value and suspends the generator's execution until the next value is requested.

---

### 13. What is a generator expression?

A compact expression for creating a generator:

```python
(x * x for x in range(10))
```

---

### 14. What is the advantage of generators over lists?

Generators can process large or potentially infinite sequences without storing all values simultaneously.

---

# ⚡ Quick Revision

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
   ↓
next()
   ↓
Value
   ↓
StopIteration
```

### Iterator

```python
class MyIterator:
    def __iter__(self):
        return self

    def __next__(self):
        ...
```

### Generator

```python
def my_generator():
    yield value
```

### Generator Expression

```python
(x for x in iterable)
```

### Main Concept

```text
Iterator = object that produces values one at a time

Generator = easy way to create an iterator

yield = pause + produce value

Lazy evaluation = calculate only when needed
```

---

# ✅ Best Practices

* Prefer generators when processing large sequences.
* Use `yield` for lazy data production.
* Avoid converting huge generators into lists unnecessarily.
* Use meaningful generator function names.
* Handle `StopIteration` when manually calling `next()`.
* Add explicit stopping conditions for infinite generators.
* Use generator pipelines for large data-processing workflows.
* Prefer simple generators over complicated custom iterator classes when possible.
* Use custom iterators when you need more control over iteration state or behavior.
* Remember that generators are generally single-use.

---

# 📌 Key Takeaways

> **Iterators provide a standard way to traverse data one item at a time.**

> **Generators provide a simple and efficient way to create iterators.**

> **`yield` pauses execution while preserving the generator's state.**

> **Lazy evaluation helps reduce unnecessary computation and memory usage.**

> **Generators are especially powerful for files, streams, APIs, pipelines, and large datasets.**

---

# 📖 References

* [Python Documentation — Iterator Types](https://docs.python.org/3/library/stdtypes.html?utm_source=chatgpt.com#iterator-types)
* [Python Documentation — Generators](https://docs.python.org/3/reference/expressions.html?utm_source=chatgpt.com#generator-expressions)
* [Python Documentation — `yield` Expressions](https://docs.python.org/3/reference/expressions.html?utm_source=chatgpt.com#yield-expressions)
* [Python Tutorial — Iterators](https://docs.python.org/3/tutorial/classes.html?utm_source=chatgpt.com#iterators)

---

# ⏭️ Next Topic

Continue your Python journey with:

### **16 — Decorators and Context Managers**

You will learn:

* Function decorators
* `@decorator` syntax
* Higher-order functions
* Closures
* `functools.wraps`
* Context managers
* `with` statement
* `__enter__()` and `__exit__()`
* Custom context managers
* `contextlib`
* Real-world Python patterns

---

<div align="center">

### 🐍 Keep Building. Keep Learning. Keep Coding.

**Python Programming — From Fundamentals to Advanced**

</div>
