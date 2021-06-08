inventory = {"apples": 430, "bananas": 312, "oranges":512, "pears": 217}

print(inventory.get("apples"))
print(inventory.get("cherries"))

print(inventory.get("cherries", 0))
