 # 🐍 Python Conditional Statements

 A practical and professional guide to **Conditional Statements in Python**, covering decision-making, syntax, execution flow, nested conditions, conditional expressions, and modern `match-case` pattern matching.

 > **Level:** Beginner → Intermediate\
>  **Language:** Python 3.x\
>  **Topic:** Control Flow / Decision Making

---

 ## 📌 Overview

 Conditional statements allow a Python program to **make decisions based on conditions**. 
 **Conditional statements are used to control the flow of execution in a program based on specific conditions. They allow programs to execute different blocks of code depending on whether a condition evaluates to True or False.**

 A condition is evaluated and produces a truth value:

```
True
False
```

 Based on the result, Python decides which block of code should execute.

 ### Basic Example

```
age = 20

if age >= 18:
    print("Eligible to vote.")
```

 **Output:**

```
Eligible to vote.
```

 The condition:

```
age >= 18
```

 evaluates to `True`, so Python executes the indented block.

---

 # 🧩 Why Conditional Statements?

 Conditional statements are fundamental to program logic.

 They are used for:

 - User authentication
- Permission checks
- Input validation
- Age verification
- Grade calculation
- Login systems
- Menu selection
- Error handling
- Business rules
- Game logic
- Application workflows

 ### General Flow

```
             Condition
                 │
          ┌──────┴──────┐
          │             │
        True          False
          │             │
          ▼             ▼
     Execute A      Execute B
```

---

 # 📚 Types of Conditional Statements

 Python provides several ways to implement conditional logic:

 | # | Statement | Purpose |
| --- | --- | --- |
| 1 | `if` | Execute code when a condition is true |
| 2 | Short-hand `if` | Write a simple `if` statement in one line |
| 3 | `if-else` | Choose between two alternatives |
| 4 | `if-elif-else` | Handle multiple conditions |
| 5 | Nested `if` | Place one condition inside another |
| 6 | Conditional Expression | Compact one-line `if-else` |
| 7 | `match-case` | Match a value against multiple patterns |

---

 # 1\. `if` Statement

 The `if` statement executes a block of code **only when its condition evaluates to `True`**.

---

<img width="800" height="297" alt="image" src="https://github.com/user-attachments/assets/f6d4c2ad-e19f-49f5-863f-dca9c354a0a1" />

---
 ## Syntax

```
if condition:
    statement
```

 Python uses **indentation** to define the block of code controlled by the `if` statement.

 ## Example

```
age = 20

if age >= 18:
    print("Eligible to vote.")
```

 **Output:**

```
Eligible to vote.
```

 ### Execution Flow

```
age >= 18
    │
    ▼
  True
    │
    ▼
Execute print()
```

 ### When the Condition Is False

```
age = 15

if age >= 18:
    print("Eligible to vote.")
```

 There is no output because the condition evaluates to `False`.

---

 # 2\. Short-Hand `if`

 A simple `if` statement can be written on a single line when only one statement needs to be executed.

 ## Syntax

```
if condition: statement
```

 ## Example

```
age = 19

if age >= 18: print("Eligible to vote.")
```

 **Output:**

```
Eligible to vote.
```

 ### Recommended Usage

 Short-hand `if` can be useful for very simple statements:

```
if debug: print("Debug mode enabled.")
```

 However, for complex logic, the normal multi-line form is more readable.

 ### Avoid Overusing It

 Instead of:

```
if user and user.is_active: print("Active")
```

 prefer:

```
if user and user.is_active:
    print("Active")
```

 when the condition becomes more complicated.

---

 # 3\. `if-else` Statement

 The `if-else` statement provides **two possible execution paths**.

 - If the condition is `True`, the `if` block executes.
- If the condition is `False`, the `else` block executes.

---

  <img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/337a876f-5854-48d7-8653-90d2941203c3" />

---

 ## Syntax

```
if condition:
    statement_if_true
else:
    statement_if_false
```

 ## Example

```
age = 10

if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")
```

 **Output:**

```
Travel for free.
```

 ### Execution Flow

```
              Condition
                  │
           ┌──────┴──────┐
           │             │
         True          False
           │             │
           ▼             ▼
      if block       else block
```

 ### Another Example

