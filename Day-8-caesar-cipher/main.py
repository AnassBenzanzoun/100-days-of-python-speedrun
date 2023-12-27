alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceasar(text, shift, direction):
    # Define encoding and decoding methods
    enc_method = {
        "encode": lambda x, y: (x + y) % 26,
        "decode": lambda x, y: (x - y) % 26,
    }
    final_text = ""
    for letter in text:
        position = alphabet.index(letter)
        final_text += alphabet[enc_method[direction](position, shift)]
    print(f"The {direction}d text is {final_text}")


ceasar(text, shift, direction)
