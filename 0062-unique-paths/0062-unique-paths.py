class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        inbound = lambda r, c: 0 <= r < m and 0 <= c < n
        
        memo = {}
        def backtrack(r, c):
            if not inbound(r, c):
                return 0
            if (r, c) == (m-1, n-1):
                return 1
            if (r, c) in memo:
                return memo[(r, c)]
            
            memo[(r,c)] = backtrack(r, c+1) + backtrack(r+1, c)
            return memo[(r, c)]
        
        return backtrack(0, 0)