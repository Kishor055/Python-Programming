```python
"""
Number Guessing Game

The computer randomly selects a number between 1 and 100.
The player keeps guessing until the correct number is found.
"""

import random


def get_valid_guess():
    """Return a valid guess between 1 and 100."""
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))

            if 1 <= guess <= 100:
                return guess

            print("Please enter a number between 1 and 100.")

        except ValueError:
            print("Please enter a valid whole number.")


def play_game():
    """Play one round of the guessing game."""
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI'm thinking of a number between 1 and 100!")

    while True:
        guess = get_valid_guess()
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")

        elif guess > secret_number:
            print("Too high! Try again.")

        else:
            print("\nCongratulations!")
            print(f"You guessed the number: {secret_number}")
            print(f"Attempts: {attempts}")
            return


def main():
    """Run the game and handle replay."""
    print("=" * 40)
    print("     NUMBER GUESSING GAME")
    print("=" * 40)

    while True:
        play_game()

        choice = input("\nPlay again? (y/n): ").strip().lower()

        if choice != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
```
