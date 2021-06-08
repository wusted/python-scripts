s = "what if we went to the zoo"
num_vowels = 0
s_vowels = []

for i in s:
    if i in ["a", "e", "i", "o", "u"]:
        num_vowels += 1
        s_vowels += [i]

print(s_vowels)
print(num_vowels)
