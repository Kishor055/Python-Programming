 # 🐍 Python Operators Masterclass

 A practical and developer-focused guide to **Python operators**, covering syntax, behavior, examples, precedence, associativity, and real-world usage.

 > **Level:** Beginner → Intermediate\
>  **File:** `07_operators.py`\
>  **Language:** Python 3.x

---

<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/1dfd6068-d85c-4b88-b56d-11f632e2e739" />

---

 ## 📌 Overview

 Operators are special symbols or keywords used to perform operations on values, variables, and expressions.

 ### Basic Example

```
a = 10
b = 5

result = a + b

print(result)
```

 **Output:**

```
15
```

 ### Core Terminology

 | Term | Description | Example |
| --- | --- | --- |
| **Operator** | Symbol or keyword that performs an operation | `+` |
| **Operand** | Value or variable used by an operator | `a`, `b` |
| **Expression** | Combination of operands and operators | `a + b` |

---

 # 🧩 Types of Python Operators

 Python provides several categories of operators:

 | # | Category | Purpose |
| --- | --- | --- |
| 1 | **Arithmetic** | Mathematical calculations |
| 2 | **Comparison** | Compare values |
| 3 | **Logical** | Combine or modify conditions |
| 4 | **Bitwise** | Perform operations on binary bits |
| 5 | **Assignment** | Assign and update values |
| 6 | **Identity** | Check object identity |
| 7 | **Membership** | Check whether a value exists in a collection |
| 8 | **Conditional / Ternary** | Write simple conditional expressions |

---

 # 1\. Arithmetic Operators

 Arithmetic operators perform mathematical operations on numeric values.

 ### Example

```
a = 15
b = 4

print(a + b)    # Addition
print(a - b)    # Subtraction
print(a * b)    # Multiplication
print(a / b)    # Division
print(a // b)   # Floor division
print(a % b)    # Modulus
print(a ** b)   # Exponentiation
```

 ### Operator Reference

 | Operator | Operation | Example | Result |
| --- | --- | --- | --- |
| `+` | Addition | `15 + 4` | `19` |
| `-` | Subtraction | `15 - 4` | `11` |
| `*` | Multiplication | `15 * 4` | `60` |
| `/` | Division | `15 / 4` | `3.75` |
| `//` | Floor Division | `15 // 4` | `3` |
| `%` | Modulus | `15 % 4` | `3` |
| `**` | Exponentiation | `15 ** 4` | `50625` |

 ### `/` vs `//`

```
print(4 / 2)
print(4 // 2)
```

 **Output:**

```
2.0
2
```

 - `/` performs true division and returns a `float`.
- `//` performs floor division.

 > **Note:** With negative numbers, floor division rounds toward negative infinity rather than simply truncating the decimal portion.

---

 # 2\. Comparison Operators

 Comparison operators compare two values and return a Boolean result:

```
True
False
```

 ### Example

```
a = 13
b = 33

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= b)   # False
print(a <= b)   # True
```

 ### Operator Reference

 | Operator | Meaning | Example | Result |
| --- | --- | --- | --- |
| `==` | Equal to | `13 == 33` | `False` |
| `!=` | Not equal to | `13 != 33` | `True` |
| `>` | Greater than | `13 > 33` | `False` |
| `<` | Less than | `13 < 33` | `True` |
| `>=` | Greater than or equal to | `13 >= 33` | `False` |
| `<=` | Less than or equal to | `13 <= 33` | `True` |

 ### Practical Example

```
age = 21

if age >= 18:
    print("Adult")
```

 **Output:**

```
Adult
```

---

 # 3\. Logical Operators

 Logical operators combine or modify Boolean expressions.

 ### Example

```
age = 25
has_id = True

print(age >= 18 and has_id)
print(age < 18 or has_id)
print(not has_id)
```

 **Output:**

```
True
True
False
```

 ### Operator Reference

 | Operator | Description |
| --- | --- |
| `and` | True when both operands are truthy |
| `or` | True when at least one operand is truthy |
| `not` | Reverses the truth value |

 ### Logical Precedence

