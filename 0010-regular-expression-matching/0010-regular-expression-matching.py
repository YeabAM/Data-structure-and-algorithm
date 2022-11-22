class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @lru_cache(None)
        def dp(sp, pp):
            if sp >= len(s) and pp >= len(p):
                return True
            if pp >= len(p):
                return False
            
            match =(sp < len(s)) and (s[sp] == p[pp] or p[pp] == '.')
            
            if (pp + 1) < len(p) and (p[pp + 1] == '*'):
                return dp(sp, pp + 2) or (match and dp(sp+1, pp))
            
            if match:
                return dp(sp+1, pp+1)
            
            return False
        
        return dp(0,0)
                
            
        