# 🎯 16 — Decorators in Python

> **Python Programming — Beginner to Advanced**

Decorators are one of the most powerful and important concepts in Python.

They allow you to **modify, extend, or enhance the behavior of a function, method, or class without changing its original source code**.

Decorators are widely used in:

* Web frameworks
* Authentication and authorization
* Logging
* Caching
* Validation
* Performance monitoring
* API development
* Testing
* Retry mechanisms
* Access control
* Database applications
* Class-based frameworks

---

## 📚 Table of Contents

* [Learning Objectives](#-learning-objectives)
* [What is a Decorator?](#-what-is-a-decorator)
* [Why Do We Need Decorators?](#-why-do-we-need-decorators)
* [Understanding Functions as Objects](#-understanding-functions-as-objects)
* [First-Class Functions](#-first-class-functions)
* [Passing Functions as Arguments](#-passing-functions-as-arguments)
* [Returning Functions](#-returning-functions)
* [Higher-Order Functions](#-higher-order-functions)
* [Nested Functions](#-nested-functions)
* [Closures](#-closures)
* [Understanding Decorators Step by Step](#-understanding-decorators-step-by-step)
* [Basic Decorator](#-basic-decorator)
* [`@` Decorator Syntax](#--decorator-syntax)
* [How Decorator Syntax Works Internally](#-how-decorator-syntax-works-internally)
* [Decorator Execution Flow](#-decorator-execution-flow)
* [Decorators with Arguments](#-decorators-with-arguments)
* [Preserving Function Metadata](#-preserving-function-metadata)
* [Why `functools.wraps` Matters](#-why-functoolswraps-matters)
* [Decorators with `*args` and `**kwargs`](#-decorators-with-args-and-kwargs)
* [Returning Values from Decorators](#-returning-values-from-decorators)
* [Decorators with Function Arguments](#-decorators-with-function-arguments)
* [Multiple Decorators](#-multiple-decorators)
* [Decorator Order](#-decorator-order)
* [Decorating Methods](#-decorating-methods)
* [Decorating Classes](#-decorating-classes)
* [Class Decorators](#-class-decorators)
* [Built-in Decorators](#-built-in-decorators)
* [`@staticmethod`](#-staticmethod)
* [`@classmethod`](#-classmethod)
* [`@property`](#-property)
* [`@abstractmethod`](#-abstractmethod)
* [Real-World Examples](#-real-world-examples)
* [Authentication Decorator](#-authentication-decorator)
* [Logging Decorator](#-logging-decorator)
* [Timing Decorator](#-timing-decorator)
* [Validation Decorator](#-validation-decorator)
* [Caching Decorator](#-caching-decorator)
* [Retry Decorator](#-retry-decorator)
* [Advanced Decorator Concepts](#-advanced-decorator-concepts)
* [Decorator Factory](#-decorator-factory)
* [Stateful Decorators](#-stateful-decorators)
* [Decorators and Closures](#-decorators-and-closures)
* [Decorators and Dependency Injection](#-decorators-and-dependency-injection)
* [Common Mistakes](#-common-mistakes)
* [When Should You Use Decorators?](#-when-should-you-use-decorators)
* [When Should You Avoid Decorators?](#-when-should-you-avoid-decorators)
* [Practice Exercises](#-practice-exercises)
* [Mini Projects](#-mini-projects)
* [Interview Questions](#-interview-questions)
* [Quick Revision](#-quick-revision)
* [Best Practices](#-best-practices)
* [References](#-references)
* [Next Topic](#-next-topic)

---

# 🎯 Learning Objectives

After completing this chapter, you should be able to:

* Understand what decorators are
* Understand why decorators exist
* Understand functions as objects
* Understand first-class functions
* Understand higher-order functions
* Understand nested functions
* Understand closures
* Create custom decorators
* Use `@decorator` syntax
* Understand decorator execution order
* Pass arguments to decorated functions
* Preserve function metadata
* Use `functools.wraps`
* Create decorators using `*args` and `**kwargs`
* Create decorators that accept configuration
* Decorate methods
* Decorate classes
* Understand built-in decorators
* Build practical decorators for real applications
* Understand advanced decorator patterns
* Write clean and maintainable decorators

---

# 🧠 What is a Decorator?

A **decorator** is a function that takes another function as input and returns a new function with additional or modified behavior.

Conceptually:

```text
Original Function
       │
       ▼
   Decorator
       │
       ▼
Enhanced Function
```

A decorator allows us to add behavior **without directly modifying the original function**.

---

# 💡 Why Do We Need Decorators?

Suppose you have several functions:

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b
```

Now imagine that every function needs:

* Logging
* Authentication
* Execution timing
* Input validation
* Error handling

You could repeat the same code inside every function.

That creates:

```text
❌ Duplicate Code
❌ Harder Maintenance
❌ Difficult Testing
❌ Less Reusability
```

Decorators provide a reusable solution:

```text
              ┌─────────────┐
              │  Decorator  │
              └──────┬──────┘
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
      add()       sub()        multiply()
```

One decorator can enhance many functions.

---

# 🧩 Understanding Functions as Objects

Before learning decorators, you must understand an important Python concept:

> **Functions are objects.**

A function can be:

* Stored in a variable
* Passed as an argument
* Returned from another function
* Stored inside a collection

Example:

```python
def greet():
    print("Hello")


message = greet

message()
```

Output:

```text
Hello
```

Both names refer to the same function object.

---

# ⭐ First-Class Functions

Python treats functions as **first-class objects**.

This means functions can be manipulated like other objects.

For example:

```python
def square(number):
    return number ** 2


operation = square

print(operation(5))
```

Output:

```text
25
```

This property is fundamental to decorators.

---

# 📦 Passing Functions as Arguments

A function can receive another function as an argument.

```python
def greet():
    return "Hello"


def execute(function):
    return function()


print(execute(greet))
```

Output:

```text
Hello
```

Here:

```python
execute(greet)
```

passes the function object `greet` into `execute`.

---

# 🔙 Returning Functions

A function can also return another function.

```python
def outer():
    def inner():
        print("Hello from inner")

    return inner


function = outer()

function()
```

Output:

```text
Hello from inner
```

This concept is extremely important because decorators commonly return wrapper functions.

---

# 🔝 Higher-Order Functions

A **higher-order function** is a function that:

1. Accepts another function as an argument, or
2. Returns another function.

Example:

```python
def execute(function):
    return function()
```

`execute()` is a higher-order function.

Decorators are built on top of this concept.

---

# 🏠 Nested Functions

A function defined inside another function is called a **nested function**.

```python
def outer():
    
    def inner():
        print("Inside inner function")

    inner()


outer()
```

Nested functions are commonly used when creating decorators.

---

# 🔐 Closures

A **closure** occurs when an inner function remembers variables from its enclosing function even after the enclosing function has finished executing.

Example:

```python
def outer(message):

    def inner():
        print(message)

    return inner


hello = outer("Hello")

hello()
```

Output:

```text
Hello
```

The `inner()` function remembers:

```python
message
```

even after `outer()` has finished.

---

# 🧠 Decorators Depend on Three Core Concepts

To understand decorators deeply, remember:

```text
Functions as Objects
        +
Higher-Order Functions
        +
Closures
        =
Decorators
```

This mental model makes decorator syntax much easier to understand.

---

# 🏗️ Understanding Decorators Step by Step

Let's build one manually.

Suppose we have:

```python
def greet():
    print("Hello")
```

We want to execute something before `greet()`.

Create a decorator:

```python
def decorator(function):

    def wrapper():
        print("Before function")
        function()
        print("After function")

    return wrapper
```

Apply it manually:

```python
greet = decorator(greet)

greet()
```

Output:

```text
Before function
Hello
After function
```

---

# 🔄 Basic Decorator

A cleaner example:

```python
def logger(function):

    def wrapper():
        print("Function is starting")
        function()
        print("Function has finished")

    return wrapper
```

Use it:

```python
def greet():
    print("Hello")


greet = logger(greet)

greet()
```

Output:

```text
Function is starting
Hello
Function has finished
```

The original function has been wrapped with additional behavior.

---

# @ Decorator Syntax

Python provides special syntax for decorators.

Instead of:

```python
greet = logger(greet)
```

you can write:

```python
@logger
def greet():
    print("Hello")
```

Then:

```python
greet()
```

Output:

```text
Function is starting
Hello
Function has finished
```

---

# 🔍 How `@` Decorator Syntax Works

This:

```python
@logger
def greet():
    print("Hello")
```

is approximately equivalent to:

```python
def greet():
    print("Hello")


greet = logger(greet)
```

This is one of the most important facts to remember.

> `@decorator` is syntactic sugar for replacing the function with the decorator's returned value.

---

# 🔄 Decorator Execution Flow

Consider:

```python
@logger
def greet():
    print("Hello")
```

Conceptually:

```text
              greet()
                 │
                 ▼
             wrapper()
                 │
       ┌─────────┴─────────┐
       ▼                   ▼
 Before                  After
       │                   ▲
       ▼                   │
    greet() ───────────────┘
```

The wrapper controls when and how the original function executes.

---

# ⚠️ Important: Decoration vs Function Execution

Consider:

```python
@logger
def greet():
    print("Hello")
```

The decorator is applied when the function is defined.

But:

```python
greet()
```

executes the resulting wrapped function.

These are two separate events:

```text
Function Definition
        ↓
Decorator Application
        ↓
Function Call
        ↓
Wrapper Execution
        ↓
Original Function Execution
```

Understanding this distinction is essential for debugging decorators.

---

# 🎯 Decorators with Arguments

Real functions often accept arguments.

Example:

```python
def greet(name):
    print(f"Hello {name}")
```

A simple wrapper like:

```python
def wrapper():
```

cannot accept arguments.

We need:

```python
def wrapper(*args, **kwargs):
```

Example:

```python
def logger(function):

    def wrapper(*args, **kwargs):
        print("Function started")

        result = function(*args, **kwargs)

        print("Function finished")

        return result

    return wrapper
```

Use it:

```python
@logger
def greet(name):
    print(f"Hello {name}")


greet("Kishor")
```

---

# 📦 `*args` and `**kwargs`

A general-purpose decorator should usually support arbitrary function arguments.

```python
def decorator(function):

    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper
```

### `*args`

Captures positional arguments.

```python
function(10, 20)
```

becomes:

```python
args = (10, 20)
```

### `**kwargs`

Captures keyword arguments.

```python
function(a=10, b=20)
```

becomes:

```python
kwargs = {
    "a": 10,
    "b": 20
}
```

---

# ↩️ Returning Values from Decorators

A common mistake is forgetting to return the original function's result.

Bad:

```python
def decorator(function):

    def wrapper(*args, **kwargs):
        function(*args, **kwargs)

    return wrapper
```

If the original function returns a value, it gets lost.

Correct:

```python
def decorator(function):

    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result

    return wrapper
```

Or simply:

```python
def decorator(function):

    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper
```

---

# 🏷️ Preserving Function Metadata

Consider:

```python
def greet():
    """Greet the user."""
    print("Hello")
```

Now decorate it:

```python
def decorator(function):

    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper
```

After decoration:

```python
@decorator
def greet():
    """Greet the user."""
    print("Hello")
```

The function's metadata can now refer to the wrapper rather than the original function.

For example:

```python
print(greet.__name__)
```

may produce:

```text
wrapper
```

This is undesirable in many production applications.

---

# 🛠️ Why `functools.wraps` Matters

Python provides:

```python
from functools import wraps
```

Use it like this:

```python
from functools import wraps


def decorator(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper
```

Now:

```python
@decorator
def greet():
    """Greet the user."""
    print("Hello")
```

The original function's metadata is preserved.

```python
print(greet.__name__)
print(greet.__doc__)
```

Output:

```text
greet
Greet the user.
```

### Production Rule

> When writing reusable decorators, prefer `functools.wraps`.

---

# 🔢 Decorators with Function Arguments

Example:

```python
from functools import wraps


def log_call(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Calling {function.__name__}")
        result = function(*args, **kwargs)
        print(f"Finished {function.__name__}")
        return result

    return wrapper
```

Usage:

```python
@log_call
def add(a, b):
    return a + b


result = add(10, 20)

print(result)
```

Output:

```text
Calling add
Finished add
30
```

---

# 🔗 Multiple Decorators

Python allows multiple decorators.

```python
@decorator_one
@decorator_two
def greet():
    print("Hello")
```

The decorators are applied from the bottom upward.

Conceptually:

```python
greet = decorator_one(
    decorator_two(greet)
)
```

So:

```text
greet
 ↓
decorator_two
 ↓
decorator_one
 ↓
final function
```

---

# 📐 Decorator Order

Decorator order matters.

Example:

```python
@A
@B
def function():
    pass
```

Means:

```python
function = A(B(function))
```

It does **not** mean:

```python
function = B(A(function))
```

Changing the order can change the program's behavior.

---

# 🧪 Example of Decorator Order

```python
def first(function):

    def wrapper():
        print("First")
        function()

    return wrapper


def second(function):

    def wrapper():
        print("Second")
        function()

    return wrapper
```

Apply:

```python
@first
@second
def greet():
    print("Hello")
```

Output:

```text
First
Second
Hello
```

---

# 🧑‍💻 Decorating Methods

Decorators can also be applied to class methods.

```python
def logger(function):

    def wrapper(*args, **kwargs):
        print("Method called")
        return function(*args, **kwargs)

    return wrapper


class User:

    @logger
    def login(self):
        print("User logged in")
```

Usage:

```python
user = User()

user.login()
```

Output:

```text
Method called
User logged in
```

The `self` argument is automatically passed through `*args`.

---

# 🏛️ Decorating Classes

Decorators can also be applied to classes.

Example:

```python
def add_method(cls):

    cls.say_hello = lambda self: print("Hello")

    return cls
```

Use:

```python
@add_method
class User:
    pass
```

Now:

```python
user = User()

user.say_hello()
```

Output:

```text
Hello
```

Class decorators receive the class object and can modify or replace it.

---

# 🧱 Class Decorators

A class decorator has the general structure:

```python
def class_decorator(cls):

    # modify class

    return cls
```

Example:

```python
def add_version(cls):

    cls.version = "1.0"

    return cls


@add_version
class Application:
    pass


print(Application.version)
```

Output:

```text
1.0
```

---

# 🐍 Built-in Decorators

Python provides several important built-in decorators.

Common examples include:

```text
@staticmethod
@classmethod
@property
@abstractmethod
```

These are heavily used in professional Python code.

---

# ⚙️ `@staticmethod`

A static method does not receive an automatic `self` or `cls` argument.

```python
class Math:

    @staticmethod
    def add(a, b):
        return a + b
```

Usage:

```python
print(Math.add(10, 20))
```

Use `staticmethod` when the method logically belongs to a class but does not need instance or class state.

---

# 🏛️ `@classmethod`

A class method receives the class as its first argument:

```python
cls
```

Example:

```python
class User:

    count = 0

    @classmethod
    def show_count(cls):
        print(cls.count)
```

Usage:

```python
User.show_count()
```

Class methods are commonly used for:

* Alternative constructors
* Class-level operations
* Factory methods

---

# 🏠 `@property`

The `property` decorator allows a method to be accessed like an attribute.

```python
class Person:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
```

Usage:

```python
person = Person("Kishor")

print(person.name)
```

Notice:

```python
person.name
```

instead of:

```python
person.name()
```

---

# 🧩 `@abstractmethod`

Used with Python's abstract base classes.

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

Subclasses must provide an implementation.

```python
class Dog(Animal):

    def sound(self):
        print("Bark")
```

This is useful for defining interfaces and enforcing contracts.

---

# 🌐 Real-World Decorator Example: Authentication

Decorators are frequently used for access control.

```python
from functools import wraps


def login_required(function):

    @wraps(function)
    def wrapper(user, *args, **kwargs):

        if not user.is_authenticated:
            print("Access denied")
            return None

        return function(user, *args, **kwargs)

    return wrapper
```

Usage:

```python
@login_required
def dashboard(user):
    print("Welcome to dashboard")
```

Conceptually:

```text
Request
   ↓
Authentication Check
   ↓
Authenticated?
  / \
No  Yes
↓    ↓
Deny  Execute
```

---

# 📝 Logging Decorator

A logging decorator can automatically record function calls.

```python
from functools import wraps


def log_call(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print(
            f"Calling {function.__name__}"
        )

        result = function(*args, **kwargs)

        print(
            f"{function.__name__} completed"
        )

        return result

    return wrapper
```

Usage:

```python
@log_call
def calculate(a, b):
    return a + b
```

---

# ⏱️ Timing Decorator

A timing decorator can measure execution time.

```python
import time
from functools import wraps


def timer(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        result = function(*args, **kwargs)

        end = time.perf_counter()

        print(
            f"{function.__name__}: "
            f"{end - start:.6f} seconds"
        )

        return result

    return wrapper
```

Usage:

```python
@timer
def process_data():
    time.sleep(1)
```

This pattern is useful for performance analysis.

---

# ✅ Validation Decorator

Decorators can validate function input.

```python
from functools import wraps


def positive_only(function):

    @wraps(function)
    def wrapper(number):

        if number <= 0:
            raise ValueError(
                "Number must be positive"
            )

        return function(number)

    return wrapper
```

Usage:

```python
@positive_only
def square(number):
    return number ** 2
```

---

# 💾 Caching Decorator

Caching avoids repeating expensive calculations.

Python provides:

```python
from functools import cache
```

Example:

```python
from functools import cache


@cache
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
```

Caching can dramatically improve recursive calculations by reusing previously computed results.

---

# 🔁 Retry Decorator

A retry decorator can repeat an operation when a temporary failure occurs.

Conceptually:

```text
Function Call
     ↓
Success? ───── Yes → Return
     │
     No
     ↓
Retry
     ↓
Success? ───── Yes → Return
     │
     No
     ↓
Retry Limit
     ↓
Raise Error
```

Example:

```python
from functools import wraps
import time


def retry(attempts):

    def decorator(function):

        @wraps(function)
        def wrapper(*args, **kwargs):

            for attempt in range(attempts):
                try:
                    return function(*args, **kwargs)

                except Exception:
                    if attempt == attempts - 1:
                        raise

                    time.sleep(1)

        return wrapper

    return decorator
```

Usage:

```python
@retry(3)
def connect():
    print("Connecting...")
```

---

# 🏭 Decorator Factory

Sometimes we want to configure a decorator.

Example:

```python
@retry(3)
def connect():
    pass
```

Notice that:

```python
retry(3)
```

is not the decorator itself.

It **returns a decorator**.

The structure becomes:

```text
retry(3)
   ↓
Decorator
   ↓
Original Function
   ↓
Wrapped Function
```

This pattern is called a **decorator factory**.

---

# 🧠 Decorator Factory Structure

A parameterized decorator usually has three levels:

```python
def decorator_factory(configuration):

    def decorator(function):

        def wrapper(*args, **kwargs):
            ...

        return wrapper

    return decorator
```

Think of it as:

```text
Level 1 → Configuration
Level 2 → Function
Level 3 → Execution
```

This is an advanced but very useful decorator pattern.

---

# 🔐 Stateful Decorators

A decorator can maintain state using a closure.

Example:

```python
from functools import wraps


def count_calls(function):

    count = 0

    @wraps(function)
    def wrapper(*args, **kwargs):

        nonlocal count

        count += 1

        print(f"Called {count} times")

        return function(*args, **kwargs)

    return wrapper
```

Usage:

```python
@count_calls
def greet():
    print("Hello")
```

Calling:

```python
greet()
greet()
greet()
```

Produces:

```text
Called 1 times
Hello

Called 2 times
Hello

Called 3 times
Hello
```

The closure preserves the state.

---

# 🔗 Decorators and Closures

A typical decorator contains:

```text
Decorator Function
       │
       ├── Receives original function
       │
       ├── Defines wrapper
       │
       ├── Wrapper remembers original function
       │
       └── Returns wrapper
```

That "remembering" behavior is provided by a closure.

This is why understanding closures makes decorators much easier.

---

# 🧩 Decorators and Dependency Injection

Decorators can also be used to provide dependencies or common resources.

For example, a decorator can:

* Open a database connection
* Check authentication
* Inject configuration
* Create a transaction
* Prepare request context

Conceptually:

```text
Function
   ↑
Dependency
   ↑
Decorator
```

This allows cross-cutting concerns to be separated from business logic.

---

# 🏗️ Decorators as Separation of Concerns

One of the biggest architectural benefits of decorators is **separation of concerns**.

Without decorators:

```text
Business Logic
+
Logging
+
Authentication
+
Validation
+
Performance
```

Everything becomes mixed together.

With decorators:

```text
Authentication → Decorator
Logging        → Decorator
Validation     → Decorator
Timing         → Decorator

Business Logic → Function
```

This makes code easier to:

* Read
* Test
* Reuse
* Maintain
* Extend

---

# ⚠️ Common Mistakes

## 1. Forgetting `return`

Bad:

```python
def wrapper(*args, **kwargs):
    function(*args, **kwargs)
```

Correct:

```python
def wrapper(*args, **kwargs):
    return function(*args, **kwargs)
```

---

## 2. Not Using `*args` and `**kwargs`

A decorator that only accepts:

```python
def wrapper():
```

will only work with functions requiring no arguments.

For reusable decorators:

```python
def wrapper(*args, **kwargs):
```

is usually safer.

---

## 3. Forgetting `functools.wraps`

Bad:

```python
def decorator(function):

    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper
```

Better:

```python
from functools import wraps


def decorator(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper
```

---

## 4. Too Much Logic in Decorators

Decorators should generally focus on a specific cross-cutting concern.

Avoid creating decorators that perform many unrelated tasks.

---

## 5. Excessive Nesting

Complex decorator chains can make debugging difficult.

```python
@A
@B
@C
@D
def function():
    pass
```

Use multiple decorators when they improve structure, not simply because they are possible.

---

# 🚦 When Should You Use Decorators?

Decorators are a good choice when behavior needs to be applied consistently across multiple functions or methods.

Good use cases:

```text
✓ Logging
✓ Authentication
✓ Authorization
✓ Validation
✓ Timing
✓ Caching
✓ Retry logic
✓ Transactions
✓ Monitoring
✓ Rate limiting
✓ Permission checks
```

---

# 🚫 When Should You Avoid Decorators?

Avoid decorators when:

* The behavior is only needed once
* The decorator makes code harder to understand
* Debugging becomes unnecessarily difficult
* A simple helper function would be clearer
* The decorator hides important business logic

### Rule

> **Use decorators to simplify repeated behavior, not to make simple code look complicated.**

---

# 🧪 Practice Exercises

## 🟢 Beginner

1. Create a decorator that prints `"Hello"` before a function.
2. Create a decorator that prints `"Goodbye"` after a function.
3. Create a logging decorator.
4. Create a decorator that counts function calls.
5. Create a decorator that prints the function name.
6. Create a decorator that prints `"START"` and `"END"`.

---

## 🟡 Intermediate

7. Create a decorator supporting `*args`.
8. Create a decorator supporting `**kwargs`.
9. Create a decorator that measures execution time.
10. Create a validation decorator.
11. Create an authentication decorator.
12. Create two decorators and test their order.
13. Use `functools.wraps`.
14. Create a decorator that modifies the return value.

---

## 🔴 Advanced

15. Create a parameterized decorator.
16. Create a retry decorator.
17. Create a caching decorator.
18. Create a rate-limiting decorator.
19. Create a permission decorator.
20. Create a decorator for exception handling.
21. Create a class decorator.
22. Create a stateful decorator.
23. Build a decorator pipeline.
24. Combine three decorators safely.

---

# 🚀 Mini Project 1 — Function Logger

Build a reusable logging system.

Requirements:

```python
@log_function
def add(a, b):
    return a + b
```

Expected behavior:

```text
Calling add
Arguments: 10, 20
Result: 30
Completed add
```

Use:

* `*args`
* `**kwargs`
* `functools.wraps`

---

# 🚀 Mini Project 2 — Authentication System

Create:

```python
@login_required
def dashboard(user):
    ...
```

The decorator should:

1. Check authentication.
2. Reject unauthenticated users.
3. Allow authenticated users.
4. Preserve function metadata.

---

# 🚀 Mini Project 3 — Performance Monitor

Create:

```python
@performance_monitor
def process_data():
    ...
```

The decorator should display:

```text
Function: process_data
Execution Time: 0.1234 seconds
```

Use:

```python
time.perf_counter()
```

---

# 🚀 Mini Project 4 — Retry Framework

Build:

```python
@retry(attempts=3)
def api_request():
    ...
```

Requirements:

* Retry failed operations
* Stop after maximum attempts
* Preserve the original exception
* Allow configurable attempts
* Use `functools.wraps`

---

# 💼 Interview Questions

### Beginner

1. What is a decorator?
2. Why are decorators used?
3. What does the `@` symbol mean?
4. What are first-class functions?
5. What is a higher-order function?
6. What is a nested function?
7. What is a closure?
8. Why are closures useful for decorators?

### Intermediate

9. How does a decorator work internally?
10. What is the difference between a decorator and a wrapper?
11. Why should decorators use `*args` and `**kwargs`?
12. Why is `functools.wraps` important?
13. Can a function have multiple decorators?
14. What is decorator execution order?
15. Can decorators accept arguments?
16. What is a decorator factory?
17. Can methods be decorated?
18. Can classes be decorated?

### Advanced

19. Explain the relationship between decorators and closures.
20. How do stateful decorators work?
21. How would you create a retry decorator?
22. How would you implement a caching decorator?
23. How can decorators affect debugging?
24. How can decorators affect function metadata?
25. What are cross-cutting concerns?
26. How can decorators support separation of concerns?
27. What are the disadvantages of decorators?
28. How do multiple decorators compose?
29. Explain:

```python
@A
@B
def function():
    pass
```

Answer:

```python
function = A(B(function))
```

---

# 🧠 Deep Concept — The Decorator Mental Model

A powerful way to understand decorators is:

```text
                    ORIGINAL FUNCTION
                           │
                           ▼
                     decorator()
                           │
                           ▼
                    wrapper function
                           │
                 ┌─────────┴─────────┐
                 │                   │
                 ▼                   ▼
        Additional Logic      Original Function
                 │                   │
                 └─────────┬─────────┘
                           ▼
                     Final Result
```

The decorator does not necessarily modify the original function's source code.

Instead, it commonly creates another callable that controls access to the original function.

---

# 📌 Decorator Formula

Remember this pattern:

```python
def decorator(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        # Before
        ...

        result = function(*args, **kwargs)

        # After
        ...

        return result

    return wrapper
```

This pattern covers a huge percentage of practical decorators.

---

# ⚡ Quick Revision

### Function as Object

```python
function = greet
```

### Pass Function

```python
execute(greet)
```

### Return Function

```python
return inner
```

### Decorator

```python
def decorator(function):
    ...
    return wrapper
```

### Decorator Syntax

```python
@decorator
def function():
    pass
```

Equivalent to:

```python
function = decorator(function)
```

### Generic Wrapper

```python
def wrapper(*args, **kwargs):
    return function(*args, **kwargs)
```

### Preserve Metadata

```python
from functools import wraps
```

```python
@wraps(function)
```

### Multiple Decorators

```python
@A
@B
def function():
    pass
```

Equivalent to:

```python
function = A(B(function))
```

### Decorator Factory

```python
@decorator(config)
def function():
    pass
```

---

# 🏆 Four Levels of Decorator Understanding

## Level 1 — Beginner

Understand:

```python
@decorator
```

and:

```python
function = decorator(function)
```

---

## Level 2 — Intermediate

Understand:

```python
*args
**kwargs
functools.wraps
multiple decorators
```

---

## Level 3 — Advanced

Understand:

```text
Closures
Decorator factories
Stateful decorators
Class decorators
Method decorators
```

---

## Level 4 — Professional

Use decorators for:

```text
Authentication
Authorization
Caching
Monitoring
Logging
Validation
Retry systems
Transactions
Rate limiting
Framework design
```

---

# 🧠 Key Takeaways

> **Decorators allow behavior to be added to functions or classes without changing their core implementation.**

> **Python decorators are built on first-class functions, higher-order functions, nested functions, and closures.**

> **The `@decorator` syntax is syntactic sugar for function reassignment.**

> **A wrapper function usually handles the additional behavior.**

> **`*args` and `**kwargs` make decorators flexible.**

> **`functools.wraps` preserves important function metadata.**

> **Multiple decorators are applied from the bottom upward.**

> **Parameterized decorators are commonly implemented using decorator factories.**

> **Decorators are especially useful for cross-cutting concerns such as logging, authentication, caching, validation, and monitoring.**

---

# ✅ Best Practices

* Keep decorators focused on one responsibility.
* Use `functools.wraps`.
* Support `*args` and `**kwargs` for reusable decorators.
* Preserve the wrapped function's return value.
* Preserve exceptions unless intentionally handling them.
* Keep decorator names descriptive.
* Avoid unnecessarily complex decorator chains.
* Document decorators that have non-obvious behavior.
* Be careful with stateful decorators.
* Test decorated functions independently.
* Consider readability before adding a decorator.
* Use built-in decorators when they already solve the problem.

---

# 📖 References

* [Python Documentation — functools](https://docs.python.org/3/library/functools.html?utm_source=chatgpt.com)
* [Python Documentation — Function Definitions](https://docs.python.org/3/reference/compound_stmts.html?utm_source=chatgpt.com#function-definitions)
* [Python Documentation — Classes](https://docs.python.org/3/tutorial/classes.html?utm_source=chatgpt.com)
* [Python Documentation — `property`](https://docs.python.org/3/library/functions.html?utm_source=chatgpt.com#property)
* [Python Documentation — `staticmethod`](https://docs.python.org/3/library/functions.html?utm_source=chatgpt.com#staticmethod)
* [Python Documentation — `classmethod`](https://docs.python.org/3/library/functions.html?utm_source=chatgpt.com#classmethod)

---

# ⏭️ Next Topic

Continue your Python journey with:

## **17 — Context Managers**

You will learn:

* `with` statement
* Context manager protocol
* `__enter__()`
* `__exit__()`
* Resource management
* Custom context managers
* `contextlib`
* `@contextmanager`
* Exception handling in context managers
* File and database resource management
* Advanced context-manager patterns

---

<div align="center">

# 🐍 Keep Building. Keep Learning. Keep Coding.

### Python Programming — Beginner → Advanced

**Master the concepts. Build projects. Write production-quality Python.**

</div>
