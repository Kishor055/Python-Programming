```python
"""
To-Do App
---------
A simple command-line to-do application with JSON file storage.

Features:
- Add tasks
- View tasks
- Mark tasks as completed
- Delete tasks
- Save tasks between program runs
"""

import json
from pathlib import Path


TASKS_FILE = Path("tasks.json")


def load_tasks():
    """Load tasks from the JSON file."""
    if not TASKS_FILE.exists():
        return []

    try:
        with TASKS_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with TASKS_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    """Add a new task."""
    title = input("Enter task: ").strip()

    if not title:
        print("Task cannot be empty.")
        return

    tasks.append({
        "title": title,
        "completed": False
    })

    save_tasks(tasks)
    print("Task added successfully.")


def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n========== TO-DO LIST ==========")

    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{index}. [{status}] {task['title']}")

    print("===============================")


def complete_task(tasks):
    """Mark a task as completed."""
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to complete: "))

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    """Delete a task."""
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Deleted: {removed_task['title']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    """Run the To-Do application."""
    tasks = load_tasks()

    while True:
        print("\n========== TO-DO APP ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        print("===============================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Thank you for using the To-Do App.")
            break

        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
```
