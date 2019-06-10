largest_now = -1
for nums in [34, 75, 39, 92, 74, 98, 23, 93]:
    if nums > largest_now:
        largest_now = nums
    print(largest_now, nums)
print('the largest is: ', largest_now)
