f = open("studentdata.txt", "r")

for aline in f:
    items = aline.split()
    for i in range(len(items[1:])):
        items[i+1] = int(items[i+1])
    print(items[0], "max is", max(items[1:]), "min is", min(items[1:]))

f.close()
