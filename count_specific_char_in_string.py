#!/usr/bin/python3

def count(p):
    lows = "abcdefghijklmnopqrstuvwxyz"
    ups = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    numberOfe = 0
    totalChars = 0
    for achar in p:
        if achar in lows or ups:
            totalChars = totalChars + 1
            if achar == "e":
                numberOfe = numberOfe + 1

    percent_with_e = (numberOfe / totalChars) * 100
    print("Your text contains", totalChars, "alphabetic characters of which", numberOfe, "(",f"{percent_with_e:.2f}", "%) are 'e'.")

p = '''
"If the automobile had followed the same development cycle as the computer, a
Rolls-Royce would today cost $100, get a million miles per gallon, and explode
once a year, killing everyone inside."
-Robert Cringely
'''

count(p)

