# Number Guessing Game
# Codveda Internship - Level 1
# Author: Chishibe Kabwe

import random

MAX_ATTEMPTS = 7


def display_welcome():
    print("=" * 45)
    print("         NUMBER GUESSING GAME")
    print("=" * 45)
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {MAX_ATTEMPTS} attempts. Good luck!\n")


def get_guess(attempt):
    while True:
        try:
            guess = int(input(f"Attempt {attempt}/{MAX_ATTEMPTS} - Enter your guess: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.\n")
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")


def give_hint(guess, secret):
    diff = abs(guess - secret)
    if diff <= 5:
        return "Very close!"
    elif diff <= 15:
        return "Getting warm."
    elif diff <= 30:
        return "Getting cooler."
    else:
        return "Way off."


def play_game():
    display_welcome()
    secret_number = random.randint(1, 100)
    attempts_used = 0

    for attempt in range(1, MAX_ATTEMPTS + 1):
        guess = get_guess(attempt)
        attempts_used += 1

        if guess == secret_number:
            print(f"\nCorrect! The number was {secret_number}.")
            print(f"You got it in {attempts_used} attempt(s).\n")
            return True
        elif guess < secret_number:
            print("Too low.")
        else:
            print("Too high.")

        print(give_hint(guess, secret_number))

        remaining = MAX_ATTEMPTS - attempt
        if remaining > 0:
            print(f"{remaining} attempt(s) remaining.\n")

    print(f"\nOut of attempts. The number was {secret_number}.")
    print("Better luck next time.\n")
    return False


def main():
    while True:
        play_game()
        print("-" * 45)
        again = input("Play again? (yes/no): ").strip().lower()
        print()
        if again not in ("yes", "y"):
            print("Thanks for playing. Goodbye.")
            print("=" * 45)
            break


if __name__ == "__main__":
    main()