# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
size=int(input())
items=OrderedDict()
for i in range(size):
    item=input().split()
    itemName=" ".join(item[:-1])
    itemPrice=item[-1]
    if itemName in items:
        items[itemName] += int(itemPrice)
    else:
        items[itemName]=int(itemPrice)
    
for i in items:
    print(i,items[i])
