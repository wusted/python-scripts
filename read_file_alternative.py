infile = open("qbdata.txt", "r")
line = infile.readline()

while line:
    values = line.split()
    print("QB", values[0], values[1], "had a rating of ", values[10])
    line = infile.readline()

infile.close()

