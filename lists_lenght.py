#!/usr/bin/python3

fruit = ["apple", "orange", "banana", "cherry"]
a = [1, 2] + [3, 4]
b = fruit + [6, 7, 8, 9]

c = [0] * 4
d = [[1, 2], ["hello", "goodbye"]] * 2
e = a, b, c, d

for i in e:
    print("list", i)
    print("lenght of list", len(i))
