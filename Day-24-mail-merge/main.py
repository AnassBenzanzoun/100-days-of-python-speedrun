# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name], [date], [time], [address] and [yourname] placeholders with your stuff.
# Save the letters in the folder "ReadyToSend".

name, date, time, address, myName = (
    "",
    "Monday 8th",
    "10:00",
    "123 Street",
    "Anass",
)
activities = """
1. Watching paint dry competition
2. Extreme paperclip collecting
3. Competitive napping championship
4. Professional bubble wrap popping contest
5. Competitive staring contest with statues
6. Competitive knitting of mismatched socks
7. Marshmallow eating competition without using hands
8. Competitive puzzle solving with missing pieces
9. Slow-motion race for snails
10. Dramatic reenactment of a plant growing
"""


with open("./Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()

with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

for name in names_list:
    stripped_name = name.strip()
    new_letter = letter_content.replace("[name]", stripped_name)
    new_letter = new_letter.replace("[activities]", activities)
    new_letter = new_letter.replace("[date]", date)
    new_letter = new_letter.replace("[time]", time)
    new_letter = new_letter.replace("[address]", address)
    new_letter = new_letter.replace("[myName]", myName)
    with open(
        f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w"
    ) as completed_letter:
        completed_letter.write(new_letter)
