recipe, k, q = map(int, input().split())

prefixSum = [0 for _ in range(200002)]


for _ in range(recipe):
    left, right = map(int, input().split())
    prefixSum[left] += 1
    if right + 1 < len(prefixSum):
        prefixSum[right + 1] -= 1
# print("before",prefixSum)
for i in range(1, len(prefixSum)):
    prefixSum[i] += prefixSum[i - 1]

for i in range(1, len(prefixSum)):
    if prefixSum[i] >= k:
        prefixSum[i] = 1
    else:
        prefixSum[i] = 0

for i in range(1, len(prefixSum)):
    prefixSum[i] += prefixSum[i - 1]


for _ in range(q):
    l, r = map(int, input().split())
    print(prefixSum[r] - prefixSum[l-1])













































# for _ in range(q):
#     count = 0

    