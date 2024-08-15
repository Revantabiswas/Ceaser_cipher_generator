from logo import logo 
print(logo)
import string
alphabets = list(string.ascii_lowercase)
direction=input("Type'encode' to encrypt,Type 'decode' to decrypt\n")
text=input("Enter the text\n").lower()
shifts=int(input("Enter the amount of shifts you want\n"))



def encrypt(plain_text,n_shift):
  
  encrypted_text = ""
  for letter in plain_text:
    position=alphabets.index(letter)
    new_position=position + n_shift
    new_letter=alphabets[new_position]
    encrypted_text += new_letter
  print(f'The encoded text is {encrypted_text}')

def decrypt(cipher_text,nshift):
  
  decrypted_text = ""
  for letter in cipher_text:
    position=alphabets.index(letter)
    new_position = position - nshift
    decrypted_text += alphabets[new_position]
  print(f"The decoded text is {decrypted_text}")
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
if direction=="encode":
   encrypt(plain_text=text,n_shift=shifts)
elif direction=="decode":
  decrypt(cipher_text=text,nshift=shifts)


