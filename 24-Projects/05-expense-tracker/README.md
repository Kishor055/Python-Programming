# 💰 05 — Expense Tracker

> **A beginner-friendly Python command-line application for recording, viewing, categorizing, summarizing, and deleting expenses using JSON file storage.**

---

## 📌 Project Overview

The **Expense Tracker** is the fifth project in the `24-Projects` section of this Python Programming repository.

The application helps users keep track of their daily spending from the terminal.

### Features

* ➕ Add expenses
* 📋 View all expenses
* 💰 Calculate total spending
* 📊 View spending by category
* 🗑️ Delete expenses
* 💾 Save expenses to a JSON file
* 🔄 Load saved expenses when the program starts
* 🛡️ Handle invalid input

---

## 🎯 Learning Objectives

This project helps practice:

* Python functions
* Lists
* Dictionaries
* Loops
* Conditional statements
* User input
* Type conversion
* Exception handling
* JSON
* File handling
* `pathlib`
* `sum()`
* Data aggregation
* CRUD operations
* Persistent storage

---

## 🛠️ Technologies Used

| Technology   | Purpose                     |
| ------------ | --------------------------- |
| 🐍 Python    | Programming language        |
| 📦 `json`    | Store and load expense data |
| 📁 `pathlib` | Manage file paths           |
| 💻 Terminal  | User interface              |

No external packages are required.

---

## 📁 Project Structure

```text
24-Projects/
└── 05-expense-tracker/
    ├── program.py
    ├── expenses.json
    └── README.md
```

---

## ⚙️ Requirements

Make sure Python is installed.

Check the version:

```bash
python --version
```

or:

```bash
python3 --version
```

This project uses only Python's standard library.

---

## 🚀 How to Run

### 1️⃣ Navigate to the project

```bash
cd 24-Projects/05-expense-tracker
```

### 2️⃣ Run the application

Windows:

```powershell
python program.py
```

Linux/macOS:

```bash
python3 program.py
```

---

## 🖥️ Application Menu

When the program starts:

```text
========== EXPENSE TRACKER ==========
1. Add Expense
2. View Expenses
3. Show Total
4. Category Summary
5. Delete Expense
6. Exit
=====================================
Enter your choice (1-6):
```

---

## ➕ Add Expense

Select:

```text
1. Add Expense
```

The program asks for:

```text
Enter expense description:
Enter category:
Enter amount:
```

Example:

```text
Enter your choice (1-6): 1
Enter expense description: Lunch
Enter category: Food
Enter amount: 150

Expense added successfully.
```

---

## 📋 View Expenses

Select:

```text
2. View Expenses
```

Example output:

```text
========== EXPENSES ==========
1. Lunch | Food | ₹150.00
2. Bus Ticket | Travel | ₹40.00
3. Notebook | Education | ₹80.00
==============================
```

Each expense contains:

```text
Title
Category
Amount
```

---

## 💰 Show Total Expenses

Select:

```text
3. Show Total
```

Example:

```text
Total Expenses: ₹270.00
```

The total is calculated using:

```python
total = sum(expense["amount"] for expense in expenses)
```

---

## 📊 Category Summary

Select:

```text
4. Category Summary
```

Example:

```text
====== CATEGORY SUMMARY ======
Food: ₹450.00
Travel: ₹180.00
Education: ₹250.00
==============================
```

This groups expenses by category and calculates the total amount spent in each category.

---

## 🗑️ Delete Expense

Select:

```text
5. Delete Expense
```

Example:

```text
Enter expense number to delete: 2
Deleted: Bus Ticket
```

The selected expense is removed from the list and the updated data is saved to `expenses.json`.

---

## 💾 Persistent Storage

Expenses are stored in:

```text
expenses.json
```

Example:

```json
[
    {
        "title": "Lunch",
        "category": "Food",
        "amount": 150.0
    },
    {
        "title": "Bus Ticket",
        "category": "Travel",
        "amount": 40.0
    }
]
```

The data remains available after closing and reopening the application.

---

## 🧩 Data Structure

Each expense is represented as a dictionary:

