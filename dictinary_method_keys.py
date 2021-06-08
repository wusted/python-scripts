inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}

for akey in inventory.keys():   # the order in which we the key is not defined
    print("Got key", akey, "which maps to value", inventory[akey])

ks = list(inventory.keys())
print(ks)


# OR

for k in inventory:
    print("Got a key", k)
