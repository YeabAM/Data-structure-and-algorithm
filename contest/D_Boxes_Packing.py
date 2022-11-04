import heapq


boxSize = int(input())

boxes = list(map(int, input().split()))

boxes.sort()

heap = []

for i in range(boxSize):
    if heap and heap[0] < boxes[i]:
        heapq.heappop(heap)
    heapq.heappush(heap, boxes[i])
    # print(heap, i)
print(len(heap))