def listsum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    elif len(numlist) > 1:
        return numlist[0] + listsum(numlist[1:])

print(listsum([1, 3, 5 , 7, 9]))
