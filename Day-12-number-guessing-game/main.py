import random
import os
from colorama import Fore, Style, init

init(autoreset=True)


# Function - play_game - handle game logic
def play_game(possible_attempts):
    number = random.randint(1, 101)
    guess = 0
    attempts = 0
    while guess != number and attempts < possible_attempts:
        guess = int(input(Fore.BLUE + "Make a guess: "))
        attempts += 1
        if guess > number:
            print(Fore.RED + f"Too high. Attempts left {possible_attempts - attempts}")
        elif guess < number:
            print(Fore.RED + f"Too low. Attempts left {possible_attempts - attempts}")
        else:
            print(Fore.GREEN + f"You got it! The answer was {number}")
            return
    print(Fore.RED + "you have no more attempts left. You lose.")


# Main - handle game loop and user input
play_again = "y"
possible_attempts = 8
while play_again == "y":
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.YELLOW + "Welcome to the Number Guessing Game!")
    print(Fore.YELLOW + "I'm thinking of a number between 1 and 100.")
    print(Fore.YELLOW + f"you have {possible_attempts} attempts to guess the number")
    play_game(possible_attempts)
    play_again = input(Fore.YELLOW + "Do you want to play again? (y/n): ")
