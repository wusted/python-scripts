inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
print("apples" in inventory)
print("cherries" in inventory)

if "bananas" in inventory:
    print(inventory["bananas"])
elif "bananas" not in inventory:
    print("We have no bananas")
if "cherries" in inventory:
    print(inventory["cherries"])
elif "cherries" not in inventory:
    print("We have no cherries")
