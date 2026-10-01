# 🎯 02 — Number Guessing Game

> **A beginner-friendly Python command-line game where the computer generates a random number and the player tries to guess it.**

---

## 📌 Project Overview

The **Number Guessing Game** is the second project in the `24-Projects` section of this Python Programming repository.

The computer randomly selects a number between **1 and 100**. The player keeps entering guesses until the correct number is found.

After every guess, the program provides a hint:

* 📈 **Too low** — guess a higher number
* 📉 **Too high** — guess a lower number
* 🎉 **Correct** — the game is completed

The player can also choose to play multiple rounds.

---

## 🎯 Learning Objectives

This project helps practice:

* Python functions
* `random` module
* Random number generation
* User input
* Type conversion
* `if / elif / else`
* `while` loops
* Input validation
* Exception handling
* Counters
* String methods
* Program structure

---

## 🛠️ Technologies Used

| Technology  | Purpose                    |
| ----------- | -------------------------- |
| 🐍 Python   | Programming language       |
| 🎲 `random` | Generate the secret number |
| 💻 Terminal | User interface             |

No external libraries are required.

---

## 📁 Project Structure

```text
24-Projects/
└── 02-number-guessing-game/
    ├── number_guessing_game.py
    └── README.md
```

---

## ⚙️ Requirements

Make sure Python is installed.

Check your version:

```bash
python --version
```

or:

```bash
python3 --version
```

No `pip install` command is required.

---

## 🚀 How to Run

### 1️⃣ Navigate to the project

```bash
cd 24-Projects/02-number-guessing-game
```

### 2️⃣ Run the program

Windows:

```powershell
python number_guessing_game.py
```

Linux/macOS:

```bash
python3 number_guessing_game.py
```

---

## 🎮 How to Play

When the game starts:

```text
========================================
     NUMBER GUESSING GAME
========================================

I'm thinking of a number between 1 and 100!
```

Enter a number:

```text
Enter your guess (1-100): 50
```

The program gives a hint.

### Guess too low

```text
Enter your guess (1-100): 25
Too low! Try again.
```

### Guess too high

```text
Enter your guess (1-100): 75
Too high! Try again.
```

### Correct guess

```text
Enter your guess (1-100): 63

Congratulations!
You guessed the number: 63
Attempts: 6
```

---

## 🧠 How It Works

```text
                 Start
                   │
                   ▼
        Generate Random Number
             1 ─── 100
                   │
                   ▼
             Ask for Guess
                   │
                   ▼
            Validate Input
                   │
             ┌─────┴─────┐
             │           │
           Invalid      Valid
             │           │
             ▼           ▼
        Show Error    Compare Guess
                           │
                  ┌────────┼────────┐
                  ▼        ▼        ▼
                Lower    Higher   Correct
                  │        │        │
                  └────────┴────────┤
                                   ▼
                             Show Attempts
                                   │
                                   ▼
                              Play Again?
                              /        \
                            Yes         No
                             │           │
                             ▼           ▼
                          New Game      Exit
```

---

## 🎲 Random Number Generation

The game uses Python's built-in `random` module:

```python
import random
```

A number between 1 and 100 is generated using:

```python
secret_number = random.randint(1, 100)
```

`randint()` includes both the starting and ending values.

---

## 🔢 Input Validation

The program checks whether the entered value is a valid number:

```python
try:
    guess = int(input("Enter your guess (1-100): "))
except ValueError:
    print("Please enter a valid whole number.")
```

It also checks that the number is within the game range:

```python
if 1 <= guess <= 100:
    return guess
```

This prevents invalid values from breaking the game.

---

## 🧩 Main Functions

### `get_valid_guess()`

Responsible for:

* Reading user input
* Converting input to an integer
* Checking the range
* Handling invalid input

```python
def get_valid_guess():
    ...
```

### `play_game()`

Responsible for:

* Generating the secret number
* Tracking attempts
* Comparing guesses
* Displaying hints
* Ending the current round

```python
def play_game():
    ...
```

### `main()`

Responsible for:

* Starting the application
* Displaying the title
* Allowing replay
* Ending the program

```python
def main():
    ...
```

---

