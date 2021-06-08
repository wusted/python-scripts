scores = [85, 95, 70]
result = ''
for score in scores[:-1]:
    result = result + str(score) + ", "

result = result + "and " +  str(scores[-1]) + "."
        
        
print("The scores are " + result)
