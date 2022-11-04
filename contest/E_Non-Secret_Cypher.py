from collections import defaultdict
def main():
    n, k = map(int, input().split())
    elements = list(map(int, input().split()))

    countOf = defaultdict(int)
    count = 1

    left , ans = 0, 0
    for right in range(n):
        countOf[elements[right]] += 1
        if countOf[elements[right]] > 1:
            count += 1
        
        while left <= right and count >= k:
            if countOf[elements[left]] > 1:
                count -= 1
                countOf[elements[left]] -= 1
            left += 1
        if left > 0:
            ans += (left)
    print(ans)
main()