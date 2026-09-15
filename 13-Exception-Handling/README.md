# ⚠️ 13 — Exception Handling

> **Learn how to detect, handle, and recover from runtime errors gracefully in Python.**

Exception Handling is an essential part of writing **robust, reliable, and production-ready Python applications**.

Programs can fail because of invalid user input, missing files, incorrect data, network failures, database problems, or unexpected conditions.

Python provides `try`, `except`, `else`, `finally`, and `raise` to handle these situations gracefully.

---

## 🎯 Learning Objectives

By the end of this chapter, you will understand:

* What are errors and exceptions?
* Syntax errors vs runtime errors
* What is an exception?
* `try` block
* `except` block
* Handling specific exceptions
* Multiple `except` blocks
* `else` block
* `finally` block
* `raise`
* Custom exceptions
* Exception hierarchy
* Exception chaining
* `assert`
* Best practices
* Real-world exception handling
* Debugging and defensive programming

---

# 🧠 1. What is an Error?

An **error** is a problem that prevents a program from behaving as expected.

Python errors can broadly be divided into:

```text
Errors
│
├── Syntax Errors
│
└── Exceptions
```

---

# ❌ 2. Syntax Error

A syntax error occurs when Python cannot understand the code because it violates Python's syntax rules.

Example:

```python
if True
    print("Hello")
```

Python raises:

```text
SyntaxError
```

Correct version:

```python
if True:
    print("Hello")
```

Syntax errors must generally be fixed in the source code before the program can run successfully.

---

# 💥 3. What is an Exception?

An **exception** is an event that occurs during program execution that interrupts the normal flow of the program.

Example:

```python
number = 10
result = number / 0
```

Python raises:

```text
ZeroDivisionError
```

Another example:

```python
number = int("hello")
```

Raises:

```text
ValueError
```

---

# 🆚 4. Error vs Exception

| Concept      | Description                               |
| ------------ | ----------------------------------------- |
| Syntax Error | Invalid Python syntax                     |
| Exception    | Problem occurring during execution        |
| Handling     | Recovering from expected runtime problems |
| Debugging    | Finding and fixing the underlying problem |

Simple idea:

```text
Syntax Error
    ↓
Fix the code

Exception
    ↓
Handle / recover / propagate appropriately
```

---

# 🛡️ 5. `try` and `except`

The basic exception-handling structure is:

```python
try:
    # Code that may raise an exception
except:
    # Code that handles the exception
```

Example:

```python
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input")
```

If the user enters:

```text
abc
```

The program doesn't immediately terminate with an unhandled exception.

---

# 🎯 6. Catch Specific Exceptions

Avoid catching every exception unnecessarily.

Instead of:

```python
try:
    number = int(input("Enter number: "))
except:
    print("Something went wrong")
```

Prefer:

```python
try:
    number = int(input("Enter number: "))
except ValueError:
    print("Please enter a valid number.")
```

This makes the program's behavior more predictable.

---

# ➗ 7. Handling `ZeroDivisionError`

```python
try:
    a = 10
    b = 0

    result = a / b

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Output:

```text
Cannot divide by zero.
```

---

# 📦 8. Handling Multiple Exceptions

You can handle different exceptions separately:

```python
try:
    number = int(input("Enter number: "))
    result = 100 / number

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

This is better than using one generic handler because each problem can receive an appropriate response.

---

# 🔗 9. Handling Multiple Exceptions Together

If multiple exceptions require the same handling logic:

```python
try:
    number = int(input("Enter number: "))
except (ValueError, TypeError):
    print("Invalid input.")
```

---

# 📝 10. Exception Object

You can store the exception in a variable using `as`.

```python
try:
    number = int("Python")

except ValueError as error:
    print("Error:", error)
```

Example output:

```text
Error: invalid literal for int() with base 10: 'Python'
```

This is useful for logging or debugging.

---

# 🧩 11. `else` Block

The `else` block executes **only when no exception occurs**.

Syntax:

```python
try:
    # Risky code

except:
    # Error handling

else:
    # Runs if no exception
```

Example:

```python
try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid input.")

else:
    print("You entered:", number)
```

Flow:

```text
             ┌── Exception ──→ except
try ─────────┤
             └── No exception ──→ else
```

---

# 🧹 12. `finally` Block

The `finally` block executes whether an exception occurs or not.

Syntax:

```python
try:
    # Code

except:
    # Handle exception

finally:
    # Always execute
```

Example:

```python
try:
    number = int("10")

except ValueError:
    print("Invalid input.")

finally:
    print("Execution completed.")
```

Output:

```text
Execution completed.
```

`finally` is especially useful for cleanup operations.

