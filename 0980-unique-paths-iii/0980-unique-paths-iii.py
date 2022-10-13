class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        visited = set()
        n, m = len(grid), len(grid[0])
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        inbound = lambda r, c: 0 <= r < n and 0 <= c < m
        ans = 0
        
        def dfs(row ,col):
            nonlocal ans
            visited.add((row, col))
            if grid[row][col] == 2:
                if len(visited) == n * m:
                    ans += 1
                return
            for dx, dy in DIR:
                nx, ny = row + dx, col + dy
                
                if not inbound(nx, ny) or (nx, ny) in visited:
                    continue
                
                if grid[nx][ny] == -1:
                    visited.add((nx, ny))
                    continue
                dfs(nx, ny)
                visited.remove((nx, ny))
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return ans