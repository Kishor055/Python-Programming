# 🔐 03 — Password Generator

> **A beginner-friendly Python command-line application that generates secure random passwords using Python's built-in `secrets` module.**

---

## 📌 Project Overview

The **Password Generator** is the third project in the `24-Projects` section of this Python Programming repository.

The program allows the user to choose a password length and automatically generates a random password containing:

* 🔤 Uppercase letters
* 🔡 Lowercase letters
* 🔢 Numbers
* 🔣 Special characters

The project introduces basic security-aware programming while practicing Python fundamentals.

---

## 🎯 Learning Objectives

By completing this project, you will practice:

* Python modules
* `secrets` module
* `string` module
* Functions
* User input
* Type conversion
* Input validation
* `while` loops
* `try / except`
* String concatenation
* Generator expressions
* `join()`
* Constants
* Basic secure random generation

---

## 🛠️ Technologies Used

| Technology   | Purpose                        |
| ------------ | ------------------------------ |
| 🐍 Python    | Programming language           |
| 🔐 `secrets` | Secure random value generation |
| 🔤 `string`  | Character sets                 |
| 💻 Terminal  | User interface                 |

No external packages are required.

---

## 📁 Project Structure

```text
24-Projects/
└── 03-password-generator/
    ├── program.py
    └── README.md
```

---

## ⚙️ Requirements

Make sure Python is installed on your computer.

Check the Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

This project uses only Python's standard library, so no `pip install` command is needed.

---

## 🚀 How to Run

### 1️⃣ Navigate to the project

```bash
cd 24-Projects/03-password-generator
```

### 2️⃣ Run the program

Windows:

```powershell
python program.py
```

Linux/macOS:

```bash
python3 program.py
```

---

## 💻 Example

```text
=============================================
        PASSWORD GENERATOR
=============================================

Enter password length (8-128): 16

Generated Password:
mT7#vQ2!xP9@kL4$
```

Each run can produce a different password.

---

## 🔐 Password Character Set

The generated password is created from three main character groups.

### Letters

```python
string.ascii_letters
```

Contains:

```text
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

### Numbers

```python
string.digits
```

Contains:

```text
0123456789
```

### Special Characters

```python
string.punctuation
```

Contains characters such as:

```text
! @ # $ % ^ & * ( ) _ + - = ...
```

These character groups are combined:

```python
characters = (
    string.ascii_letters
    + string.digits
    + string.punctuation
)
```

---

## 🔑 Why `secrets` Instead of `random`?

For security-sensitive random values, Python provides the `secrets` module.

The project uses:

```python
secrets.choice(characters)
```

instead of:

```python
random.choice(characters)
```

The `secrets` module is designed for generating values intended for security-related use cases.

---

## 🧩 Main Functions

### `get_password_length()`

Gets and validates the password length.

```python
def get_password_length():
    ...
```

The current allowed range is:

```text
Minimum: 8
Maximum: 128
```

Invalid input is handled using `try / except`.

---

### `generate_password(length)`

Creates the password using the selected character set.

```python
def generate_password(length):
    ...
```

The password is constructed using:

```python
"".join(...)
```

---

### `main()`

Controls the complete application flow:

```text
Start
  ↓
Display Menu
  ↓
Get Password Length
  ↓
Generate Password
  ↓
Display Password
  ↓
Exit
```

---

## 🔄 Password Generation Logic

```text
           Start
             │
             ▼
      Ask Password Length
             │
             ▼
       Validate Length
          /       \
      Invalid     Valid
        │           │
        ▼           ▼
   Show Error   Build Character Set
                    │
                    ▼
              Generate Characters
                    │
                    ▼
             Combine Characters
                    │
                    ▼
              Display Password
                    │
                    ▼
                   End
```

---

## 🛡️ Input Validation

The program checks whether the user enters a valid whole number.

Example:

```text
Enter password length (8-128): abc
```

Output:

```text
Please enter a valid whole number.
```

It also checks the allowed range:

```python
if MIN_LENGTH <= length <= MAX_LENGTH:
    return length
