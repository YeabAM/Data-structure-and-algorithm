class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        rows = len(matrix)
        cols = len(matrix[0])
        
        
        in_bound = lambda r, c: 0 <= r < rows and 0 <= c < cols
    
        
        
        def find_path(r, c):
            maxx = 0
            
            if (r, c) in memo:
                return memo[(r, c)]
            
            for dx, dy in direction:
                nr, nc = r + dx, c + dy
                
                if in_bound(nr, nc) and matrix[nr][nc] > matrix[r][c]:
                
                    curr = find_path(nr, nc)
                    
                    maxx = max(curr, maxx)
            
            memo[(r, c)] = maxx + 1
                    
            return maxx + 1
        
        longest = 1
        memo = {}
        for r in range(rows):
            for c in range(cols):
            
                curr_length = find_path(r, c)
                longest = max(longest, curr_length )
                
                
        return longest
                
            
        