## 🔢 Attempt Counter

The game tracks how many guesses the player makes:

```python
attempts = 0
```

After every valid guess:

```python
attempts += 1
```

The final number of attempts is displayed when the player wins.

---

## 🔄 Replay Feature

After completing a round, the player is asked:

```text
Play again? (y/n):
```

The input is normalized using:

```python
choice = input(...).strip().lower()
```

Entering `y` starts another game.

Any other response exits the program.

---

## 🧠 Python Concepts Used

| Concept         | Example            | Purpose                      |
| --------------- | ------------------ | ---------------------------- |
| Import          | `import random`    | Use random number generation |
| Function        | `def play_game()`  | Organize code                |
| Input           | `input()`          | Get user guesses             |
| Type conversion | `int()`            | Convert input to number      |
| Condition       | `if / elif / else` | Compare guesses              |
| Loop            | `while`            | Continue guessing            |
| Exception       | `try / except`     | Handle invalid input         |
| Counter         | `attempts += 1`    | Track guesses                |
| String methods  | `.strip().lower()` | Clean input                  |
| Return          | `return`           | Finish a function            |

---

## 🧪 Practice Exercises

After completing the basic version, try these improvements.

### 🟢 Level 1 — Beginner

Add:

* Maximum number of attempts
* Difficulty levels
* Custom number range
* Better game messages

Example:

```text
Easy   → 1-50
Medium → 1-100
Hard   → 1-500
```

---

### 🟡 Level 2 — Intermediate

Add:

* Score system
* Best score
* Hint after several attempts
* Guess history
* Number of games played

Example:

```text
Guess History:
25 → 60 → 75 → 68 → 63
```

---

### 🔴 Level 3 — Advanced

Build:

* Multiplayer mode
* Timed mode
* Leaderboard
* Persistent scores using a file
* Difficulty selection menu
* ASCII/terminal interface

---

## 💡 Possible Future Version

```text
Number Guessing Game
        │
        ▼
Difficulty Selection
        │
        ├── Easy
        ├── Medium
        └── Hard
        │
        ▼
Random Number
        │
        ▼
Player Guesses
        │
        ▼
Hints + Attempts
        │
        ▼
Score Calculation
        │
        ▼
Leaderboard
```

---

## 📊 Project Difficulty

```text
Difficulty: ⭐ Beginner

Python Concepts: ⭐⭐
Logic:           ⭐⭐
Input Handling:  ⭐⭐
Random Module:   ⭐
Project Value:   ⭐⭐⭐
```

---

## ⚡ Quick Revision

```text
import random
      ↓
Generate Number
      ↓
Take User Input
      ↓
Validate Input
      ↓
Compare Guess
      ↓
Too Low / Too High
      ↓
Track Attempts
      ↓
Correct Guess
      ↓
Play Again / Exit
```

### One-Line Revision

> **Generate → Guess → Validate → Compare → Hint → Repeat → Win**

---

## 🔑 Important Code

### Generate Random Number

```python
secret_number = random.randint(1, 100)
```

### Validate Range

```python
if 1 <= guess <= 100:
    return guess
```

### Compare Guess

```python
if guess < secret_number:
    print("Too low!")

elif guess > secret_number:
    print("Too high!")

else:
    print("Congratulations!")
```

### Track Attempts

```python
attempts += 1
```

---

## 🚀 Skills Gained

After completing this project, you should be comfortable with:

```text
✅ Functions
✅ Loops
✅ Conditions
✅ Input validation
✅ Exception handling
✅ Random number generation
✅ Counters
✅ Basic CLI application design
```

---

## 👨‍💻 Author

**Kishor Patil**

B.Tech — Electronics & Communication Engineering

GitHub: [Kishor055](https://github.com/Kishor055)

---

## 📚 Part of Python Projects

This project belongs to:

```text
24 — Python Projects
        │
        ├── 01 — Calculator
        │
        └── 02 — Number Guessing Game
```

The goal of this section is to turn Python concepts into practical, working applications.

---

## 📄 License

This project is available for educational and learning purposes.

---

## ⭐ Support

If this project helps you learn Python, consider giving the repository a ⭐ on GitHub.
