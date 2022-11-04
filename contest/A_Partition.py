size = int(input())

seq = list(map(int, input().split()))

B = 0
C = 0

for i in range(size):
    if seq[i] < 0:
        C += seq[i]
    else:
        B += seq[i]

print(B - C)