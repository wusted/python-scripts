def doubleStuff(alist):
    for position in range(len(alist)):
        alist[position] = alist[position] * 2


thislist = [2, 5, 9]
print(thislist)
doubleStuff(thislist)
print(thislist)
