alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    if new_position>25:
      new_position-=26
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")


def decrypt(text,shift):
  new_text=""
  for let in text:
    position = alphabet.index(let)
    new_position=position-shift
    letter=alphabet[new_position]
    new_text+=letter
  print(f"The decoded text is {new_text}")


if direction=="encode":
  encrypt(plain_text=text, shift_amount=shift)

if direction=="decode":
  decrypt(text,shift)