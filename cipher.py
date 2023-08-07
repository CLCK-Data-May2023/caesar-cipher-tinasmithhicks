def caesar_cipher(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():  # check if the character is an alphabet
            # find the position of the character in the alphabet (0-25)
            position = ord(char) - ord('a' if char.islower() else 'A')
            # shift the position
            new_position = (position + shift) % 26
            # add the shifted character to the encrypted text
            encrypted_text += chr(new_position + ord('a' if char.islower() else 'A'))
        else:
            encrypted_text += char
    
    return encrypted_text

# Test the function
plaintext = "programming python is fun!"
shift = 5
encrypted_text = caesar_cipher(plaintext, shift)
print(f"Plaintext: {plaintext}")
print(f"Encrypted text: {encrypted_text}")







