from collections import defaultdict
n = int(input())
s = 9
 
while s < n:
    s = 10 * s + 9
s //= 10
sn = n - s
_max = float("-inf")
 
def sumOfDigits(num1):  
    total = 0
    while num1:
        total += num1 % 10
        num1 //= 10
    return total
 
_max = sumOfDigits(s) + sumOfDigits(sn)
    
print(_max)