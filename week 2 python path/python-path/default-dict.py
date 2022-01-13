# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
A = list()
B = list()
sizes=input().split()
sizeA=int(sizes[0])
sizeB=int(sizes[1])
indices=defaultdict(list)
index=0
for i in range(sizeA):
    element=input()
    A.append(element)
for i in range(sizeB):
    element=input()
    B.append(element)
for i in A:
    indices[i].append( A.index(i, index) + 1)
    index+=1
for i in B:
    if i not in A:
        print (-1)
    else:
        indice = " ".join(map(str, indices[i])) 
        print (indice)   