```
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

 **Output:**

```
Odd
```

---

 # 4\. `if-elif-else` Statement

 The `if-elif-else` structure is used when a program needs to evaluate **multiple conditions**.

 - `if` checks the first condition.
- `elif` checks additional conditions.
- `else` executes when all previous conditions are false.

---

<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/1ac65844-115a-4ca1-8aff-7a84700ed40f" />

---

<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/9751b63f-1530-46ff-94e0-f41ece596cf5" />

---

<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/012852cd-ef16-452c-9cd8-690264dc86d4" />

---

 ## Syntax

```
if condition1:
    statement1
elif condition2:
    statement2
elif condition3:
    statement3
else:
    statement4
```

 ## Example

```
age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")
```

 **Output:**

```
Young adult.
```

 ### Explanation

 For:

```
age = 25
```

 Python evaluates:

```
25 <= 12   → False
25 <= 19   → False
25 <= 35   → True
```

 Therefore:

```
Young adult.
```

 is printed.

 ### Execution Flow

```
              if condition
                   │
             ┌─────┴─────┐
           True         False
             │             │
             ▼             ▼
          Execute       elif condition
                          │
                    ┌─────┴─────┐
                  True         False
                    │             │
                    ▼             ▼
                 Execute       Next elif
                                  │
                                  ▼
                                else
```

 > **Important:** Python executes the **first matching branch** and then skips the remaining branches.

---

 # 5\. Multiple `elif` Conditions

 You can use multiple `elif` blocks when more conditions are required.

```
marks = 82

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"

print("Grade:", grade)
```

 **Output:**

```
Grade: A
```

 ### Best Practice

 Arrange conditions carefully from the **most restrictive/highest threshold to the lowest**, when that matches the logic of your problem.

---

 # 6\. Nested `if-else` Statement

 A nested conditional is an `if` statement placed inside another `if`, `elif`, or `else` block.

 Nested conditions are useful when a second decision depends on the first decision.

---

 <img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/03506f03-fb3f-4a4a-b63a-024ca2192e1b" />

---

 ## Example

```
age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")
```

 **Output:**

```
30% senior discount!
```

 ### Execution Flow

```
age >= 60
    │
    ├── False → Not eligible
    │
    └── True
         │
         ▼
    is_member
         │
    ┌────┴────┐
   True     False
    │          │
    ▼          ▼
  30%         20%
 discount    discount
```

 ### Another Example

```
username = "admin"
password = "python123"

if username == "admin":
    if password == "python123":
        print("Login successful.")
    else:
        print("Incorrect password.")
else:
    print("Unknown user.")
```

 **Output:**

```
Login successful.
```

 > **Clean Code Tip:** Deeply nested conditions can become difficult to maintain. When nesting becomes excessive, consider using guard clauses, helper functions, or combined conditions.

---

 # 7\. Conditional Expression

 A **conditional expression**, commonly called the **ternary operator**, provides a compact way to select between two values.

 ## Syntax

```
value_if_true if condition else value_if_false
```

 ## Example

```
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)
```

 **Output:**

```
Adult
```

 ### Equivalent `if-else`

 The conditional expression:

```
status = "Adult" if age >= 18 else "Minor"
```

 is equivalent to:

```
if age >= 18:
    status = "Adult"
else:
    status = "Minor"
```

 ### Another Example

```
number = 10

result = "Even" if number % 2 == 0 else "Odd"

print(result)
```

 **Output:**

```
Even
```

 ### Best Practice

 Use conditional expressions when the logic is simple and readable.

 ### Avoid

```
result = "A" if condition1 else "B" if condition2 else "C" if condition3 else "D"
```

 Complex nested conditional expressions reduce readability.

 Prefer a normal `if-elif-else` structure instead.

---

 # 8\. `match-case` Statement

 Python 3.10 introduced the `match-case` statement for **structural pattern matching**.

 It can be used when a program needs to compare a value against multiple patterns.

 It is conceptually similar to `switch-case` statements found in other programming languages, but Python's pattern matching is more powerful.

 ## Basic Syntax

```
match value:
    case pattern1:
        statement1
    case pattern2:
        statement2
    case _:
        default_statement
