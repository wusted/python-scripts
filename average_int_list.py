def average(numlist):
    total = 0
    for num in numlist:
        total = total + num

    return total / len(numlist)

print(average([2,3,4,5]))
