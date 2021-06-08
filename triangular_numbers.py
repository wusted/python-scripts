#!/usr/bin/python3

def print_triangular_numbers(n):
    for i in range(1, n + 1 ):
        print(i, "\t", (i ** 2 + i)//2 )

print_triangular_numbers(int(input("Please enter how many triangular numbers you want to print: "))) 