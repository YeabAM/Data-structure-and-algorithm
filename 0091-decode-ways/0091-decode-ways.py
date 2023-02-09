class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def dfs(idx):
            if idx >= len(s):
                return 1
            
            if s[idx] == '0':
                return 0
            
            res = 0
            res += dfs(idx+1)
            
            if idx + 1 < len(s):
                if s[idx] == '1' or (s[idx] == '2' and s[idx+1] in '0123456'):
                    res += dfs(idx+2)
                    
            return res
        
        return dfs(0)
                
        