```

 ## Example

```
number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")
```

 **Output:**

```
Two or Three
```

 ### Explanation

 The value is:

```
number = 2
```

 Python checks each pattern:

```
case 1       → No match
case 2 | 3   → Match
```

 Therefore:

```
Two or Three
```

 is printed.

---

 # 9\. The Wildcard Pattern `_`

 The underscore:

```
_
```

 acts as a catch-all pattern in `match-case`.

 Example:

```
command = "delete"

match command:
    case "create":
        print("Creating...")
    case "update":
        print("Updating...")
    case "delete":
        print("Deleting...")
    case _:
        print("Unknown command.")
```

 **Output:**

```
Deleting...
```

 If the value does not match any previous case, `_` handles it.

---

 # 10\. Multiple Patterns in `match-case`

 The `|` operator can combine multiple patterns.

```
status_code = 200

match status_code:
    case 200 | 201:
        print("Success")
    case 400 | 404:
        print("Client error")
    case 500 | 502:
        print("Server error")
    case _:
        print("Unknown status")
```

 **Output:**

```
Success
```

 This is useful when several values should produce the same result.

---

 # 11\. `match-case` with Guards

 A `match` case can include an additional condition called a **guard**.

 ## Syntax

```
match value:
    case pattern if condition:
        statement
```

 ## Example

```
age = 25

match age:
    case age if age < 13:
        print("Child")
    case age if age < 20:
        print("Teenager")
    case age if age < 60:
        print("Adult")
    case _:
        print("Senior")
```

 **Output:**

```
Adult
```

 The `if` after the pattern acts as a guard.

---

 # 12\. `if-elif-else` vs `match-case`

 Both can implement decision-making, but they are useful in different situations.

 | Feature | `if-elif-else` | `match-case` |
| --- | --- | --- |
| General conditions | ✅ Excellent | ⚠️ Not always necessary |
| Range comparisons | ✅ Excellent | Possible with guards |
| Boolean expressions | ✅ Excellent | Possible |
| Exact value matching | ✅ Good | ✅ Excellent |
| Multiple patterns | Manual conditions | ✅ Built-in |
| Structural pattern matching | ❌ | ✅ |
| Python version | All modern Python | Python 3.10+ |
| General-purpose branching | ✅ | ✅ |

 ### Use `if-elif-else` for:

```
if age >= 18:
    ...
elif age >= 13:
    ...
else:
    ...
```

 ### Use `match-case` for:

```
match command:
    case "start":
        ...
    case "stop":
        ...
    case "pause":
        ...
```

---

 # 🧠 Truthy and Falsy Values

 Python conditions do not always need to explicitly compare values with `True` or `False`.

 Python evaluates objects according to their **truth value**.

 ### Common Falsy Values

 The following are generally considered false in a Boolean context:

```
False
None
0
0.0
0j
""
[]
()
{}
set()
```

 Most other objects are truthy.

 ## Example

```
name = ""

if name:
    print("Name provided.")
else:
    print("Name is empty.")
```

 **Output:**

```
Name is empty.
```

 ### Better Python Style

 Instead of:

```
if len(users) > 0:
    print("Users available.")
```

 you can usually write:

```
if users:
    print("Users available.")
```

---

 # 🔗 Combining Conditions

 Conditional statements become more powerful when combined with logical operators.

 Python provides:

```
and
or
not
```

 ## Example

```
age = 25
has_license = True

if age >= 18 and has_license:
    print("Allowed to drive.")
```

 **Output:**

```
Allowed to drive.
```

 ### Multiple Conditions

```
marks = 85
attendance = 90

if marks >= 40 and attendance >= 75:
    print("Student passed.")
else:
    print("Student failed.")
```

 **Output:**

```
Student passed.
```

---

 # 🔄 Conditional Statement Flow

 A typical Python decision-making structure looks like:

```
              Start
                │
                ▼
            Condition
                │
       ┌────────┴────────┐
       │                 │
     True              False
       │                 │
       ▼                 ▼
   Execute A         Execute B
       │                 │
       └────────┬────────┘
                │
                ▼
               End
