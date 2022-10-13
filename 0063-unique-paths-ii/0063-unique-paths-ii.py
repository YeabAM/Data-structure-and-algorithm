class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        inbound = lambda r, c: 0 <= r < m  and 0 <= c < n
        
        memo = {}
        def backtrack(r, c):
            if not inbound(r, c) or obstacleGrid[r][c] == 1:
                return 0
            if (r, c) == (m-1, n-1):
                return 1
            if (r, c) in memo:
                return memo[(r, c)]
            
            memo[(r,c)] = backtrack(r, c+1) + backtrack(r+1, c)
            return memo[(r, c)]
        
        return backtrack(0, 0)
        