mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

mylist.insert(1, 12)
print(mylist)
print(mylist.count(12))

print(mylist.index(3))
print(mylist.count(5))

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

mylist.remove(5)
print(mylist)

lastitem = mylist.pop(2)
print(lastitem)
print(mylist)

error = mylist.sort()
print(error)

poplist = [5, 27, 3, 12]
poplist = poplist.pop(0)
print(poplist)
