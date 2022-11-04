test = int(input())

for _ in range(test):
    numBoxes = int(input())
    candies = list(map(int,input().split()))
    
    minBox = min(candies)
    totalEaten = 0
    for candy in candies:
        totalEaten += candy - minBox

    print(totalEaten)