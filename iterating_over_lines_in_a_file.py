"""Path is relative to where I'm in the terminal when running the script, not to where the file is located"""

qbfile = open("qbdata.txt", "r")

for aline in qbfile:
    values = aline.split()
    print("QB", values[0], values[1], "had a rating of", values[10])

qbfile.close()
