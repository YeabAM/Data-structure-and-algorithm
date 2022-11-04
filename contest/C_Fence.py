# def insertPiano(fence, piano_width):
#     fence_width = len(fence)
#     left_index = 0
#     answer = 1
#     min_width = float('inf')
#     running_sum = sum(fence[0:piano_width])
#     for right_index in range(piano_width, fence_width + 1):
#         if running_sum < min_width:
#             min_width = running_sum
#             answer = left_index + 1
        
#         if right_index < fence_width:
#             running_sum += fence[right_index]
#             running_sum -= fence[left_index]
#             left_index += 1

#     return answer

# length, piano_width = list(map(int, input().split()))
# fence = list(map(int, input().split()))
# answer = insertPiano(fence, piano_width)
# print(answer)

n, k = map(int, input().split())
planks = list(map(int, input().split()))

mini = float("inf")
idx = 0

for i in range(n - k):
    curr_sum = sum(planks[i: i + k])
    if mini > curr_sum:
        mini = curr_sum
        idx = i + 1

print(idx)