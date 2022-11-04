size = int(input())

pylons = list(map(int, input().split()))
height = [0]

for i in range(size):
    height.append(pylons[i])

print(max(height))