```python
{
    "title": "Lunch",
    "category": "Food",
    "amount": 150.0
}
```

Multiple expenses are stored in a list:

```python
expenses = [
    {
        "title": "Lunch",
        "category": "Food",
        "amount": 150.0
    },
    {
        "title": "Bus Ticket",
        "category": "Travel",
        "amount": 40.0
    }
]
```

---

## 🔄 Expense Tracker Workflow

```text
                  Start
                    │
                    ▼
              Load Expenses
                    │
                    ▼
               Show Menu
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
   Add Expense   View Expenses  Show Total
       │            │            │
       └────────────┼────────────┘
                    │
                    ▼
             Category Summary
                    │
                    ▼
             Delete Expense
                    │
                    ▼
              Save Expenses
                    │
                    ▼
                Show Menu
                    │
                    ▼
                  Exit
```

---

## 🧮 Total Calculation

The total expense is calculated with Python's `sum()` function:

```python
total = sum(
    expense["amount"]
    for expense in expenses
)
```

For example:

```text
₹150 + ₹40 + ₹80 = ₹270
```

---

## 📊 Category Aggregation

The program creates a summary dictionary:

```python
summary = {}
```

Each expense is added to its category:

```python
summary[category] = (
    summary.get(category, 0) + expense["amount"]
)
```

Example:

```text
Food
 ├── Lunch      ₹150
 ├── Snacks     ₹50
 └── Dinner     ₹200
       ↓
Total Food = ₹400
```

---

## 🛡️ Input Validation

The program validates expense amounts.

### Invalid amount

```text
Enter amount: abc
```

Output:

```text
Please enter a valid amount.
```

### Negative amount

```text
Enter amount: -100
```

Output:

```text
Amount must be greater than 0.
```

This prevents invalid expense values from being stored.

---

## 🧠 Main Functions

### `load_expenses()`

Loads saved expenses from `expenses.json`.

```python
def load_expenses():
    ...
```

### `save_expenses(expenses)`

Saves the current expense list to the JSON file.

```python
def save_expenses(expenses):
    ...
```

### `add_expense(expenses)`

Creates a new expense.

```python
def add_expense(expenses):
    ...
```

### `view_expenses(expenses)`

Displays all recorded expenses.

```python
def view_expenses(expenses):
    ...
```

### `show_total(expenses)`

Calculates total spending.

```python
def show_total(expenses):
    ...
```

### `show_category_summary(expenses)`

Groups spending by category.

```python
def show_category_summary(expenses):
    ...
```

### `delete_expense(expenses)`

Removes a selected expense.

```python
def delete_expense(expenses):
    ...
```

### `main()`

Controls the complete application.

```python
def main():
    ...
```

---

## 🧠 Python Concepts Used

| Concept       | Example                         | Purpose                  |
| ------------- | ------------------------------- | ------------------------ |
| Function      | `def add_expense()`             | Organize logic           |
| List          | `expenses = []`                 | Store multiple expenses  |
| Dictionary    | `{"title": ..., "amount": ...}` | Represent an expense     |
| Loop          | `while True`                    | Keep application running |
| Condition     | `if / elif / else`              | Control program flow     |
| Input         | `input()`                       | Read user data           |
| Conversion    | `float()`                       | Convert amount to number |
| Exception     | `try / except`                  | Handle invalid input     |
| JSON          | `json.load()`                   | Read saved data          |
| JSON          | `json.dump()`                   | Write saved data         |
| `sum()`       | `sum(...)`                      | Calculate totals         |
| `enumerate()` | `enumerate(expenses, start=1)`  | Number expenses          |
| `Path`        | `Path("expenses.json")`         | Manage file paths        |

---

## 🔄 CRUD Operations

The application demonstrates CRUD concepts:

| CRUD       | Expense Tracker                        |
| ---------- | -------------------------------------- |
| **Create** | Add Expense                            |
| **Read**   | View Expenses                          |
| **Update** | Modify expense data in future versions |
| **Delete** | Delete Expense                         |

```text
CRUD
 │
 ├── Create → Add
 ├── Read   → View
 ├── Update → Edit
 └── Delete → Remove
```

---

