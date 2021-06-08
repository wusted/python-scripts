words = ["adopt", "bake","talk", "beam", "confide","walk", "grill", "plant","start", "time", "wave", "wish"]
past_tense = []

for word in words:
    if word[-1] == "e":
        past_tense.append(word + "d")
    elif word[-1] != "e":
        past_tense.append(word + "ed")

print(past_tense)
