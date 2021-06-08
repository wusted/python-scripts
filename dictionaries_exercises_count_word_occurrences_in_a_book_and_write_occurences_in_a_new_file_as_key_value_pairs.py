file = open("greeks.txt", "r")

count = {}

for line in file:
    for word in line.split():

        ### Remove puntuactuion for each word in line
        word = word.replace("_", "").replace('"', "").replace(",", "").replace(".", "")
        word = word.replace("-", "").replace("?", "").replace("!", "").replace("'", "")
        word = word.replace("(", "").replace(")", "").replace(":", "").replace("[", "")
        word = word.replace("]", "").replace(";", "")

        ### Make it Lowercase, for simpler classification
        word = word.lower()

        ### ignore numbers, since this is to count only letters, and start counting
        if word.isalpha():
            if word in count:
                count[word] = count[word] + 1   # Add up in every occurence
            else:
                count[word] = 1                 # Remain in 1


### Sort the keys, which are the letters.

keys = count.keys()

### save the word count analysis to a new file
out = open("greeks_words_count.txt", "w")

for word in keys:
    out.write(word + " " + str(count[word]))
    out.write("\n")

print("The word 'greeks' appears " + str(count["greeks"]) + " times in the book.")

