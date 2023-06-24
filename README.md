# Encryption and Decryption Script

This is a Python script that allows you to encrypt or decrypt a given text using a shift cipher. The script prompts the user to choose the mode (encryption or decryption), enter the shift key, and provide the input text. It then performs the chosen operation and writes the result to an output file.

## Usage

1. Make sure you have Python installed on your system.
2. Copy and save the code into a file with a `.py` extension, e.g., `Ceaser.py`.
3. Open a terminal or command prompt and navigate to the directory where you saved the script.
4. Run the script using the command: `python Ceaser.py`.
5. Follow the prompts to choose the mode, enter the shift key, text, and output file name.
6. The script will encrypt or decrypt the text based on the chosen mode and save the result in the specified output file.

## Code

```python
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shifted_char = ord(char) + shift
            if char.islower():
                result += chr((shifted_char - 97) % 26 + 97)
            else:
                result += chr((shifted_char - 65) % 26 + 65)
        else:
            result += char
    return result

def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shifted_char = ord(char) - shift
            if char.islower():
                result += chr((shifted_char - 97) % 26 + 97)
            else:
                result += chr((shifted_char - 65) % 26 + 65)
        else:
            result += char
    return result

mode = input("Do you want to encrypt or decrypt? ")
shift = int(input("Enter the shift key: "))
text = input("Enter the text: ")

if mode == "encrypt":
    result = encrypt(text, shift)
elif mode == "decrypt":
    result = decrypt(text, shift)

filename = input("Enter the name of the output file: ")
with open(filename, "w") as f:
    f.write(result)
```
## Encryption and Decryption Process

The script uses a shift cipher algorithm to encrypt or decrypt the text. The algorithm works as follows:

- For encryption:
  - Each alphabetic character in the input text is shifted by the specified `shift` value.
  - The shifted character is determined by adding the `shift` value to the character's Unicode code point.
  - If the character is lowercase, the shifted value is wrapped around within the lowercase range (97-122), ensuring it stays within valid lowercase characters.
  - If the character is uppercase, the shifted value is wrapped around within the uppercase range (65-90), ensuring it stays within valid uppercase characters.
  - Non-alphabetic characters are unchanged and appended to the result as they are.

- For decryption:
  - Each alphabetic character in the input text is shifted back by the specified `shift` value.
  - The shifted character is determined by subtracting the `shift` value from the character's Unicode code point.
  - Similar to encryption, the shifted value is wrapped around within the lowercase or uppercase range, based on the character's case.
  - Non-alphabetic characters are unchanged and appended to the result as they are.

