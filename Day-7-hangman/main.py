import random
from hangman_words import word_list
from hangman_ascii import logo, stages
from colorama import Fore, Style

# Setup game variables
chosen_word = random.choice(word_list)
end_of_game = False
lives = 6
display = ["_" for _ in range(len(chosen_word))]

print(Fore.RED + logo + Style.RESET_ALL)

# Main game loop
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check if letter has been guessed, if not update display
    if guess in display:
        print(f"You've already guessed {guess}")
    else:
        for position, letter in enumerate(chosen_word):
            if letter == guess:
                display[position] = letter

    # If guess is wrong, decrease lives
    if guess not in chosen_word:
        print(
            Fore.RED
            + f"You guessed {guess}, that's not in the word. You lose a life."
            + Style.RESET_ALL
        )
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(Fore.RED + f"The word was {chosen_word}" + Style.RESET_ALL)
            print(Fore.RED + "You lose." + Style.RESET_ALL)

    print(f"{' '.join(display)}")

    # Check if game is won
    if "_" not in display:
        end_of_game = True
        print(Fore.GREEN + "You win." + Style.RESET_ALL)
    # Print the hangman
    print(Fore.RED + stages[lives] + Style.RESET_ALL)
