from heapq import heapify, heappop, heappush

def solve(size, social):
    socialbility = []
    ans = []
    for i, value in enumerate(social):
            if value > 0:
                heappush(socialbility, [-1 * value, i+1])

    while len(socialbility) >= 2:
        p1, idx = heappop(socialbility)
        p1 *= -1
        
        p2, idx2 = heappop(socialbility)

        p2 *= -1

        p1 -= 1
        p2 -= 1

        ans.append((idx, idx2))

        if p1 > 0:
            heappush(socialbility, [-1 * p1, idx])

        if p2 > 0:
            heappush(socialbility, [-1 * p2, idx2])


    print(len(ans))

    for i in range(len(ans)):
        print(*ans[i])

def main():
    cases = int(input())

    for _ in range(cases):
        size = int(input())
        social = list(map(int, input().split()))
        solve(size, social)
        


main()

        
            

        
        
                

