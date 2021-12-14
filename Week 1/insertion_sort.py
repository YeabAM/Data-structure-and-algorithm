#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
#   str1 = ''.join(arr)
            
# print(str1)
def insertionSort1(n, arr):
    # Write your code here
    
    if(n>=1 and n<=1000):
        x=arr[n-1]
        
        for i in range(n-2,-1,-1):
            if x<arr[i]:
                arr[i+1]=arr[i]
                idx=i
            elif x>=arr[i]:
               arr[i+1]=x
               break
            for j in arr:
                print (j,end=" " )
            print ()
        if idx==0:
            arr[idx]=x   
            # print(arr)
            
            
        for j in arr:
            print (j,end=" " )
           
               
             
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