```

 For multiple conditions:

```
              Start
                │
                ▼
             if
                │
          ┌─────┴─────┐
        True         False
          │             │
          ▼             ▼
       Execute        elif
                        │
                  ┌─────┴─────┐
                True         False
                  │             │
                  ▼             ▼
               Execute        else
                                │
                                ▼
                             Execute
```

---

 # ⚠️ Indentation in Conditional Statements

 Indentation is mandatory for defining Python code blocks.

 ### Correct

```
age = 20

if age >= 18:
    print("Adult")
```

 ### Incorrect

```
age = 20

if age >= 18:
print("Adult")
```

 The second example produces an `IndentationError`.

 ### Recommended Style

 Use **4 spaces** for each indentation level.

```
if condition:
    if another_condition:
        print("Condition satisfied.")
```

---

 # 🧪 Complete Practical Example

 The following program combines comparison, logical operators, membership, and conditional statements.

```
# Student Eligibility System

marks = 85
attendance = 90
role = "student"

allowed_roles = ["student", "teacher"]

if marks >= 40 and attendance >= 75:
    if role in allowed_roles:
        result = "PASS"
    else:
        result = "INVALID ROLE"
else:
    result = "FAIL"

print("Marks:", marks)
print("Attendance:", attendance)
print("Role:", role)
print("Result:", result)
```

 **Output:**

```
Marks: 85
Attendance: 90
Role: student
Result: PASS
```

---

 # 🏗️ Real-World Example

 A simple access-control system:

```
username = "admin"
password = "python123"
is_active = True

if username == "admin" and password == "python123":
    if is_active:
        print("Access granted.")
    else:
        print("Account is inactive.")
else:
    print("Invalid credentials.")
```

 **Output:**

```
Access granted.
```

 This demonstrates how conditional statements can represent real application logic.

---

 # 📊 Conditional Statement Comparison

 | Statement | Conditions | Execution |
| --- | --- | --- |
| `if` | One | Executes only when true |
| `if-else` | One | Chooses between two paths |
| `if-elif-else` | Multiple | Executes first matching branch |
| Nested `if` | Dependent | Condition inside another condition |
| Conditional expression | One | Compact two-value decision |
| `match-case` | Multiple patterns | Executes matching pattern |

---

 # 🧠 Common Mistakes

 ## 1\. Forgetting the Colon

 ❌ Incorrect:

```
if age >= 18
    print("Adult")
```

 ✅ Correct:

```
if age >= 18:
    print("Adult")
```

---

 ## 2\. Incorrect Indentation

 ❌ Incorrect:

```
if age >= 18:
print("Adult")
```

 ✅ Correct:

```
if age >= 18:
    print("Adult")
```

---

 ## 3\. Using `=` Instead of `==`

 Assignment:

```
age = 18
```

 Comparison:

```
age == 18
```

 Use `==` when checking equality.

---

 ## 4\. Incorrect Condition Ordering

 Consider:

```
marks = 95

if marks >= 40:
    print("Pass")
elif marks >= 90:
    print("Excellent")
```

 The `elif` will never execute because `marks >= 40` is already true.

 Prefer:

```
if marks >= 90:
    print("Excellent")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
```

---

 ## 5\. Overusing Nested Conditions

 Instead of deeply nesting:

```
if user:
    if user.is_active:
        if user.has_permission:
            print("Allowed")
```

 consider whether the logic can be simplified:

```
if user and user.is_active and user.has_permission:
    print("Allowed")
```

---

 # ✨ Best Practices

 ### 1\. Keep Conditions Readable

 Prefer:

```
if age >= 18 and has_license:
    print("Allowed")
```

 over unnecessarily complicated expressions.

 ### 2\. Use Parentheses When They Improve Clarity

```
if (age >= 18 and has_license) or is_admin:
    print("Allowed")
```

 ### 3\. Avoid Deep Nesting

 Use helper functions or guard clauses when conditional logic becomes difficult to follow.

 ### 4\. Use `elif` for Mutually Exclusive Choices

```
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
```

 ### 5\. Use `match-case` for Pattern-Based Decisions

```
match command:
    case "start":
        ...
    case "stop":
        ...
    case _:
        ...
