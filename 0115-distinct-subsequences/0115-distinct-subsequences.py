class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        
        def match(ss, tt):
            if (ss, tt) in memo:
                return memo[(ss, tt)]
            
            if tt >= len(t):
                return 1
            
            if ss >= len(s) or len(s) - ss < len(t) - tt:
                return 0
            
            isMatch = t[tt] == s[ss]
            result = 0
            
            if isMatch:
                result = match(ss + 1, tt + 1)
            
            result += match(ss + 1, tt)
            memo[(ss, tt)] = result
            return result
        
        return match(0, 0)