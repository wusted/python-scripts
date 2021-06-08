#!/usr/bin/python3

def encrypt(message, cipher):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    for char in message:
        if char == " ":
            encrypted = encrypted + " "
        else:
            pos = alphabet.index(char)
            encrypted = encrypted + cipher[pos]
    return encrypted

cipher = "b#42fe$3j8lk5@p6^qt7*u&w9y"

def decrypt(encrypted, cipher):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decrypted = ""
    for char in encrypted:
        if char == " ":
            decrypted = decrypted +  " "
        else:
            pos = cipher.index(char)
            decrypted = decrypted + alphabet[pos]
    return decrypted

cipher = "b#42fe$3j8lk5@p6^qt7*u&w9y"

encrypted = encrypt(input("Which string do you need to encrypt? "), cipher)
print(encrypted)

yes_or_no = input("Dou you want to decrypt it? Yes/No ")
if yes_or_no == "Yes":
    decrypted = decrypt(encrypted, cipher)
    print(decrypted)    
elif yes_or_no == "No":
    print("Too bad, run again and select Yes to decrypt :) ")
else:
    print("Not a valid option selected, run again and select Yes or No")

