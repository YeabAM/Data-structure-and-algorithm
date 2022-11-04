

def countTwo(num):
    count = 0

    while num % 2 == 0:
        count += 1
        num = num // 2

    return count

def solve(size, nums):

    amountOfTwos = []
    currTot = 0
    for i in range(size):
        currTot += countTwo(nums[i])
        # if i % 2 != 0:
        amountOfTwos.append(countTwo(i + 1))
    

    if currTot >= size:
        print(0)
        return

    amountOfTwos.sort(reverse=True)
    # print(amountOfTwos,currTot,"o")
    idx = 0
    ops = 0
    while idx < len(amountOfTwos) and currTot < size:
        
        currTot += amountOfTwos[idx]
        idx += 1
        ops += 1
        # print("d", ops)

    if currTot >= size:
        print(ops)
        return

    print(-1)
    return




def main():
    cases = int(input())
    for _ in range(cases):
        size = int(input())
        nums = list(map(int, input().split()))

        solve(size, nums)

main()
