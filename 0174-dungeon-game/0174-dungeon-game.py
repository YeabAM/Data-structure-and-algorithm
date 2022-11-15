class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])
        
        @lru_cache(None)
        def dp(r, c):
            if r >= rows  or c >= cols: 
                return -inf
            
            if r == rows - 1 and c == cols - 1:
                return min(0, dungeon[r][c])
            
            
            return min(0, dungeon[r][c] + max(dp(r+1,c), dp(r,c+1)))
        
        return abs(dp(0,0)) + 1
            
        