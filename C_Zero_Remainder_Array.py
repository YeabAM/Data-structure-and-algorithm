from collections import defaultdict
from math import ceil


def solve(size, arr, d):
    incVal = defaultdict(int)
    countD = 0

    for i in range(size):
        incVal[arr[i]] = ceil(arr[i] // d)
    while countD == size:
        




def main():
    cases = int(input())

    for _ in range(cases):
        size, d = map(int,input().split())
        arr = list(map(int,input().split()))
        solve(size, arr, d)