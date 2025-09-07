from random import randint
from name_art import logo

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5


def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1

    else:
        print(f"You got it! The answer was {actual_answer}")


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("i'm thinking of a number between 1 and 100.")


game()


def difficulty():
    difficulty_level = input("choose a difficulty. Type 'easy' or 'hard: ")
    if difficulty_level == "easy":
        return EASY_LEVEL_TURN
    elif difficulty_level == "hard":
        return HARD_LEVEL_TURN
    else:
        return "invalid! input"


answer = randint(1, 100)
turns = difficulty()
guess = 0

while guess != answer:
    print(f"you have {turns} attempts remaining to guess the number.")
    guess = int(input("make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
        print("You've run out of guesses, you lose.")

    elif guess != answer:
        print("Guess again.")
    else:
        print("game over")

