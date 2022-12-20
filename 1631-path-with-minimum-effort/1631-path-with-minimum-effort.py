class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        
        next_cell = []
        
        heapq.heappush(next_cell, (0,0,0))
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        in_bound = lambda r, c: 0 <= r < rows and 0 <= c < cols
    
        visited = set()
        
        
        while next_cell:
            curr_effort, row, col = heapq.heappop(next_cell)
            
            if row == rows - 1 and col == cols - 1:
                return curr_effort
            
            for dx, dy in directions:
                nr, nc = row + dx, col + dy
                
                if in_bound(nr, nc) and (row, col, nr, nc) not in visited and (nr, nc, row, col) not in visited:
                    abs_dif = abs(heights[nr][nc] - heights[row][col])
                    
                    effort = max(curr_effort, abs_dif)
                    
                    heapq.heappush(next_cell, (effort, nr, nc))
                    
                    visited.add((row, col, nr, nc))
                    visited.add((nr, nc, row, col))
                    
        
                    
                    
        
        
        
        
        
        
        