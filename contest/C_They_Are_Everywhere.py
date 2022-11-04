from collections import defaultdict

n = int(input())
st = input()
l = 0
seen = set()
shouldSee = len(set(st))
count = defaultdict(int)
maxx = n
l = 0
for r in range(n):
    seen.add(st[r])
    count[st[r]] += 1
    # print(seen, count, shouldSee, maxx)
    while len(seen) == shouldSee:
        
        maxx = min(maxx, r - l + 1)
        count[st[l]] -= 1
        if count[st[l]] == 0: 
            seen.remove(st[l])
        l += 1
        
print(maxx)