```
not
 ↓
and
 ↓
or
```

 Example:

```
result = not False and True

print(result)
```

 Python evaluates this as:

```
(not False) and True
```

 **Output:**

```
True
```

 > **Important:** `and` and `or` can return operands rather than strictly `True` or `False`. They use short-circuit evaluation.

 Example:

```
name = ""

result = name or "Guest"

print(result)
```

 **Output:**

```
Guest
```

---

 # 4\. Bitwise Operators

 Bitwise operators operate on the binary representation of integers.

 ### Example

```
a = 10
b = 4

print(a & b)    # AND
print(a | b)    # OR
print(a ^ b)    # XOR
print(~a)       # NOT
print(a << 2)   # Left shift
print(a >> 2)   # Right shift
```

 ### Operator Reference

 | Operator | Operation | Description |
| --- | --- | --- |
| `&` | Bitwise AND | Sets a bit to `1` when both bits are `1` |
| `\|` | Bitwise OR | Sets a bit to `1` when either bit is `1` |
| `^` | Bitwise XOR | Sets a bit to `1` when the bits are different |
| `~` | Bitwise NOT | Inverts the bits |
| `<<` | Left Shift | Shifts bits to the left |
| `>>` | Right Shift | Shifts bits to the right |

 ### Binary Example

```
10 = 1010
 4 = 0100
```

 Bitwise AND:

```
  1010
& 0100
------
  0000
```

 Therefore:

```
10 & 4
```

 returns:

```
0
```

 ### Bitwise NOT

 Python integers use signed integer semantics, so:

```
print(~10)
```

 produces:

```
-11
```

 This follows the identity:

```
~x == -x - 1
```

---

 # 5\. Assignment Operators

 Assignment operators assign values to variables.

 ### Basic Assignment

```
x = 10
```

 ### Compound Assignment

```
x = 10

x += 5
print(x)    # 15

x -= 3
print(x)    # 12

x *= 2
print(x)    # 24

x /= 4
print(x)    # 6.0
```

 ### Operator Reference

 | Operator | Example | Equivalent |
| --- | --- | --- |
| `=` | `x = 10` | Assign value |
| `+=` | `x += 5` | `x = x + 5` |
| `-=` | `x -= 5` | `x = x - 5` |
| `*=` | `x *= 5` | `x = x * 5` |
| `/=` | `x /= 5` | `x = x / 5` |
| `//=` | `x //= 5` | `x = x // 5` |
| `%=` | `x %= 5` | `x = x % 5` |
| `**=` | `x **= 5` | `x = x ** 5` |
| `&=` | `x &= 5` | `x = x & 5` |
| `\|=` | `x \|= 5` | `x = x \| 5` |
| `^=` | `x ^= 5` | `x = x ^ 5` |
| `<<=` | `x <<= 5` | `x = x << 5` |
| `>>=` | `x >>= 5` | `x = x >> 5` |

---

 # 6\. Identity Operators

 Identity operators determine whether two expressions refer to the **same object**.

 Python provides:

```
is
is not
```

 ### Example

```
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)       # True
print(a is c)       # False
print(a is not c)   # True
```

 Here:

```
a ─────┐
       ├──> [1, 2, 3]
b ─────┘

c ─────────> [1, 2, 3]
```

 `a` and `b` reference the same object, while `c` references a different object.

 ### Operator Reference

 | Operator | Meaning |
| --- | --- |
| `is` | Both references point to the same object |
| `is not` | References point to different objects |

---

 ## `is` vs `==`

 This is one of the most important distinctions in Python.

```
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

 **Output:**

```
True
False
```

 ### Difference

 | Operator | Checks |
| --- | --- |
| `==` | Value / equality |
| `is` | Object identity |

 ### Best Practice

 Use `is` when checking for `None`:

```
if value is None:
    print("No value provided")
