class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        
        
        in_bound = lambda r,c : 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        
        def dfs(nr, nc):
            
            if not in_bound(nr, nc) or grid[nr][nc] == 0:
                return 0
            if (nr, nc) in visited:
                return 0
            
            visited.add((nr, nc))
            
            
           
            total = max(dfs(nr + 1, nc) , dfs(nr - 1, nc) , dfs(nr, nc+1), dfs(nr, nc-1))  + grid[nr][nc]
            
            visited.remove((nr,nc))
            
            return total
                
        self.gold = 0    
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    self.gold = max(self.gold, dfs(r,c))  


        return (self.gold)
            
        