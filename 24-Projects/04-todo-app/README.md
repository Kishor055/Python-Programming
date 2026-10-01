# ✅ 04 — To-Do App

> **A simple Python command-line To-Do application for creating, viewing, completing, and deleting tasks with persistent JSON storage.**

---

## 📌 Project Overview

The **To-Do App** is the fourth project in the `24-Projects` section of this Python Programming repository.

This project allows users to manage their daily tasks directly from the terminal.

### Features

* ➕ Add tasks
* 📋 View tasks
* ✅ Mark tasks as completed
* 🗑️ Delete tasks
* 💾 Save tasks permanently
* 🔄 Load tasks when the application starts
* 🛡️ Handle invalid input

Tasks are stored locally in a `tasks.json` file.

---

## 🎯 Learning Objectives

This project helps practice:

* Python functions
* Lists
* Dictionaries
* Loops
* Conditional statements
* User input
* Exception handling
* JSON
* File handling
* `pathlib`
* CRUD operations
* Persistent data storage
* Basic application structure

---

## 🛠️ Technologies Used

| Technology   | Purpose                  |
| ------------ | ------------------------ |
| 🐍 Python    | Programming language     |
| 📦 `json`    | Store and load task data |
| 📁 `pathlib` | Manage file paths        |
| 💻 Terminal  | User interface           |

No external packages are required.

---

## 📁 Project Structure

```text
24-Projects/
└── 04-todo-app/
    ├── program.py
    ├── tasks.json
    └── README.md
```

---

## ⚙️ Requirements

Install Python on your system.

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

This project uses only Python's standard library.

No `pip install` command is required.

---

## 🚀 How to Run

### 1️⃣ Navigate to the project

```bash
cd 24-Projects/04-todo-app
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
========== TO-DO APP ==========
1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit
===============================
Enter your choice (1-5):
```

---

## ➕ Add a Task

Select:

```text
1. Add Task
```

Example:

```text
Enter your choice (1-5): 1
Enter task: Complete Python project
Task added successfully.
```

The task is stored in `tasks.json`.

---

## 📋 View Tasks

Select:

```text
2. View Tasks
```

Example:

```text
========== TO-DO LIST ==========
1. [ ] Complete Python project
2. [ ] Study functions
3. [✓] Practice JSON
===============================
```

### Task Status

```text
[ ] → Pending
[✓] → Completed
```

---

## ✅ Complete a Task

Select:

```text
3. Complete Task
```

Example:

```text
Enter task number to complete: 2
Task marked as completed.
```

The task status changes from:

```text
[ ]
```

to:

```text
[✓]
```

---

## 🗑️ Delete a Task

Select:

```text
4. Delete Task
```

Example:

```text
Enter task number to delete: 1
Deleted: Complete Python project
```

The task is removed from both the application and `tasks.json`.

---

## 💾 Persistent Storage

The application stores tasks in:

```text
tasks.json
```

Initial file:

```json
[]
```

After adding tasks, it may look like:

```json
[
    {
        "title": "Complete Python project",
        "completed": false
    },
    {
        "title": "Study functions",
        "completed": true
    }
]
```

Because the tasks are saved to a file, they remain available after closing and reopening the program.

---

## 🧩 How It Works

```text
                    Start
                      │
                      ▼
                 Load Tasks
                      │
                      ▼
                 Show Menu
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
     Add Task     View Tasks    Complete Task
        │             │             │
        └─────────────┼─────────────┘
                      │
                      ▼
                  Delete Task
                      │
                      ▼
                  Save Tasks
                      │
                      ▼
                  Show Menu
                      │
                      ▼
                    Exit
```

---

## 🗄️ Data Structure

Each task is stored as a Python dictionary:

```python
{
    "title": "Study Python",
    "completed": False
}
```

Multiple tasks are stored in a list:

```python
tasks = [
    {
        "title": "Study Python",
        "completed": False
    },
    {
        "title": "Practice coding",
        "completed": True
    }
]
```

---

## 🔄 CRUD Operations

The application demonstrates basic **CRUD** concepts.

| Operation  | To-Do App       |
| ---------- | --------------- |
| **Create** | Add a task      |
| **Read**   | View tasks      |
| **Update** | Complete a task |
| **Delete** | Delete a task   |

```text
CRUD
 │
 ├── Create → Add
 ├── Read   → View
 ├── Update → Complete
 └── Delete → Remove
```

---

## 📦 JSON Handling

The project uses Python's built-in `json` module.

### Load JSON

```python
with TASKS_FILE.open("r", encoding="utf-8") as file:
    tasks = json.load(file)
```

### Save JSON

```python
with TASKS_FILE.open("w", encoding="utf-8") as file:
    json.dump(tasks, file, indent=4)
```

The `indent=4` option keeps the JSON file easy to read.

---

## 📁 Path Handling

The project uses `pathlib`:

```python
from pathlib import Path

TASKS_FILE = Path("tasks.json")
```

Checking whether the file exists:

```python
if not TASKS_FILE.exists():
    return []
```

