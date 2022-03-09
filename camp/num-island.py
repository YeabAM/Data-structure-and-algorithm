class Solution:
    def __init__(self):
        self.island = 0
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            visited.add((row, col))
            for direction in DIR:
                newRow, newCol = row + direction[0], col + direction[1]
                if (newRow, newCol) not in visited and \
                in_bound(newRow, newCol) \
                and grid[newRow][newCol] != "0":
                    dfs(newRow, newCol)
                
                else:
                    continue
            
            
                
        
        in_bound = lambda row, col : 0 <= row < len(grid) and 0 <= col < len(grid[0])
        visited = set((0, 0))
        DIR = [[1,0], [0,1],[-1,0],[0,-1]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] != "0":
                    dfs(i,j)
                    self.island += 1
    
        
        return self.island
        