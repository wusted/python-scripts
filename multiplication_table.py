#!/usr/bin/python3

n = int(input("Please enter a positive integer between 1 and 15: "))
for row in range(1, n +1):
    print(*(f"{row*col:3}" for col in range(1, n + 1)))
