# 🧮 01 — Calculator

> **A beginner-friendly command-line calculator built with Python to practice functions, user input, loops, conditionals, and exception handling.**

---

## 📌 Project Overview

The **Calculator** is the first project in the `24-Projects` section of this repository.

It is a simple command-line application that allows users to perform basic arithmetic operations:

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division

The project focuses on applying fundamental Python concepts in a small, practical application.

---

## 🎯 Learning Objectives

By completing this project, you will practice:

* Python functions
* Variables and data types
* User input
* Conditional statements
* `while` loops
* Exception handling
* `try` / `except`
* `ValueError`
* `ZeroDivisionError`
* f-strings
* Program flow
* Basic project structure

---

## 🛠️ Technologies Used

| Technology         | Purpose                        |
| ------------------ | ------------------------------ |
| 🐍 Python          | Programming language           |
| 💻 Terminal        | Application interface          |
| 🔧 Built-in Python | No external libraries required |

---

## 📁 Project Structure

```text
24-Projects/
└── 01-calculator/
    ├── calculator.py
    └── README.md
```

---

## ⚙️ Requirements

Make sure Python is installed on your system.

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

No external Python packages are required.

---

## 🚀 How to Run

### 1️⃣ Navigate to the project

```bash
cd 24-Projects/01-calculator
```

### 2️⃣ Run the program

Windows:

```powershell
python calculator.py
```

Linux/macOS:

```bash
python3 calculator.py
```

---

## 🧮 Available Operations

When the program starts, you will see:

```text
========================================
        🧮 SIMPLE CALCULATOR
========================================

Choose an operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
```

### ➕ Addition

```text
10 + 5 = 15
```

### ➖ Subtraction

```text
10 - 5 = 5
```

### ✖️ Multiplication

```text
10 × 5 = 50
```

### ➗ Division

```text
10 ÷ 5 = 2
```

---

## 💻 Example

```text
========================================
        🧮 SIMPLE CALCULATOR
========================================

Choose an operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit

Enter your choice (1-5): 1

Enter first number: 25
Enter second number: 15

✅ Result: 25 + 15 = 40
```

---

## 🧠 How It Works

The application follows this basic flow:

```text
                Start
                  │
                  ▼
          Display Calculator
                  │
                  ▼
          Select Operation
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
   Valid Choice        Invalid Choice
        │                   │
        ▼                   ▼
   Enter Numbers       Show Error
        │                   │
        ▼                   └──────► Menu
    Calculate
        │
        ▼
   Display Result
        │
        ▼
   Continue / Exit
```

---

## 🧩 Functions

The calculator separates each mathematical operation into its own function.

### Addition

```python
def add(a, b):
    return a + b
```

### Subtraction

```python
def subtract(a, b):
    return a - b
```

### Multiplication

```python
def multiply(a, b):
    return a * b
```

### Division

```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b
```

This makes the code easier to understand, test, and maintain.

---

## 🛡️ Error Handling

The calculator handles common user errors.

### Invalid Number

If the user enters:

```text
Enter first number: abc
```

The program displays:

```text
❌ Please enter valid numbers.
```

This is handled using:

```python
try:
    first_number = float(input("Enter first number: "))

except ValueError:
    print("❌ Please enter valid numbers.")
```

---

### Division by Zero

The program prevents:

```text
10 ÷ 0
```

and displays:

```text
❌ Cannot divide by zero.
```

---

## 🔄 Main Program Loop

The calculator uses a `while` loop so the user can perform multiple calculations without restarting the program.

```python
while True:
    # Calculator menu
```

The loop ends when the user selects:

```text
5. Exit
```

---

## 🧠 Python Concepts Used

| Concept        | Usage                      |
| -------------- | -------------------------- |
| Variables      | Store numbers and results  |
| Functions      | Perform calculations       |
| `input()`      | Get user input             |
| `if/elif/else` | Select operations          |
| `while`        | Repeat calculator          |
| `try/except`   | Handle errors              |
| `float()`      | Convert input to numbers   |
| f-strings      | Format output              |
| `return`       | Return calculation results |
| `break`        | Exit the loop              |

---

## 🧪 Practice Exercises

After completing the basic calculator, try adding:

### Level 1

* 🔢 Modulus `%`
* 🔢 Floor division `//`
* 🔢 Exponentiation `**`

### Level 2

* 📜 Calculation history
* 🔄 Clear history option
* 🔢 Support more than two numbers
* 🎨 Improve terminal formatting

### Level 3

Add advanced mathematical operations:

```text
√ Square Root
x² Square
% Percentage
sin() Sine
cos() Cosine
tan() Tangent
```

You can use Python's built-in `math` module:

```python
import math
```

---

## 🚀 Future Improvements

Possible upgrades:

```text
Basic Calculator
      ↓
Better Error Handling
      ↓
Calculation History
      ↓
Advanced Operations
      ↓
GUI Calculator
      ↓
Scientific Calculator
```

Possible GUI technologies:

* Tkinter
* PyQt
* CustomTkinter

---

## 📊 Project Difficulty

```text
Difficulty: ⭐ Beginner

Python Concepts: ⭐⭐
Logic:           ⭐⭐
Error Handling:  ⭐⭐
Project Value:   ⭐⭐⭐
```

---

## 💡 Key Takeaways

```text
Functions
   ↓
Organize Code

Input
   ↓
Interact with User

Conditions
   ↓
Choose Operation

Loops
   ↓
Repeat Program

Exceptions
   ↓
Handle Errors
```

The main lesson is to turn individual Python concepts into a **working application**.

---

## 📝 Quick Revision

```text
Calculator
│
├── Input
│
├── Menu
│
├── Operations
│   ├── Addition
│   ├── Subtraction
│   ├── Multiplication
│   └── Division
│
├── Functions
│
├── Loop
│
├── Error Handling
│
└── Output
```

### One-Line Revision

> **Input → Choose Operation → Calculate → Handle Errors → Display Result → Repeat**

---

## 📚 Related Python Concepts

This project builds a foundation for future projects involving:

* Functions
* CLI applications
* File handling
* Object-Oriented Programming
* APIs
* Automation
* GUI applications
* Web applications

---

## 👨‍💻 Author

**Kishor Patil**

B.Tech — Electronics & Communication Engineering

GitHub: [Kishor055](https://github.com/Kishor055)

---

## ⭐ Repository

This project is part of the **Python Programming** learning repository.

The `24-Projects` section focuses on applying Python concepts through practical projects.

---

## 📄 License

This project is available for educational and learning purposes.

---

## ⭐ Support

If this project helps you learn Python, consider giving the repository a ⭐ on GitHub.
