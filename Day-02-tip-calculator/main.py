print("Welcome to the tip calculator.")
# If the bill was $150.00, split between 5 people, with 12% tip.
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
# Each person should pay (150.00 / 5) * 1.12 = 33.6
total = (float(bill) / int(people)) * (1 + float(tip) / 100)
# Format the result to 2 decimal places = 33.60
print(f"Each person should pay: ${total:.2f}")
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

# one line solution
# print(f"Welcome to the tip calculator.\n {int(input('how much was the bill?')) * float(input('how much tip would you like to give?'))/ 100 / int(input('how many people are splitting the bill?')):.2f}")