---

# 🔄 13. Complete Exception Handling Structure

Python supports:

```python
try:
    # Risky code

except SomeException:
    # Handle exception

else:
    # Runs when no exception occurs

finally:
    # Always runs
```

Example:

```python
try:
    number = int(input("Enter number: "))
    result = 100 / number

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Number cannot be zero.")

else:
    print("Result:", result)

finally:
    print("Program finished.")
```

---

# 🚨 14. `raise`

The `raise` statement allows you to explicitly raise an exception.

Example:

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")
```

Output:

```text
ValueError: Age cannot be negative.
```

---

# 🔐 15. Input Validation with `raise`

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age must be positive.")

    return age


print(set_age(25))
```

Invalid input:

```python
print(set_age(-10))
```

raises:

```text
ValueError
```

This is useful for enforcing business rules.

---

# 🧱 16. Custom Exceptions

Python allows you to create your own exception classes.

Example:

```python
class InsufficientBalanceError(Exception):
    pass
```

Use it:

```python
balance = 1000
withdraw = 1500

if withdraw > balance:
    raise InsufficientBalanceError("Insufficient balance.")
```

Custom exceptions make application-specific failures clearer.

---

# 💳 17. Real-World Custom Exception Example

```python
class InsufficientBalanceError(Exception):
    pass


class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):

        if amount > self.balance:
            raise InsufficientBalanceError(
                "Insufficient balance."
            )

        self.balance -= amount
        return self.balance


account = BankAccount(5000)

try:
    account.withdraw(6000)

except InsufficientBalanceError as error:
    print(error)
```

Output:

```text
Insufficient balance.
```

---

# 🌳 18. Exception Hierarchy

Python exceptions are organized into a class hierarchy.

Simplified:

```text
BaseException
│
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
│
└── Exception
    │
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   └── OverflowError
    │
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    │
    ├── TypeError
    ├── ValueError
    ├── OSError
    └── RuntimeError
```

Most application-level exceptions inherit from:

```python
Exception
```

---

# 🔍 19. Common Built-in Exceptions

| Exception             | Common Cause             |
| --------------------- | ------------------------ |
| `ValueError`          | Invalid value            |
| `TypeError`           | Invalid operation/type   |
| `ZeroDivisionError`   | Division by zero         |
| `IndexError`          | Invalid sequence index   |
| `KeyError`            | Missing dictionary key   |
| `FileNotFoundError`   | File doesn't exist       |
| `PermissionError`     | Insufficient permissions |
| `NameError`           | Unknown variable         |
| `AttributeError`      | Missing attribute        |
| `ImportError`         | Import failure           |
| `ModuleNotFoundError` | Module not found         |
| `OverflowError`       | Numeric result too large |
| `RuntimeError`        | Generic runtime problem  |

---

# 📚 20. `KeyError`

A `KeyError` occurs when a dictionary key doesn't exist.

```python
user = {
    "name": "Kishor",
    "age": 25
}

print(user["email"])
```

Raises:

```text
KeyError
```

Handle it:

```python
try:
    print(user["email"])

except KeyError:
    print("Email key not found.")
```

Or use:

```python
print(user.get("email"))
```

when returning `None` for a missing key is appropriate.

---

# 📋 21. `IndexError`

Occurs when accessing an invalid sequence index.

```python
numbers = [10, 20, 30]

print(numbers[10])
```

Handle it:

```python
try:
    print(numbers[10])

except IndexError:
    print("Index out of range.")
```

---

# 🔤 22. `TypeError`

Occurs when an operation is applied to an inappropriate type.

```python
result = "10" + 5
```

Raises:

```text
TypeError
```

Example handling:

```python
try:
    result = "10" + 5

except TypeError:
    print("Invalid data types.")
```

---

# 📁 23. File Exceptions

File operations commonly raise:

```text
FileNotFoundError
PermissionError
IsADirectoryError
NotADirectoryError
```

Example:

```python
try:
    with open("data.txt", "r", encoding="utf-8") as file:
        data = file.read()

except FileNotFoundError:
    print("File not found.")
```

---

# 🌐 24. Network Exception Example

When working with external services, network operations can fail.

Conceptually:

```python
try:
    # Network operation

except TimeoutError:
    print("Request timed out.")

except ConnectionError:
    print("Connection failed.")
```

The exact exceptions depend on the library being used.

---

# 🪵 25. Exception Handling + Logging

Production applications should generally **log useful diagnostic information** rather than simply printing errors.

Example:

```python
import logging

logging.basicConfig(level=logging.ERROR)

try:
    result = 10 / 0

except ZeroDivisionError:
    logging.exception("Calculation failed.")
```

