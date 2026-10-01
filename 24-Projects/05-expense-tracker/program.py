```python
"""
Expense Tracker
---------------
A simple command-line expense tracker that allows users to:

- Add expenses
- View all expenses
- View total spending
- Delete expenses
- Store expenses in a JSON file
"""

import json
from pathlib import Path


EXPENSES_FILE = Path("expenses.json")


def load_expenses():
    """Load expenses from the JSON file."""
    if not EXPENSES_FILE.exists():
        return []

    try:
        with EXPENSES_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_expenses(expenses):
    """Save expenses to the JSON file."""
    with EXPENSES_FILE.open("w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    """Add a new expense."""
    title = input("Enter expense description: ").strip()

    if not title:
        print("Expense description cannot be empty.")
        return

    category = input("Enter category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    expense = {
        "title": title,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully.")


def view_expenses(expenses):
    """Display all expenses."""
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n========== EXPENSES ==========")

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['title']} | "
            f"{expense['category']} | "
            f"₹{expense['amount']:.2f}"
        )

    print("==============================")


def show_total(expenses):
    """Display total expenses."""
    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal Expenses: ₹{total:.2f}")


def show_category_summary(expenses):
    """Display spending grouped by category."""
    if not expenses:
        print("\nNo expenses found.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"]

    print("\n====== CATEGORY SUMMARY ======")

    for category, total in summary.items():
        print(f"{category}: ₹{total:.2f}")

    print("==============================")


def delete_expense(expenses):
    """Delete an expense."""
    view_expenses(expenses)

    if not expenses:
        return

    try:
        expense_number = int(input("Enter expense number to delete: "))

        if 1 <= expense_number <= len(expenses):
            removed = expenses.pop(expense_number - 1)
            save_expenses(expenses)

            print(f"Deleted: {removed['title']}")

        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    """Run the Expense Tracker application."""
    expenses = load_expenses()

    while True:
        print("\n========== EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Category Summary")
        print("5. Delete Expense")
        print("6. Exit")
        print("=====================================")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            show_total(expenses)

        elif choice == "4":
            show_category_summary(expenses)

        elif choice == "5":
            delete_expense(expenses)

        elif choice == "6":
            print("Thank you for using the Expense Tracker.")
            break

        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
```
