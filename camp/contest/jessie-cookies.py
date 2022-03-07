def cookies(k, A):
    # Write your code here
    heapq.heapify(A)
    count = 0
    while A[0] < k: 
        s1 = heapq.heappop(A)
        if len(A) > 0:
            s2 = heapq.heappop(A)
            new = s1 + (s2 * 2)
            heapq.heappush(A, new)
            count += 1
        if not A:
            return -1
    return count