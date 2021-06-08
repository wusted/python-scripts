#!/usr/bin/python3


def getGrade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80 and mark <90:
        return "B"
    elif mark >= 70 and mark <80:
        return "C"
    elif mark >= 60 and mark <70:
        return "D"
    else:
        return "F"

a = 95
b1 = 85
d = 65
c = 79.9999
b2 = 80

for marks in [a,b1,d,c,b2]:
    result = getGrade(marks)
    print ("Mark:",marks," - ","Grade:", result)
