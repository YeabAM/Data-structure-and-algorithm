from functools import lru_cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        inbound = lambda r , c: 0 <= r < m and 0 <= c < n
        @lru_cache()
        
        def dfs(r, c):
            if not inbound(r, c):
                return float("inf")
            if r == m - 1 and c == n - 1:
                return grid[r][c]
            
            
            return min(dfs(r+1, c), dfs(r, c+1)) + grid[r][c]
        
        minPath = dfs(0,0)
        return minPath
    

            