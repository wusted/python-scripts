#!/usr/bin/python3

def remove_dups(astring):
    temp = ""

    for i in astring:
        if i in temp:
            temp = temp
        elif i not in temp:
            temp += i
    return temp

print(remove_dups("mississippi"))