```

 Do **not** normally replace:

```
if value == None:
```

 with identity checks in reverse; prefer:

```
if value is None:
```

---

 # 7\. Membership Operators

 Membership operators determine whether a value exists in a collection or sequence.

 Python provides:

```
in
not in
```

 ### Example

```
languages = ["Python", "Java", "C++"]

print("Python" in languages)
print("JavaScript" not in languages)
```

 **Output:**

```
True
True
```

 ### Operator Reference

 | Operator | Meaning |
| --- | --- |
| `in` | Value exists in the collection |
| `not in` | Value does not exist in the collection |

 ### Practical Example

```
users = ["admin", "developer", "guest"]

username = "developer"

if username in users:
    print("User exists")
```

 **Output:**

```
User exists
```

 ### Membership with Strings

```
message = "Python is powerful"

print("Python" in message)
```

 **Output:**

```
True
```

---

 # 8\. Ternary Operator

 Python provides a concise conditional expression for simple `if-else` decisions.

 ### Syntax

```
value_if_true if condition else value_if_false
```

 ### Example

```
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)
```

 **Output:**

```
Adult
```

 ### Traditional Approach

```
if age >= 18:
    status = "Adult"
else:
    status = "Minor"
```

 ### Ternary Approach

```
status = "Adult" if age >= 18 else "Minor"
```

 > **Clean Code Tip:** Use conditional expressions when the logic remains easy to read. Avoid deeply nested ternary expressions.

---

 # ⚡ 9. Operator Precedence

 Operator precedence determines which operations are evaluated first when an expression contains multiple operators.

 ### Example

```
result = 10 + 20 * 3

print(result)
```

 **Output:**

```
70
```

 Because multiplication has higher precedence:

```
20 * 3 = 60
10 + 60 = 70
```

 ### Using Parentheses

 Parentheses can explicitly control evaluation order:

```
result = (10 + 20) * 3

print(result)
```

 **Output:**

```
90
```

---

 ## Operator Precedence — High to Low

 The following is a simplified practical hierarchy:

 | Priority | Operators / Constructs |
| --- | --- |
| 1 | `()` — grouping / calls / subscription syntax |
| 2 | `**` — exponentiation |
| 3 | `+x`, `-x`, `~x` — unary operators |
| 4 | `*`, `/`, `//`, `%` |
| 5 | `+`, `-` |
| 6 | `<<`, `>>` |
| 7 | `&` |
| 8 | `^` |
| 9 | `\|` |
| 10 | Comparisons, `in`, `not in`, `is`, `is not` |
| 11 | `not` |
| 12 | `and` |
| 13 | `or` |
| 14 | Conditional expression |
| 15 | `lambda` |
| 16 | Assignment expressions / assignment statements |

 > **Best Practice:** When an expression becomes difficult to read, use parentheses rather than relying entirely on precedence rules.

---

 # 🔄 10. Operator Associativity

 Associativity determines how operators with the same precedence are grouped.

 ### Left-to-Right

 Multiplication and division group from left to right.

```
result = 100 / 10 * 2

print(result)
```

 This is evaluated as:

```
(100 / 10) * 2
```

 **Output:**

```
20.0
```

 ### Right-to-Left

 Exponentiation groups from right to left.

```
result = 2 ** 3 ** 2

print(result)
```

 This is evaluated as:

```
2 ** (3 ** 2)
```

 Therefore:

```
2 ** 9 = 512
```

 **Output:**

```
512
```

---

 # 💻 11. Complete Integration Example

 The following example combines several Python operators into a small eligibility system.

```
# 07_operators.py

marks = 85
attendance = 90

allowed_roles = ["admin", "student", "teacher"]
user_role = "student"

# Comparison + Logical Operators
passed = marks >= 40 and attendance >= 75

# Membership Operator
role_valid = user_role in allowed_roles

# Identity Operator
system_status = None
is_ready = system_status is None

# Ternary / Conditional Expression
result_status = "PASS" if passed else "FAIL"

print("----- Execution Summary -----")
print("Marks:", marks)
print("Attendance:", attendance)
print("Role Allowed:", role_valid)
print("System Ready:", is_ready)
print("Passed Criteria:", passed)
print("Final Status:", result_status)
```

 ### Output

