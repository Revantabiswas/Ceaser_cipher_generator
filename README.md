
# Caesar Cipher Python Script

This repository contains a Python implementation of the Caesar cipher, a simple encryption technique where each letter in the plaintext is shifted by a fixed number of positions in the alphabet.

## Features

- **Encode and Decode:** The script allows users to encode and decode text using the Caesar cipher.
- **Customizable Shifts:** Users can specify the number of shifts for the cipher.
- **User-Friendly Interface:** The script interacts with users through the command line, prompting them for inputs and providing clear feedback.

## How It Works

1. **Encoding/Decoding:** Users are prompted to choose whether they want to encode or decode a message.
2. **Input Text:** Users then input the text they wish to encode or decode.
3. **Shift Amount:** Users specify the number of shifts they want to apply.
4. **Output:** The script returns the encoded or decoded text.

## Usage

1. **Clone the Repository:**
   \`\`\`bash
   git clone https://github.com/Revantabiswas/Ceaser_cipher_generator.git
   cd caesar-cipher
   \`\`\`

2. **Run the Script:**
   \`\`\`bash
   python Ceaser_cipher_generator.py
   \`\`\`

3. **Follow the Prompts:**
   - Choose whether to encode or decode.
   - Enter the text you want to process.
   - Specify the number of shifts.

4. **Restart Option:**
   - After each operation, you’ll be asked if you want to restart the program.

## Example

\`\`\`bash
Type 'encode' to encrypt, Type 'decode' to decrypt
> encode
Enter the text
> hello
Enter the amount of shifts you want
> 3
The encode text is khoor
Do you want to restart the program? (yes/no)
> no
Thank you for using Caesar cipher.
\`\`\`

## Dependencies

- Python 3.x

The script uses the standard \`string\` module to handle alphabet operations.

## Contributing

Feel free to fork this repository and submit pull requests if you have any improvements or additional features you'd like to add.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
