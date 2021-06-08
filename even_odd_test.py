#!/usr/bin/python3

test_numbers = [10, 5, 1, 0]

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def is_odd(n):
    if n % 2 != 0:
        return True
    else:
        return False


def test_even_odd(numbers):
    print ("Event test", numbers)
    for i in numbers:
        even = is_even(i)
        if even is True:
            print ("True")
        else:
            print("False")
    print ("Odd test", numbers)
    for i in numbers:
        odd = is_odd(i)
        if odd is True:
            print("True")
        else:
            print("False")

test_even_odd(test_numbers)