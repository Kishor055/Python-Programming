```python
"""
Password Generator
-------------------
Generates secure random passwords using Python's secrets module.
"""

import secrets
import string


MIN_LENGTH = 8
MAX_LENGTH = 128


def get_password_length():
    """Get a valid password length from the user."""
    while True:
        try:
            length = int(
                input(f"Enter password length ({MIN_LENGTH}-{MAX_LENGTH}): ")
            )

            if MIN_LENGTH <= length <= MAX_LENGTH:
                return length

            print(
                f"Please enter a length between "
                f"{MIN_LENGTH} and {MAX_LENGTH}."
            )

        except ValueError:
            print("Please enter a valid whole number.")


def generate_password(length):
    """Generate a secure random password."""
    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    return "".join(
        secrets.choice(characters)
        for _ in range(length)
    )


def main():
    """Run the password generator."""
    print("=" * 45)
    print("        PASSWORD GENERATOR")
    print("=" * 45)

    length = get_password_length()
    password = generate_password(length)

    print("\nGenerated Password:")
    print(password)


if __name__ == "__main__":
    main()
```
