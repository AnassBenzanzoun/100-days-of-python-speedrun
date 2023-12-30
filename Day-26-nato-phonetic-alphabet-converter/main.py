import pandas as pd

with open("nato_phonetic_alphabet.csv") as file:
    data = pd.read_csv(file)

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
name = input("Enter your name: ").upper()
name_list = [data_dict[letter] for letter in name if letter in data_dict]
print(" ".join(name_list))
