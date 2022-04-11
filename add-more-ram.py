tests = int(input())

for i in range(tests):
    s, r = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    rams = zip(a, b)
    rams = list(rams)
    rams.sort()
    for ram in rams:
        if r >= ram[0]:
            r += ram[1]
        else:
            break
    print(r)
    
