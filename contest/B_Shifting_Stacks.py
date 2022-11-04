t = int(input())

for _ in range(t):
    n = int(input())
    heights = list(map(int, input().split()))
    can_increase = "YES"
    left = 0

    for i in range(n):
        left += heights[i] - i
        if left < 0:
            can_increase = "NO"

    print(can_increase)