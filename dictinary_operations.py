inventory1 = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
del inventory1["pears"]
print(inventory1)

inventory2 = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
inventory2["pears"] = 0
print(inventory2)

inventory3 = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
inventory3["bananas"] = inventory3["bananas"] + 200
print(inventory3)
print(len(inventory3))

mydict = {"cat": 12, "dog": 6, "elephant":23}
print(mydict)
mydict["mouse"] = mydict["cat"] + mydict["dog"]
print(mydict["mouse"])
print(mydict)
