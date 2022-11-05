from math import floor, sqrt

def solve(l, r, a):
    if l // a == r // a:
        print((r // a) + (r % a))
        return

    else:
        v1 = (r // a) + (r % a)
        v2 = (r // a) - 1 + (a - 1)

        print(max(v1, v2))
        return
        

def main():
    cases = int(input())
    for _ in range(cases):
        l, r, a = map(int, input().split())
        solve(l, r, a)

main()
