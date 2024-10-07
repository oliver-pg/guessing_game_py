"""Python number guessing game! Pick x-y number within z tries!"""

import random
from typing import Tuple


def print_introduction(max_guesses: int, min_number: int, max_number: int) -> None:
    """Print the introduction to the game, with the maximum number of guesses displayed."""
    print(
        f"Welcome to the guessing game! I'm thinking of a number between "
        f"{min_number} and {max_number}."
    )
    print(f"You have {max_guesses} attempts to choose the correct number.")


def print_guesses(guess_count: int) -> None:
    """Print how many times the player has guessed."""
    if guess_count == 1:
        print(f"You have guessed {guess_count} time.")
    else:
        print(f"You have guessed {guess_count} times.")


def print_remaining_guesses(guess_count: int, max_guesses: int) -> None:
    """Print the remaining number of guesses left."""
    attempts_left = max_guesses - guess_count
    if attempts_left > 0:
        print(f"You have {attempts_left} attempt(s) left.")
    else:
        print("This was your last attempt.")


def print_winning_message(guess_count: int, winning_number: int) -> None:
    """Print the winning message if the player guesses the correct number."""
    attempt_word = "try" if guess_count == 1 else "tries"
    print(
        f"Congratulations! You guessed the winning number: {winning_number} in "
        f"{guess_count} {attempt_word}!"
    )


def get_number_range() -> Tuple[int, int]:
    """Get the minimum and maximum numbers for the guessing range."""
    try:
        min_number = int(input("Enter the minimum number (default is 1): ") or 1)
        max_number = int(input("Enter the maximum number (default is 100): ") or 100)
        if min_number >= max_number:
            print(
                "Minimum number should be less than the maximum. Using "
                "defaults 1 and 100."
            )
            min_number, max_number = 1, 100
    except ValueError:
        print("Invalid input. Using default numbers 1 and 100.")
        min_number, max_number = 1, 100
    return min_number, max_number


def get_max_guesses() -> int:
    """Get the maximum number of guesses allowed."""
    try:
        max_guesses_input = input(
            "Enter the number of guesses you want (default is 3): "
        )
        if max_guesses_input.strip() == "":
            max_guesses = 3
        else:
            max_guesses_input = int(max_guesses_input)
            if max_guesses_input <= 0:
                print(
                    "Please enter a positive integer. Using default number of "
                    "attempts (3)."
                )
                max_guesses = 3
            else:
                max_guesses = max_guesses_input
    except ValueError:
        print("Invalid input. Using default number of attempts (3).")
        max_guesses = 3
    return max_guesses


def get_user_guess(min_number: int, max_number: int) -> int:
    """Prompt the user to enter a guess within the specified range."""
    while True:
        try:
            number_choice = int(input(f"Choose a number ({min_number}-{max_number}): "))
            if not min_number <= number_choice <= max_number:
                print(f"Please enter a number between {min_number} and {max_number}.")
            else:
                return number_choice
        except ValueError:
            print(
                f"Invalid input. Please enter an integer between {min_number} and {max_number}."
            )


def evaluate_guess(number_choice: int, winning_number: int) -> bool:
    """Compare the user's guess with the winning number and provide feedback."""
    if number_choice > winning_number:
        print("Too high!")
    elif number_choice < winning_number:
        print("Too low!")
    else:
        return True  # The guess is correct
    if abs(number_choice - winning_number) <= 5:
        print("You're very close!")
    return False  # The guess is incorrect


def play_game(
    min_number: int, max_number: int, max_guesses: int, winning_number: int
) -> None:
    """Play the main guessing game loop."""
    guess_count = 0
    while guess_count < max_guesses:
        number_choice = get_user_guess(min_number, max_number)
        guess_count += 1
        correct = evaluate_guess(number_choice, winning_number)
        if correct:
            print_winning_message(guess_count, winning_number)
            return
        print_guesses(guess_count)
        print_remaining_guesses(guess_count, max_guesses)
    else:
        print(f"The winning number was: {winning_number}")


def guessing_game() -> None:
    """Main game logic."""
    min_number, max_number = get_number_range()
    winning_number = random.randint(min_number, max_number)
    max_guesses = get_max_guesses()
    print_introduction(max_guesses, min_number, max_number)
    play_game(min_number, max_number, max_guesses, winning_number)


def main() -> None:
    """Execute the game loop here, in main."""
    while True:
        guessing_game()
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != "y":
            print("Thank you for playing!")
            break


if __name__ == "__main__":
    main()
