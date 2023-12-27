import os

auction = {}
other_bidders = "yes"
while other_bidders == "yes":
    # Clear the terminal (works in command line interface only)
    os.system("cls" if os.name == "nt" else "clear")
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))
    auction[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

# Find the key with the highest value in the auction dictionary
winner = max(auction, key=auction.get)
print(f"aaand the winner iiiiis {winner} with a bid of ${auction[winner]}.")
print(f"name of the people who partecipated {' '.join(auction.keys())}")
