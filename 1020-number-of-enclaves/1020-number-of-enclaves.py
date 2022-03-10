class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        DIR = [[1,0], [0,1],[-1,0],[0,-1]]
        in_bound = lambda row, col : 0 <= row < len(grid) and 0 <= col < len(grid[0])
        visited = set((0, 0))
        r = len(grid)
        c = len(grid[0])
        
        def dfs(row, col):
            visited.add((row, col))
            for direction in DIR:
                newRow, newCol = row + direction[0], col + direction[1]
                if (newRow, newCol) not in visited and \
                in_bound(newRow, newCol) \
                and grid[newRow][newCol] != 0:
                    dfs(newRow, newCol)
        
        for i in range(r):
            for j in range(c):
                if i == 0 or j == 0 or i == r -1 or j == c - 1:
                    if (i, j) not in visited and grid[i][j] == 1:
                        dfs(i, j)
        count = 0                 
        for i in range(r):
            for j in range(c):
                if (i, j) not in visited and grid[i][j] == 1:
                    count += 1
        return count
                        
        
            
                        
        