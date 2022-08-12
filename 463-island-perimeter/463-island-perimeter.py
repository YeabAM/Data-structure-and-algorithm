class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
            direction = [(1,0), (-1,0), (0,1), (0,-1)]
            in_bound = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[0])
            visited = set()
            perim = 0
            
            def getPerim(x, y):
                nonlocal perim
                visited.add((x, y))
                
                for d in direction:
                    nr, nc = x + d[0], y + d[1]
                    
                    if  (not in_bound(nr, nc) or grid[nr][nc] == 0):
                        if grid[x][y] == 1:
                            perim += 1

                        continue
                    
                    if (nr, nc) in visited:
                        continue
                                  
                    getPerim(nr, nc)
                    
                    
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        getPerim(i, j)
                        return perim
                        
                        
                
                
        