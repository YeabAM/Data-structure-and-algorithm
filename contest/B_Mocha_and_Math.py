cases = int(input())

for _ in range(cases):
    size = int(input())
    nums = list(map(int, input().split()))

    minm = nums[0]

    for i in range(1, size):
        minm = minm & nums[i]

    print(minm)