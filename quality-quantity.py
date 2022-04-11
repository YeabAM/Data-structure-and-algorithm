tests = int(input())

for i in range(tests):
    size = input()
    inputs = list(map(int, input().split()))
    inputs.sort()
    Blue = inputs[0] + inputs[1]
    Red = inputs[-1]
    ans = "NO"
    bp = 1
    rp = len(inputs) - 1
    
    while bp < rp:
        if Red > Blue:
            ans = "YES"
            break
        
        bp += 1
        rp -= 1
        Blue += inputs[bp]
        Red  += inputs[rp]
        
        # print(Blue, Red)
    
    print(ans)
        
    
        
        
    
