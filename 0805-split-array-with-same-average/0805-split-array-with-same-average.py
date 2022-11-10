class Solution:
    def splitArraySameAverage(self, A):
        
            @lru_cache(None)
            def find(target, k, i):
                if k == 0: 
                    return target == 0

                if target < 0 or k + i > n: 
                    return False

                return find(target - A[i], k - 1, i + 1) or find(target, k, i + 1)

            n, s = len(A), sum(A)

            return any(find(s * k // n, k, 0) for k in range(1, n // 2 + 1) if s * k % n == 0)