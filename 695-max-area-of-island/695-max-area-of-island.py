class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxArea = 0
        self.count = 0
        DIR = [[1,0], [0,1],[-1,0],[0,-1]]
        in_bound = lambda row, col : 0 <= row < len(grid) and 0 <= col < len(grid[0])
        visited = set((0, 0))
        
        def dfs(row, col):
            self.count += 1
            visited.add((row, col))
            for direction in DIR:
                newRow, newCol = row + direction[0], col + direction[1]
                if (newRow, newCol) not in visited and \
                in_bound(newRow, newCol) \
                and grid[newRow][newCol] != 0:
                    dfs(newRow, newCol)
                
                else:
                    continue
            
            
                   
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] != 0:
                    self.count = 0
                    dfs(i,j)
                    self.maxArea = max(self.maxArea, self.count)
    
        
        return self.maxArea