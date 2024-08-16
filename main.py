from logo import logo 
print(logo)
import string
alphabets = list(string.ascii_lowercase)

def caesar(original_text, n_shift, directions):
    output_text = ""
    for letter in original_text:
        if letter in alphabets:
            position = alphabets.index(letter)
            if directions == "encode":
                new_position = (position + n_shift) % len(alphabets)
            elif directions == "decode":
                new_position = (position - n_shift) % len(alphabets)
            new_letter = alphabets[new_position]
            output_text += new_letter
        else:
            output_text += letter
    print(f"The {directions} text is {output_text}")

def get_direction():
    while True:
        direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt\n").lower()
        if direction in ["encode", "decode"]:
            return direction
        else:
            print("Invalid input. Please type 'encode' or 'decode'.")

# Main program loop
should_end = False
while not should_end:
    direction = get_direction()
    text = input("Enter the text\n").lower()
    
    while True:
        try:
            shifts = int(input("Enter the amount of shifts you want\n"))
            break
        except ValueError:
            print("Invalid input. Please enter an integer for the shifts.")

    # Call the caesar function
    caesar(original_text=text, n_shift=shifts, directions=direction)
    
    restart = input("Do you want to restart the program? (yes/no)\n").lower()
    if restart == 'no':
        should_end = True
        print("Thank you for using Caesar cipher.")
