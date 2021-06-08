#!/usr/bin/python3

year = int(input("Please enter a year: "))
if year >= 1900 and year <= 2099:
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19*a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7
    dateofeaster = 22 + d + e

    if year == 1954 or year == 2981 or year == 2049 or  year == 2076:
        dateofeaster = dateofeaster - 7

    if dateofeaster > 31:
        print("April", dateofeaster - 31)
    else:
        print("March", dateofeaster)

else:
    print("ERROR...year out of range")