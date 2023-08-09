sentence = input("Please enter a sentence: ").lower()
encrypted_text = ""
shift = 5
for char in sentence:
        if char.isalpha():  
            ascii_offset = ord("A") if char.isupper() else ord("a")
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
print("The encrypted sentence is: ", encrypted_text)
    









