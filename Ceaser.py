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
