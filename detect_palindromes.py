#!/usr/bin/python3

def reverse(mystr):
    reversed = ""
    for char in mystr:
        reversed = char + reversed
    return reversed

def is_palindrome(myStr):
    if myStr in reverse(myStr):
        return True
    elif myStr not in reverse(myStr):
        return False

print(is_palindrome("abba"))
print(is_palindrome("abab"))
print(is_palindrome("straw warts"))
print(is_palindrome("a"))
print(is_palindrome(""))
