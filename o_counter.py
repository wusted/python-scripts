word = "onomatopoeia"

o_count = 0

for c in word:
    if c == "o":
        o_count = o_count + 1


print("There are " + str(o_count) + " o's in " +  word)