```

---

## 📏 Password Length Constants

The program uses constants instead of hard-coding the values throughout the code:

```python
MIN_LENGTH = 8
MAX_LENGTH = 128
```

This makes the program easier to maintain and modify.

For example:

```python
MIN_LENGTH = 12
MAX_LENGTH = 256
```

could be used for a different project requirement.

---

## 🧠 Python Concepts Used

| Concept    | Example                   | Purpose                                |
| ---------- | ------------------------- | -------------------------------------- |
| Import     | `import secrets`          | Use security-focused random generation |
| Module     | `string`                  | Access predefined character sets       |
| Constant   | `MIN_LENGTH`              | Store fixed configuration              |
| Function   | `def generate_password()` | Organize code                          |
| Input      | `input()`                 | Read user input                        |
| Conversion | `int()`                   | Convert input to an integer            |
| Condition  | `if`                      | Validate input                         |
| Loop       | `while`                   | Repeat until valid input               |
| Exception  | `try / except`            | Handle invalid input                   |
| Generator  | `for _ in range()`        | Generate characters                    |
| `join()`   | `"".join()`               | Build password string                  |

---

## 🧪 Practice Exercises

After completing the basic version, try improving the project.

### 🟢 Level 1 — Beginner

Add options to control:

* Password length
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters

Example:

```text
Password Length: 16
Include Numbers? y
Include Symbols? y
```

---

### 🟡 Level 2 — Intermediate

Add:

* Generate multiple passwords
* Password strength indicator
* Copy-to-clipboard support
* Password history
* Custom character sets

Example:

```text
Password: A8@kP2!xL9$qW7#m
Strength: Strong
```

---

### 🔴 Level 3 — Advanced

Build a more complete password manager project with:

```text
Password Generator
       ↓
Password Strength Checker
       ↓
Password Storage
       ↓
Encryption
       ↓
Master Password
       ↓
Password Manager
```

For real password storage, credentials should not be stored as plain text.

---

## 💡 Possible Future Version

```text
              🔐 Password Tool
                     │
         ┌───────────┼───────────┐
         ▼           ▼           ▼
      Generate     Strength    Settings
         │           │           │
         ▼           ▼           ▼
      Password     Check      Customize
         │
         ▼
      Copy / Save
```

---

## 📊 Project Difficulty

```text
Difficulty: ⭐⭐ Beginner

Python Concepts: ⭐⭐
String Handling: ⭐⭐
Input Validation: ⭐⭐
Security Concepts: ⭐⭐⭐
Project Value: ⭐⭐⭐
```

---

## ⚡ Quick Revision

```text
secrets
   ↓
Character Set
   ↓
Password Length
   ↓
Validate Input
   ↓
Generate Random Characters
   ↓
Join Characters
   ↓
Display Password
```

### One-Line Revision

> **Choose length → Build character set → Generate securely → Join characters → Display password**

---

## 🔑 Important Code

### Import Modules

```python
import secrets
import string
```

### Character Set

```python
characters = (
    string.ascii_letters
    + string.digits
    + string.punctuation
)
```

### Secure Character Selection

```python
secrets.choice(characters)
```

### Generate Password

```python
password = "".join(
    secrets.choice(characters)
    for _ in range(length)
)
```

---

## ✅ Skills Gained

After completing this project, you should understand:

```text
✅ Python modules
✅ Secure random generation
✅ String manipulation
✅ Functions
✅ Loops
✅ Input validation
✅ Exception handling
✅ Generator expressions
✅ Basic security-aware programming
```

---

## 👨‍💻 Author

**Kishor Patil**

B.Tech — Electronics & Communication Engineering

GitHub: [Kishor055](https://github.com/Kishor055)

---

## 📚 Part of Python Projects

This project is part of:

```text
24 — Python Projects
        │
        ├── 01 — Calculator
        ├── 02 — Number Guessing Game
        └── 03 — Password Generator
```

The purpose of this section is to convert Python concepts into practical applications.

---

## 📄 License

This project is available for educational and learning purposes.

---

## ⭐ Support

If this project helps you learn Python, consider giving the repository a ⭐ on GitHub.
