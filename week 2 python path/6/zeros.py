from collections import deque

def move_zero(nums):
    for i in nums:
        if i == 0:
            nums.remove(i)
            nums.append(i)
    print (nums)