This provides a clean way to work with files and paths.

---

## 🛡️ Error Handling

The application handles invalid user input.

### Invalid menu choice

```text
Enter your choice (1-5): 8
Invalid choice. Please select 1-5.
```

### Invalid task number

```text
Enter task number to complete: abc
Please enter a valid number.
```

### Invalid JSON

If `tasks.json` contains invalid JSON, the application safely falls back to an empty task list.

```python
except (json.JSONDecodeError, OSError):
    return []
```

---

## 🧠 Main Functions

### `load_tasks()`

Loads saved tasks from `tasks.json`.

```python
def load_tasks():
    ...
```

### `save_tasks(tasks)`

Writes the current task list to the JSON file.

```python
def save_tasks(tasks):
    ...
```

### `add_task(tasks)`

Creates and stores a new task.

```python
def add_task(tasks):
    ...
```

### `view_tasks(tasks)`

Displays all available tasks.

```python
def view_tasks(tasks):
    ...
```

### `complete_task(tasks)`

Updates a task's completion status.

```python
def complete_task(tasks):
    ...
```

### `delete_task(tasks)`

Removes a task from the list.

```python
def delete_task(tasks):
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

| Concept       | Example                            | Purpose                      |
| ------------- | ---------------------------------- | ---------------------------- |
| Function      | `def add_task()`                   | Organize program logic       |
| List          | `tasks = []`                       | Store multiple tasks         |
| Dictionary    | `{"title": ..., "completed": ...}` | Represent a task             |
| Loop          | `while True`                       | Keep the application running |
| Condition     | `if / elif / else`                 | Control program flow         |
| Input         | `input()`                          | Read user commands           |
| Exception     | `try / except`                     | Handle errors                |
| JSON          | `json.load()`                      | Read saved data              |
| JSON          | `json.dump()`                      | Write saved data             |
| `Path`        | `Path("tasks.json")`               | Manage file paths            |
| `enumerate()` | `enumerate(tasks, start=1)`        | Number tasks                 |

---

## 🧪 Practice Exercises

After completing the basic project, try adding new features.

### 🟢 Level 1 — Beginner

Add:

* Edit a task
* Clear all tasks
* Count pending tasks
* Count completed tasks
* Confirmation before deleting

Example:

```text
Total Tasks: 5
Completed: 3
Pending: 2
```

---

### 🟡 Level 2 — Intermediate

Add:

* Task priority
* Due dates
* Categories
* Search tasks
* Sort tasks
* Mark task as pending again

Example:

```text
1. [ ] Study Python
   Priority: High
   Due: 2026-10-05
```

---

### 🔴 Level 3 — Advanced

Turn the project into a complete task-management application:

```text
To-Do App
   │
   ├── User Accounts
   ├── Task Categories
   ├── Priorities
   ├── Deadlines
   ├── Search
   ├── Filters
   ├── Statistics
   ├── Database
   └── Web Interface
```

Possible future technologies:

* SQLite
* SQLAlchemy
* Flask
* FastAPI
* HTML/CSS
* JavaScript

---

## 💡 Future Architecture

```text
                 User
                  │
                  ▼
             Web Interface
                  │
                  ▼
               Flask
                  │
                  ▼
             Application
                Logic
                  │
                  ▼
             SQLAlchemy
                  │
                  ▼
              SQLite /
            PostgreSQL
```

The current project uses JSON to keep the implementation simple and beginner-friendly.

---

## 📊 Project Difficulty

```text
Difficulty: ⭐⭐ Beginner

Python Concepts: ⭐⭐⭐
File Handling:   ⭐⭐⭐
JSON:             ⭐⭐⭐
CRUD Logic:       ⭐⭐⭐
Project Value:    ⭐⭐⭐⭐
```

---

## ⚡ Quick Revision

```text
List + Dictionary
        ↓
Create Task
        ↓
Save JSON
        ↓
Load JSON
        ↓
View Tasks
        ↓
Update Task
        ↓
Delete Task
        ↓
Repeat
```

### One-Line Revision

> **Create → Read → Update → Delete → Save → Load**

---

## 🔑 Important Code

### Load Tasks

```python
def load_tasks():
    if not TASKS_FILE.exists():
        return []

    with TASKS_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)
```

### Save Tasks

```python
def save_tasks(tasks):
    with TASKS_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)
```

### Add Task

```python
tasks.append({
    "title": title,
    "completed": False
})
```

### Complete Task

```python
tasks[task_number - 1]["completed"] = True
```

### Delete Task

```python
tasks.pop(task_number - 1)
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
✅ Input validation
✅ Exception handling
✅ File handling
✅ JSON
✅ pathlib
✅ CRUD operations
✅ Persistent storage
✅ CLI application structure
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
        └── 04 — To-Do App
```

The purpose of this section is to transform Python concepts into practical, working applications.

---

## 📄 License

This project is available for educational and learning purposes.

---

## ⭐ Support

If this project helps you learn Python, consider giving the repository a ⭐ on GitHub.
