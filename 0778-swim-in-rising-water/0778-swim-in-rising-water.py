class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        minHeight = []
        
        heapq.heappush(minHeight, (grid[0][0],0,0))
    
        
        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        inBound = lambda r, c: 0 <= r < rows and 0 <= c < cols
        visited = set()
        visited.add((0,0))
        
        while minHeight:
            currH, cx, cy = heapq.heappop(minHeight)
            
            if cx == len(grid) -1 and cy == len(grid[0]) - 1:
                
                return currH
            
            for x, y in direction:
                nr = cx + x
                nc = cy + y
                
                if inBound(nr, nc) and (nr,nc) not in visited:
                    cost = max(currH, grid[nr][nc])
                    heapq.heappush(minHeight, (cost, nr, nc))
                    visited.add((nr, nc))
                    
        
            
            
            
            
            