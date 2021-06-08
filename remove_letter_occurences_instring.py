#!/usr/bin/python3

def remove_letter(theLetter, theString):
    return theString.replace(theLetter,"")

Estring = remove_letter("e", "the letter will be removed")
print(Estring)