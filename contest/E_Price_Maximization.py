from math import remainder


cases = int(input())

for _ in range(cases):
    size, k = map(int, input().split())

    goods = list(map(int, input().split()))

    left = 0
    right = len(goods) - 1
    remains = 0
    modded = [ goods[i] % k for i in range(size)]
    modded.sort()

    while left <= right:
        currSum = modded[left] + modded[right] 

        if currSum >= k:
            remains += currSum % k
            right -= 1
        else:
            remains += modded[left]

        left += 1

    maxPrice = (sum(goods) - remains) // k
    
    print(maxPrice)

