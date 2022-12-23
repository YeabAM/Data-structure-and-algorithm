class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        rows = len(grid)
        cols = len(grid[0])
        
        in_bound = lambda r, c: 0 <= r < rows and 0 <= c < cols
        
        max_gold = 0
        
        
        
        def find_path(r, c, visited):
            curr_gold = 0
            
            visited.add((r, c))
            
        
            
            
            for dx, dy in direction:
                nr, nc = r + dx, c + dy
    
                if in_bound(nr, nc) and (nr, nc) not in visited and grid[nr][nc] != 0:
                    
                    curr_gold = max(curr_gold, find_path(nr,nc,visited) + grid[nr][nc])
                    
            visited.remove((r, c))
            
            return curr_gold
    
            
        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    max_gold = max(max_gold, find_path(r, c, set()) + grid[r][c])
                
        
        return max_gold