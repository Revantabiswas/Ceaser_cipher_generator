from logo import logo 
print(logo)
import string
alphabets = list(string.ascii_lowercase)
def get_direction():
    while True:
        direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt\n").lower()
        if direction in ["encode", "decode"]:
            return direction
        else:
            print("Invalid input. Please type 'encode' or 'decode'.")

direction = get_direction()
text=input("Enter the text\n").lower()
shifts=int(input("Enter the amount of shifts you want\n"))

def ceaser(original_text,n_shift,directions):
  output_text=""
  for letter in original_text:
    if letter in alphabets:
      position=alphabets.index(letter)
      if directions=="encode":
        new_position=position+n_shift
        new_letter=alphabets[new_position]
        output_text+=new_letter
      elif directions=="decode":
        new_position=position-n_shift
        new_letter=alphabets[new_position]
        output_text+=new_letter
  print(f"The {direction} text is {output_text}")
ceaser(original_text=text,n_shift=shifts,directions=direction)


