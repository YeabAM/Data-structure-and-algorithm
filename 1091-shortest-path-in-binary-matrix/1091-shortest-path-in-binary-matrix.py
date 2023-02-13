class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[len(grid) - 1][len(grid[0]) - 1] == 1:
            return -1
        
        queue = deque()
        queue.append((0, 0, 1))
        visited = set()
        visited.add((0, 0))
        direction = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1, -1)]
        rows = len(grid)
        cols = len(grid[0])
        in_bound = lambda r, c: 0 <= r < rows and 0 <= c < cols
        
        while queue:
            r, c, dis = queue.popleft()
            
            if r == rows -1 and c == cols -1:
                return dis
            
            for dx, dy in direction:
                nr, nc = r + dx, c + dy
                if in_bound(nr, nc) and (nr, nc) not in visited and grid[nr][nc] == 0:
                    queue.append((nr, nc, dis+1))
                    visited.add((nr, nc))
        return -1