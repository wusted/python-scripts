song = "The rain in Spain..." 
song_split = song.split()
print(song_split)

song_split_delim = song.split("ai")
print(song_split_delim)

print(song)

alist = ["red", "blue", "green"]
glue = ";"
new_list = (glue.join(alist))
print(new_list)

print("***".join(alist))
print("".join(alist))

print(alist)


blist = "Edgar Allan Poe"
newlist = blist.split()

mylist = ""
for aname in newlist:
    mylist = mylist + aname[0]
print(mylist)
