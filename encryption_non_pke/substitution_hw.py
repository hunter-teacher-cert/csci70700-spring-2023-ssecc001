#this is the alphabet that the program can draw from in order to match to the key
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#the key corresponds directly with each letter in the alphabet. In this substitution cipher, a is substituted with c and b with f
key = "QWERTYUIOPLKJHGFDSAZXCVBNM"
#the text is the text that the cipher will run through in order to make the substitutions 
text = "Susie is on Vacation"

encrypted_text = ""
for letter in text:

    if letter.upper() in alphabet:
        encrypted_text += key[alphabet.find(letter.upper())]
    else:
        encrypted_text += letter

print(encrypted_text)


decrypted_text = ""
for letter in encrypted_text:
    if letter.upper() in key:
        decrypted_text += alphabet[key.find(letter.upper())]

    else:
        decrypted_text += letter
print("This is the decrypted message " + decrypted_text)
