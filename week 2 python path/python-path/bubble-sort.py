#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    swap=0
    count=0
    n=len(a)
    if (2<=n and n<600):
        
        for i in range (0,n):
           
            for j in range (0,n-1):
                if (a[j] > a[j + 1]):
                    swap=swap+1
                    a[j],a[j+1]=a[j+1],a[j]
            if(swap>=0):
                count=count+1
            elif(swap==0):
               break     
                    
    print("Array is sorted in",swap,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[n-1])
                    
                
            
        
        
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
