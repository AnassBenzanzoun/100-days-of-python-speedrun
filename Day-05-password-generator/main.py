# Password Generator Project
import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = "!#$%&()*+"

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


password = []
for i in range(0, nr_letters):
    password.append(random.choice(letters))

for i in range(0, nr_symbols):
    password.append(random.choice(symbols))

for i in range(0, nr_numbers):
    password.append(random.choice(numbers))
random.shuffle(password)
print(f"Your password is: {''.join(password)}")
