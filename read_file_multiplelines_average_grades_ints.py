f = open("studentdata.txt", "r")

for aline in f:
    items = aline.split()
    total = 0
    grades = items[1:]
    for grade in grades:
        total = total + int(grade)

    print(items[0], total/(len(grades)))
