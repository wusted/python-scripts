sentence = input("Please enter a sentence: ")

sentence = sentence.lower()   # convert to all lowercase

alphabet = "abcdefghijklmnopqrstuvwxyz"

letter_count = {}   # empty dictionary
for char in sentence:
    if char in alphabet:    # ignore punctuation, numbers, etc
        if char in letter_count:
            letter_count[char] = letter_count[char] + 1
        else:
            letter_count[char] = 1


keys = letter_count.keys()
for char in sorted(keys):
    print(char, letter_count[char])
