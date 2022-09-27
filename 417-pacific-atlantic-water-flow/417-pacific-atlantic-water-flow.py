class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        in_bound = lambda r, c: 0<= r < rows and 0<= c < cols
        DIRS = [(1,0),(-1,0),(0,1),(0,-1)]
        pac, atl = set(), set()
        def dfs(r, c, visit, prevH):
            
            if not in_bound(r, c) or (r, c) in visit or\
            heights[r][c] < prevH:
                return
            
            visit.add((r, c))
            
            for dx, dy in DIRS:
                nr = r + dx
                nc = c + dy
                dfs(nr, nc, visit, heights[r][c])
                
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])
            
        
        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r, cols-1,atl, heights[r][cols - 1])
            
        return pac.intersection(atl)
            
            