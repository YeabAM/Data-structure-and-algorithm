# n = int(input())
# front = {}
# back = {}

# for _ in range(n):
#     a, b = list(map(int, input().split()))
#     front[a] = b
#     back[b] = a

# queue = [0]*(n)
# start = 0
# # print(back, 'b')
# #first student
# for std in front:
    
#     if std not in back:
#         queue[0] = std
#         start = std
#     # if std == 0:
#     #     queue[1] = front[std]

# #fill every other student starting from first student
# key = start
# i = 2
# while key != -1 and n > 2:
    
#     queue[i] = front[key]
#     i += 2
#     if front[key] in front and front[front[key]] != 0:
#         key = front[key]
#     else:
#         key = -1
# #last student
# for std in back:
#     if std not in front:
#         queue[-1] = std
#         start = std
#     if std == 0:
#         queue[n-2] = back[std]

# # fill every other student starting from last student
# key = start
# i = n - 3

# while key != -1 and n > 2:

#     queue[i] = back[key]
#     i -= 2
#     if back[key] in back and back[back[key]] != 0:
#         key = back[key]
#     else:
#         key = -1


 

# for j in range(n):
#     print(queue[j], end=" ")


n = int(input())
front = {}
back = {}

for _ in range(n):
    a, b = list(map(int, input().split()))
    front[a] = b
    back[b] = a

queue = [0]*(n+2)
i = 2

start = 0
if n % 2 != 0:
    for key in front:
        if key not in back:
            start = key
            queue[1] = key
            i = 3
            break

key = start

while key != -1:
    
    queue[i] = front[key]
    i += 2
    if front[key] in front and front[key] != 0:
        key = front[key]
    else:
        key = -1

i = n - 1
key = 0

while key != -1:
    queue[i] = back[key]
    i -= 2
    if back[key] in back and back[key] != 0:
        key = back[key]
    else:
        key = -1

for j in range(1,n+1):
    print(queue[j], end=" ")
    
