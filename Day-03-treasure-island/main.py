print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)


# Write your code below this line 👇

print(
    "\033[91mWelcome to Treasure Island! Your mission is to find the treasure.\033[0m"
)

print("\nYou're standing at a crossroads.")
print(
    "You see a path going \033[91mleft\033[0m and another path going \033[91mright\033[0m."
)
direction = input(
    "Which way do you choose? \033[91mLeft\033[0m or \033[91mRight\033[0m? "
).lower()

if direction == "left":
    print("\nYou chose to go \033[91mleft\033[0m.")

    # Something good
    print("\nYou found a hidden stash of supplies! They will be useful.")
    print("You gather the supplies and move forward.")

    print(
        "In front of you, there are two ancient doors: one with intricate carvings and another with mystical runes."
    )
    print("You must choose a door to proceed.")
    print("But beware, each door might lead you to your fate.")

    door_choice = input(
        "Choose a door (\033[91mCarved\033[0m / \033[91mRuned\033[0m): "
    ).lower()

    if door_choice == "carved":
        print(
            "\nYou open the \033[91mcarved\033[0m door and find yourself in a majestic chamber."
        )
        print(
            "At the center, a mirror stands reflecting your determination and curiosity."
        )
        print("You realize the true treasure is your resilience and self-discovery.")
        print("Suddenly, a dragon appears! It bows to you and takes you on its back.")
        print(
            "With a mighty flap of its wings, the dragon carries you to the treasure. \033[91mCongratulations! You've won!\033[0m"
        )
    elif door_choice == "runed":
        print(
            "\nAs you step through the \033[91mruned\033[0m door, darkness envelops you."
        )
        print("A mysterious force transports you to an unknown realm.")
        print("\033[91mYou find yourself lost, never to return. Game over.\033[0m")
    else:
        print(
            "\nYou hesitated, unsure of the choices. You pause and realize waiting was your path to victory!"
        )
        print(
            "\033[91mAt that moment, a magnificent dragon appears and takes you on a journey to the treasure. Congratulations! You've won!\033[0m"
        )

elif direction == "right":
    print("\nYou chose to go \033[91mright\033[0m.")

    # Something bad
    print("\nA wild animal blocks your path! It's too dangerous to proceed.")
    print("\033[91mYou try to go back, but the animal attacks. Game over.\033[0m")

else:
    print("\n\033[91mYou didn't choose a path. Time runs out. Game over.\033[0m")
