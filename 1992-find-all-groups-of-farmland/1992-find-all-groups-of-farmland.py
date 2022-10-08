class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        visited = set()
        farms = []
        rows = len(land)
        cols = len(land[0])
        in_bound = lambda r, c: 0 <= r < rows and 0 <= c < cols
        def bfs(r, c):
            # print("d")
            q = deque()
            end = (r, c)
            currFarms = []
            currFarms += [r, c]
            q.append((r, c))
            visited.add((r, c))
            directions = [(1,0),(-1,0),(0,-1),(0,1)]
            
            while q:
                currRow, currCol = q.popleft()
                end = max(end, (currRow, currCol))
                for dx, dy in directions:
                    nr, nc = dx + currRow, dy + currCol
                    
                    if in_bound(nr, nc) and  \
                    (nr, nc) not in visited and \
                    land[nr][nc] == 1 :
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        
            # print("farm", visited)
                    
                        
            currFarms += [end[0], end[1]]
            farms.append(currFarms)
            
        for r in range(rows):
            for c in range(cols):
                if land[r][c] == 1 and (r, c) not in visited:
                    # print(r, c)
                    bfs(r, c)
                    
        return farms
        