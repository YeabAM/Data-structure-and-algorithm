import sys
from typing import List
sys.setrecursionlimit(10**8)
from collections import deque
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        direction = [ [ 0, -1 ], [ -1, 0 ], [ 0, 1 ], [ 1, 0 ] ]
        in_bound = lambda r, c: 0<= r < rows and 0 <= c < cols
        def bfs(bx, by, i, j, pos):
            queue = deque()
            queue.append((bx, by, i, j))
            visited.add((i, j))
            
            while queue:
                bx, by, x, y = queue.popleft()
                pos.append((bx - x, by - y))
                # print(pos, bx, by, x, y)
                for dx, dy in direction:
                    nr, nc = x + dx, dy + y
                    # print(bx, by, nr, nc,'p')
                    if in_bound(nr, nc) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        # print(bx, by, nr, nc,'p')
                        queue.append((bx, by, nr, nc))
                        visited.add((nr, nc))
            return pos
                    
        islands = set()            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    points = []
                    points = bfs(r, c, r, c, points)
                    islands.add(tuple(points))
                    
        return len(islands)
                    
