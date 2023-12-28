############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The Dealer is the dealer.

import random
import os
from logo import logo
from colorama import Fore, Style, init

init(autoreset=True)


def determine_result(player_score, dealer_score):
    if player_score > 21:
        return "You lose"
    elif dealer_score == 21:
        return "You lose"
    elif player_score == 21:
        return "You win"
    elif dealer_score > 21:
        return "You win"
    elif dealer_score > player_score:
        return "You lose"
    elif dealer_score == player_score:
        return "Draw"
    else:
        return "You win"


play_again = "y"
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while play_again == "y":
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.YELLOW + logo)

    player = [random.choice(cards), random.choice(cards)]
    dealer = [random.choice(cards), random.choice(cards)]

    player_score = sum(player)
    dealer_score = sum(dealer)

    # Handle edge case where player initially draws two Aces
    if player_score > 21 and player.count(11) > 0:
        player[player.index(11)] = 1
        player_score = sum(player)

    print(Fore.GREEN + f"Your cards: {player}, current score: {player_score}")
    print(Fore.RED + f"Dealer's first card: {dealer[0]}")

    while player_score < 21:
        if input("get another card? (y/n)") == "y":
            player.append(random.choice(cards))
            player_score = sum(player)
            print(Fore.GREEN + f"Your cards: {player}, current score: {player_score}")
            print(Fore.RED + f"Dealer's first card: {dealer[0]}")
            if player_score > 21 and player.count(11) > 0:
                player[player.index(11)] = 1
                player_score = sum(player)
                os.system("cls" if os.name == "nt" else "clear")
                print(Fore.YELLOW + logo)
                print(
                    Fore.GREEN
                    + f"updated your cards: {player} now ace is worth 1, current score: {player_score}"
                )
                print(Fore.RED + f"Dealer's first card: {dealer[0]}")
        else:
            break

    while dealer_score < 17:
        dealer.append(random.choice(cards))
        dealer_score = sum(dealer)

    print(Fore.RED + f"Dealer's cards: {dealer}, current score: {dealer_score}")

    result = determine_result(player_score, dealer_score)
    if "win" in result:
        print(Fore.GREEN + result)
    elif "lose" in result:
        print(Fore.RED + result)
    else:
        print(Fore.YELLOW + result)

    play_again = input("Play again? (y/n)")
