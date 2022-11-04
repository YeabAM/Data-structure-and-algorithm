from collections import defaultdict
from math import ceil


testCase = int(input())

for _ in range(testCase):
    size = int(input())

    nums = list(map(int, input().split()))
    difCount = defaultdict(int)
    maxCount = float("-inf")
    for i, n in enumerate(nums):
        difCount[n - i] += 1

    totalCount = 0
    for dif in difCount:
        temp = difCount[dif] - 1
        totalCount += (temp * (temp + 1)) // 2

    print(totalCount)

    
