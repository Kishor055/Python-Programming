```python
"""
Simple Calculator
-----------------
A beginner-friendly calculator project demonstrating:
- Functions
- User input
- Conditional statements
- Error handling
- Loops
"""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the division of two numbers."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def calculator():
    """Run the calculator application."""

    print("=" * 40)
    print(" SIMPLE CALCULATOR")
    print("=" * 40)

    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "5":
            print("\nThank you for using the calculator!")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice. Please select 1-5.")
            continue

        try:
            first_number = float(input("Enter first number: "))
            second_number = float(input("Enter second number: "))

            if choice == "1":
                result = add(first_number, second_number)
                operation = "+"

            elif choice == "2":
                result = subtract(first_number, second_number)
                operation = "-"

            elif choice == "3":
                result = multiply(first_number, second_number)
                operation = "×"

            else:
                result = divide(first_number, second_number)
                operation = "÷"

            print(
                f"\n Result: "
                f"{first_number:g} {operation} {second_number:g} = {result:g}"
            )

        except ValueError:
            print(" Please enter valid numbers.")

        except ZeroDivisionError as error:
            print(f" {error}")


if __name__ == "__main__":
    calculator()
```
