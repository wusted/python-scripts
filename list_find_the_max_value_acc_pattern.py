nums = [9, 3 ,8, 11, 5, 29, 2]
best_num = nums[0]

for n in nums:
    if n > best_num:
        best_num = n

print(best_num)
