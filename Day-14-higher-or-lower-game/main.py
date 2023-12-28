from game_data import data
import random
import os
from colorama import Fore, Style, init

init(autoreset=True)


def format_print(celebrity):
    print(
        Fore.BLUE
        + f"{celebrity['name']}, a {celebrity['description']} from {celebrity['country']}"
    )


def check_guess(guess, celebrity_a, celebrity_b):
    if guess == "a" and celebrity_a["follower_count"] > celebrity_b["follower_count"]:
        return True
    elif guess == "b" and celebrity_b["follower_count"] > celebrity_a["follower_count"]:
        return True
    return False


SCORE = 0
guessed_wrong = False
os.system("cls" if os.name == "nt" else "clear")

while not guessed_wrong:
    celebrity_a = random.choice(data)
    celebrity_b = random.choice(data)
    format_print(celebrity_a)
    print(Fore.YELLOW + "vs")
    format_print(celebrity_b)

    guess = input(Fore.BLUE + "Who has more followers? Type 'A' or 'B': ").lower()
    if check_guess(guess, celebrity_a, celebrity_b):
        SCORE += 1
        print(Fore.GREEN + f"You're right! Current score: {SCORE}")
    else:
        print(Fore.RED + f"Sorry, that's wrong. Final score: {SCORE}")
        guessed_wrong = True
