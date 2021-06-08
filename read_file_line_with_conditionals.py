afile = open("studentdata.txt", "r")

for aline in afile:
    a = aline.split()
    if len(a[1:]) > 6:
        print(a[0])

afile.close()