`logging.exception()` records the error together with traceback information when called inside an exception handler.

---

# 🔗 26. Exception Chaining

Python allows one exception to be raised while preserving the original exception context.

Example:

```python
try:
    number = int("Python")

except ValueError as error:
    raise RuntimeError("Failed to process input.") from error
```

The `from` syntax explicitly connects the new exception to the original one.

Conceptually:

```text
Original Exception
       ↓
    ValueError
       ↓
   raise ... from
       ↓
   RuntimeError
```

This is useful when translating low-level errors into application-level exceptions.

---

# 🧪 27. Assertions

Python provides `assert` for checking assumptions during development.

```python
age = 20

assert age >= 0
```

With a message:

```python
age = -1

assert age >= 0, "Age cannot be negative."
```

Assertions are primarily for **internal correctness checks**, not for validating untrusted user input.

---

# 🚫 28. Avoid Bare `except`

Avoid:

```python
try:
    risky_operation()

except:
    print("Error")
```

A bare `except` can catch exceptions such as `KeyboardInterrupt` and `SystemExit`, which often should not be intercepted by ordinary application error handling.

Prefer:

```python
try:
    risky_operation()

except ValueError:
    print("Invalid value.")
```

Or, when you genuinely need a broad application-level fallback:

```python
try:
    risky_operation()

except Exception as error:
    print("Unexpected error:", error)
```

---

# 🎯 29. Don't Hide Errors

Avoid code like:

```python
try:
    process_data()

except Exception:
    pass
```

This silently ignores failures and makes debugging extremely difficult.

Better:

```python
try:
    process_data()

except Exception as error:
    print("Processing failed:", error)
```

In production, use appropriate logging and recovery behavior.

---

# 🔄 30. Exception Handling Flow

Understand this execution model:

```text
             ┌── Exception ──→ except
             │
try ─────────┤
             │
             └── No Exception ──→ else
                                      │
                                      ↓
                                  finally
```

If an exception isn't handled:

```text
try
 ↓
Exception
 ↓
No matching except
 ↓
Exception propagates
 ↓
Program / caller handles it
```

---

# 🏗️ 31. Real-World Example — User Registration

```python
class InvalidAgeError(Exception):
    pass


def register_user(name, age):

    if not name.strip():
        raise ValueError("Name cannot be empty.")

    if age < 18:
        raise InvalidAgeError(
            "User must be at least 18 years old."
        )

    return "Registration successful."


try:
    name = input("Enter name: ")
    age = int(input("Enter age: "))

    print(register_user(name, age))

except ValueError:
    print("Please enter valid information.")

except InvalidAgeError as error:
    print(error)
```

This combines:

```text
Input
  +
Validation
  +
Custom Exceptions
  +
Exception Handling
```

---

# 💼 32. Real-World Example — Safe Division

```python
def divide(a, b):

    if b == 0:
        raise ZeroDivisionError(
            "Denominator cannot be zero."
        )

    return a / b


try:
    result = divide(100, 0)
    print(result)

except ZeroDivisionError as error:
    print("Error:", error)
```

---

# 🧠 33. Best Practices

### ✅ Catch specific exceptions

```python
except ValueError:
```

instead of:

```python
except:
```

### ✅ Keep `try` blocks small

Prefer:

```python
try:
    number = int(value)

except ValueError:
    ...
```

rather than wrapping a large section of unrelated code.

### ✅ Don't use exceptions for ordinary control flow

Use normal conditions when they naturally express the logic.

### ✅ Provide useful error messages

```python
raise ValueError("Age must be greater than or equal to 18.")
```

### ✅ Clean up resources

Use:

```python
with open(...):
```

for files and context managers for other resources.

### ✅ Log unexpected failures

Use the `logging` module in production applications.

### ✅ Preserve the original cause

Use:

```python
raise NewError("...") from error
```

when translating exceptions.

---

# 🧪 34. Practice Exercises

## 🟢 Beginner

1. Handle `ZeroDivisionError`.
2. Handle invalid integer input.
3. Handle `IndexError`.
4. Handle `KeyError`.
5. Handle `FileNotFoundError`.
6. Write a program using `try` and `except`.
7. Practice `else` and `finally`.

---

## 🟡 Intermediate

8. Build a safe calculator.
9. Create a validated age-input program.
10. Build a file reader with exception handling.
11. Create a JSON reader that handles invalid/missing files.
12. Handle multiple exceptions.
13. Add logging to an application.
14. Practice `raise`.

---

## 🔴 Advanced

