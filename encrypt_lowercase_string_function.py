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

encrypted = encrypt(input("Which string do you need to encrypt? "), cipher)
print(encrypted)