```

 ### 6\. Prefer Explicit Conditions

 Readable:

```
if user is None:
    ...
```

 Readable:

```
if value:
    ...
```

 when checking truthiness is actually what you intend.

---

 # 🧠 Quick Reference

```
# if
if condition:
    statement

# if-else
if condition:
    statement
else:
    statement

# if-elif-else
if condition1:
    statement
elif condition2:
    statement
else:
    statement

# Nested if
if condition:
    if another_condition:
        statement

# Conditional expression
result = value_if_true if condition else value_if_false

# match-case
match value:
    case pattern1:
        statement
    case pattern2:
        statement
    case _:
        statement
```

---

 # 📁 Recommended Project Structure

```
python-learning/
│
├── 01-Variables/
│   └── ...
│
├── 02-Operators/
│   ├── 01_arithmetic_operators.py
│   ├── 02_assignment_operators.py
│   ├── 03_comparison_operators.py
│   ├── 04_logical_operators.py
│   ├── 05_bitwise_operators.py
│   ├── 06_membership_operators.py
│   └── 07_identity_operators.py
│
├── 03-Conditional-Statements/
│   ├── 01_if_statement.py
│   ├── 02_short_hand_if.py
│   ├── 03_if_else_statement.py
│   ├── 04_if_elif_else_statement.py
│   ├── 05_nested_if_else.py
│   ├── 06_conditional_expression.py
│   └── 07_match_case.py
│
└── README.md
```

---

 # 🎯 Learning Objectives

 After completing this topic, you should be able to:

 - Understand how conditional statements control program flow.
- Write basic `if` statements.
- Use short-hand `if` syntax appropriately.
- Implement `if-else` decision-making.
- Handle multiple conditions with `if-elif-else`.
- Build nested conditional logic.
- Use conditional expressions for simple decisions.
- Understand Python truthy and falsy values.
- Combine conditions with `and`, `or`, and `not`.
- Understand the importance of indentation.
- Use `match-case` for pattern matching.
- Use wildcard `_` patterns.
- Combine multiple patterns using `|`.
- Use guards with `match-case`.
- Choose between `if-elif-else` and `match-case`.
- Write readable and maintainable decision-making code.

---

 # 🧪 Practice Challenges

 ## Beginner

 1. Write a program that checks whether a number is positive or negative.
2. Check whether a number is even or odd.
3. Check whether a person is eligible to vote.
4. Determine whether a student passed or failed.
5. Find the greater of two numbers.

 ## Intermediate

 6. Create a grading system using `if-elif-else`.
7. Create an age classification program.
8. Build a simple login validation system.
9. Check whether a user is authorized to access a resource.
10. Use a nested `if` statement to implement an eligibility system.

 ## Advanced

 11. Rewrite a simple `if-else` assignment using a conditional expression.
12. Create a menu-driven program using `match-case`.
13. Use multiple patterns with `|` in `match-case`.
14. Use a `match-case` guard to classify numeric values.
15. Build a complete student eligibility system using multiple conditional techniques.

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

 Run an individual example:

```
python 01_if_statement.py
```

 For Python 3 installations where `python3` is required:

```
python3 01_if_statement.py
```

 > **Note:** `match-case` requires **Python 3.10 or later**.

---

 # 📚 References

 The concepts covered in this topic are based on standard Python conditional-statement concepts.

 GeeksforGeeks — Conditional Statements in Python

 For authoritative Python language documentation:

 Python Documentation — Compound Statements

 Python Documentation — \`match\` Statement

---

 # ⭐ Key Takeaway

 Conditional statements allow programs to **think, decide, and respond** based on data.

```
Input
  ↓
Condition
  ↓
Decision
  ↓
Code Execution
  ↓
Output
```

 Master these structures:

```
if
 ↓
if-else
 ↓
if-elif-else
 ↓
Nested Conditions
 ↓
Conditional Expressions
 ↓
match-case
```

 These concepts form the foundation of program control flow and are essential for building real-world Python applications.

---

 ## 🚀 Keep Learning. Keep Building.

 **Python → Logic → Practice → Projects → Problem Solving → Mastery**

 🐍 **Happy Coding!**
