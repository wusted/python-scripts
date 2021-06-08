nested = ["hello", 2.0, 5, [10, 20]]
innerlist = nested[3]
print(innerlist)

# We could get the index from the innerlist variable created, that contains the list in the index 3 of nested
item1example = innerlist[0]
print(item1example)
# Or we could get the index 3 from nested variable first and get the item directly in the desired index.
item2example = (nested[3][1])
print(item2example)
