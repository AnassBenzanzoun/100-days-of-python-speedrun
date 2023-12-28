import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = {1: rock, 2: paper, 3: scissors}
# do a dictionary that maps the possible outcomes based on the player and computer choices
outcomes = {
    "11": "Draw",
    "12": "Computer wins",
    "13": "Player wins",
    "21": "Player wins",
    "22": "Draw",
    "23": "Computer wins",
    "31": "Computer wins",
    "32": "Player wins",
    "33": "Draw",
}
computer_choice = random.randint(1, 3)
while True:
    try:
        player_choice = int(
            input(
                "What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors.\n"
            )
        )
        if player_choice in [1, 2, 3]:
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 3.")
    except ValueError:
        print("Invalid input. Please enter a number.")

print(f"You chose {choices[player_choice]}")
print(f"Computer chose {choices[computer_choice]}")
result = outcomes[str(player_choice) + str(computer_choice)]
print(result)