## 🧪 Practice Exercises

After completing the basic version, improve the application.

### 🟢 Level 1 — Beginner

Add:

* Edit an expense
* Clear all expenses
* Show number of expenses
* Show highest expense
* Show lowest expense

Example:

```text
Number of Expenses: 12
Highest Expense: ₹1200
Lowest Expense: ₹40
```

---

### 🟡 Level 2 — Intermediate

Add:

* Expense dates
* Monthly summaries
* Weekly summaries
* Search expenses
* Filter by category
* Sort by amount
* Sort by date

Example:

```text
Monthly Summary — September 2026

Food:      ₹4,250
Travel:    ₹1,800
Education: ₹1,200
Other:       ₹750
-------------------
Total:     ₹8,000
```

---

### 🔴 Level 3 — Advanced

Turn the project into a complete personal finance application:

```text
Expense Tracker
      │
      ├── Income
      ├── Expenses
      ├── Budgets
      ├── Categories
      ├── Reports
      ├── Monthly Analytics
      ├── Charts
      ├── Database
      └── Web Interface
```

Possible future technologies:

* SQLite
* SQLAlchemy
* Pandas
* Matplotlib
* Flask
* FastAPI

---

## 📈 Future Dashboard

A future version could provide:

```text
╔══════════════════════════════╗
║       EXPENSE DASHBOARD      ║
╠══════════════════════════════╣
║ Total Spent     ₹8,000       ║
║ Food            ₹4,250       ║
║ Travel          ₹1,800       ║
║ Education       ₹1,200       ║
║ Other             ₹750       ║
╚══════════════════════════════╝
```

Charts could later visualize monthly and category-based spending.

---

## 💡 Future Architecture

```text
                  User
                    │
                    ▼
               CLI / Web UI
                    │
                    ▼
             Expense Tracker
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
       Business Logic       Reports
          │                   │
          ▼                   ▼
       Database            Charts
          │
          ▼
    SQLite / PostgreSQL
```

The current version uses JSON to keep the project simple and beginner-friendly.

---

## 📊 Project Difficulty

```text
Difficulty: ⭐⭐ Beginner

Python Concepts: ⭐⭐⭐
File Handling:   ⭐⭐⭐
JSON:             ⭐⭐⭐
Data Processing:  ⭐⭐⭐
CRUD Logic:       ⭐⭐⭐
Project Value:    ⭐⭐⭐⭐
```

---

## ⚡ Quick Revision

```text
Expense
   ↓
Title + Category + Amount
   ↓
Store in List
   ↓
Save to JSON
   ↓
View Expenses
   ↓
Calculate Total
   ↓
Group by Category
   ↓
Delete Expense
   ↓
Save Changes
```

### One-Line Revision

> **Add → Store → Save → View → Calculate → Summarize → Delete**

---

## 🔑 Important Code

### Expense Object

```python
expense = {
    "title": title,
    "category": category,
    "amount": amount
}
```

### Add Expense

```python
expenses.append(expense)
save_expenses(expenses)
```

### Calculate Total

```python
total = sum(
    expense["amount"]
    for expense in expenses
)
```

### Delete Expense

```python
expenses.pop(expense_number - 1)
save_expenses(expenses)
```

### Save JSON

```python
with EXPENSES_FILE.open("w", encoding="utf-8") as file:
    json.dump(expenses, file, indent=4)
```

---

## ✅ Skills Gained

After completing this project, you should understand:

```text
✅ Functions
✅ Lists
✅ Dictionaries
✅ Loops
✅ Conditions
✅ User input
✅ Type conversion
✅ Input validation
✅ Exception handling
✅ JSON
✅ File handling
✅ pathlib
✅ sum()
✅ Data aggregation
✅ CRUD operations
✅ Persistent storage
✅ CLI application design
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
        ├── 03 — Password Generator
        ├── 04 — To-Do App
        └── 05 — Expense Tracker
```

The purpose of this section is to transform Python concepts into practical, working applications.

---

## 📄 License

This project is available for educational and learning purposes.

---

## ⭐ Support

If this project helps you learn Python, consider giving the repository a ⭐ on GitHub.
