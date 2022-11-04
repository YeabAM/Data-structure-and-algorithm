def solve(size, arr):
    arr.sort()
    for i in range(size - 1):
        if arr[i + 1] - arr[i] > 1:
            print('NO')
            return

    print('YES')
    return

def main():
    cases = int(input())
    # print(cases)
    for _ in range(cases):
        size = int(input())
        arr = list(map(int, input().split()))
        # print(size, arr)
        solve(size, arr)

main()