15. Create custom exception classes.
16. Build a Bank Account application.
17. Build a Student Management System with validation.
18. Build a robust Notes Manager.
19. Implement exception chaining.
20. Design an application-level exception hierarchy.
21. Build a command-line application with centralized error handling.

---

# 🏆 35. Mini Project — Bank Account

### Requirements

Create:

```text
bank_account/
├── main.py
├── account.py
└── exceptions.py
```

### Custom Exceptions

```python
class InsufficientBalanceError(Exception):
    pass


class InvalidAmountError(Exception):
    pass
```

### Expected Features

```text
Create Account
      ↓
Deposit
      ↓
Withdraw
      ↓
Validate Amount
      ↓
Handle Exceptions
      ↓
Display Balance
```

Example:

```python
try:
    account.withdraw(5000)

except InsufficientBalanceError as error:
    print(error)

except InvalidAmountError as error:
    print(error)
```

---

# 💬 36. Interview Questions

### Basic

**Q1. What is an exception?**

An event raised during execution that disrupts the normal flow of a program.

**Q2. What is exception handling?**

A mechanism for detecting and responding to exceptions.

**Q3. What is the purpose of `try`?**

To contain code that may raise an exception.

**Q4. What is `except`?**

It defines how matching exceptions should be handled.

**Q5. What is `finally`?**

A block that runs whether an exception occurs or not.

---

### Intermediate

**Q6. What is the difference between `else` and `finally`?**

```text
else    → runs when try succeeds
finally → runs regardless of success/failure
```

**Q7. What does `raise` do?**

Explicitly raises an exception.

**Q8. What is a custom exception?**

An application-specific exception class created by inheriting from an exception type, commonly `Exception`.

**Q9. What is exception chaining?**

Preserving the relationship between an original exception and a newly raised exception.

**Q10. Why should bare `except` usually be avoided?**

It can catch exceptions that should normally propagate, including interruption and exit exceptions.

---

### Advanced

**Q11. What is the difference between `Exception` and `BaseException`?**

`Exception` is the usual base class for application-level exceptions; `BaseException` is the broader root class and also includes exceptions such as `SystemExit` and `KeyboardInterrupt`.

**Q12. When should you use `assert`?**

For internal development-time assumptions and invariants, not normal user-input validation.

**Q13. Why keep `try` blocks small?**

To ensure only the operations intended to be handled are caught and to avoid accidentally masking unrelated failures.

**Q14. How can you preserve the original exception when raising another exception?**

Use exception chaining:

```python
raise RuntimeError("Operation failed") from error
```

---

# 📌 37. Quick Revision

```text
EXCEPTION HANDLING
│
├── SyntaxError
│
├── Exceptions
│   ├── ValueError
│   ├── TypeError
│   ├── IndexError
│   ├── KeyError
│   ├── ZeroDivisionError
│   └── FileNotFoundError
│
├── try
│
├── except
│
├── else
│
├── finally
│
├── raise
│
├── Custom Exceptions
│
├── Exception Hierarchy
│
├── Exception Chaining
│
├── assert
│
└── logging
```

---

# 🧭 38. Exception Handling Pattern

A production-oriented pattern often looks like:

```python
try:
    result = perform_operation()

except SpecificError as error:
    handle_expected_error(error)

else:
    process_success(result)

finally:
    cleanup()
```

Remember:

> **Catch exceptions you can meaningfully handle. Let unexpected exceptions propagate or be handled at an appropriate higher level.**

---

# 📚 Official References

* [Python Tutorial — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
* [Python Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
* [Python `raise` Statement](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement)
* [Python Logging](https://docs.python.org/3/library/logging.html)
* [Python Assertions](https://docs.python.org/3/reference/simple_stmts.html#assert)

---

# 🎯 Key Takeaway

> **Good exception handling doesn't mean hiding errors. It means handling expected failures clearly, preserving useful diagnostic information, and allowing unexpected failures to surface appropriately.**

Master this pattern:

```text
try
 ↓
Perform risky operation
 ↓
except
 ↓
Handle expected failure
 ↓
else
 ↓
Handle success
 ↓
finally
 ↓
Cleanup
```

Then learn to build your own:

```text
Built-in Exceptions
        ↓
Custom Exceptions
        ↓
Validation
        ↓
Logging
        ↓
Exception Chaining
        ↓
Robust Applications
```

---

## ⏭️ Next Topic

➡️ **[14 — Object-Oriented Programming](../14-Object-Oriented-Programming/)**

Continue your Python journey:

```text
11. Modules & Packages
          ↓
12. File Handling
          ↓
13. Exception Handling
          ↓
14. Object-Oriented Programming
          ↓
15. Advanced Python
```

---

⭐ **Keep coding. Keep debugging. Keep building.**