```
----- Execution Summary -----
Marks: 85
Attendance: 90
Role Allowed: True
System Ready: True
Passed Criteria: True
Final Status: PASS
```

---

 # 🧠 Quick Cheat Sheet

```
# Arithmetic
+   -   *   /   //   %   **

# Comparison
==   !=   >   <   >=   <=

# Logical
and   or   not

# Bitwise
&   |   ^   ~   <<   >>

# Assignment
=   +=   -=   *=   /=   //=   %=   **=
&=  |=   ^=   <<=  >>=

# Identity
is   is not

# Membership
in   not in

# Conditional Expression
value_if_true if condition else value_if_false
```

---

 # 📊 Operator Summary

 | Category | Operators | Primary Use |
| --- | --- | --- |
| Arithmetic | `+ - * / // % **` | Mathematical operations |
| Comparison | `== != > < >= <=` | Value comparison |
| Logical | `and or not` | Boolean logic |
| Bitwise | `& \| ^ ~ << >>` | Binary manipulation |
| Assignment | `= += -= *= /= //= %= **=` | Assignment and updates |
| Identity | `is is not` | Object identity |
| Membership | `in not in` | Collection membership |
| Conditional | `x if condition else y` | Simple conditional selection |

---

 # 📁 Project Structure

```
python-learning/
│
├── 01_variables.py
├── 02_comments.py
├── 03_data_types.py
├── 04_data_types.py
├── 05_input_output.py
├── 06_type_casting.py
├── 07_operators.py
│
└── README.md
```

---

 # 🎯 Learning Objectives

 After completing this topic, you should be able to:

 - Understand operators, operands, and expressions.
- Perform arithmetic calculations.
- Compare values using relational operators.
- Build conditions using logical operators.
- Perform bitwise operations on integers.
- Use assignment and compound assignment operators.
- Understand `is` vs `==`.
- Check membership using `in` and `not in`.
- Write simple conditional expressions.
- Understand operator precedence.
- Understand operator associativity.
- Write readable and maintainable Python expressions.

---

 # 🧪 Practice Challenges

 Strengthen your understanding with these exercises:

 ### Beginner

 1. Take two numbers and perform all arithmetic operations.
2. Check whether a number is positive, negative, or zero.
3. Check whether a number is even or odd.
4. Find the largest of two numbers.
5. Check whether a student has passed based on marks.

 ### Intermediate

 6. Create a program that validates both marks and attendance.
7. Check whether a username exists in a list.
8. Demonstrate the difference between `is` and `==`.
9. Perform AND, OR, XOR, and shift operations on integers.
10. Rewrite a simple `if-else` statement using a conditional expression.

 ### Challenge

 Evaluate the following expression manually before running it:

```
result = 10 + 5 * 2 ** 2 - 8 // 2
```

 Then verify your answer using Python.

---

 # ▶️ How to Run

 Check your Python version:

```
python --version
```

 Or:

```
python3 --version
```

 Run the program:

```
python 07_operators.py
```

 On systems using `python3`:

```
python3 07_operators.py
```

---

 # 📚 Reference

 This guide is based on the Python operator concepts covered by **GeeksforGeeks**.

 GeeksforGeeks — Python Operators

 For authoritative language-level behavior, consult the official Python documentation.

 Python Documentation — Expressions

---

 # ⭐ Key Takeaway

 Operators are the foundation of Python expressions and program logic.

```
Operators
    ↓
Expressions
    ↓
Conditions
    ↓
Loops
    ↓
Functions
    ↓
Algorithms
    ↓
Applications
```

 Understanding operators deeply helps you write code that is:

 - ✅ Correct
- ✅ Readable
- ✅ Predictable
- ✅ Efficient
- ✅ Maintainable

---

 ## 🚀 Keep Learning. Keep Building.

 **Python → Practice → Projects → Problem Solving → Mastery**

 🐍 **Happy Coding!**
