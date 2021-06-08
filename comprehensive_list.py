mylist = [1,2,3,4,5]

yourlist = [item ** 2 for item in mylist]

print(yourlist)

yourlist = []
for item in mylist:
    yourlist = yourlist + [item ** 2]

print(yourlist)

alist = [4,2,8,6,5]
blist = [num*2 for num in alist if num%2==1]
print(blist)
