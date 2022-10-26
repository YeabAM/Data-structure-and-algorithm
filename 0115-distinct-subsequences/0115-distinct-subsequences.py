class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        
        @lru_cache(None)
        def dp(i, j):
            if j == len(t):
                return 1
            
            if i == len(s):
                return 0
            
            if s[i] == t[j]:
                option1 = dp(i+1, j+1)
                option2 = dp(i+1, j)
                
                return option1 + option2
            
            return dp(i+1, j)
        
        return dp(0, 0)
        