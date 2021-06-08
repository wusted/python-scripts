#!/usr/bin/python3

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

encrypted = "3fkkp &pqk2"

decrypted = decrypt(encrypted, cipher)
print(decrypted)