class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def dp(path):
            
            if path in memo:
                return memo[path]
        
            if path == s:
                return True
            
            if path != s[:len(path)]:
                memo[path] = False
                return False
            
            for word in wordDict:
                if dp(path + word):
                    return True
                
            memo[path] = False    
            return False
            
        memo = {}   
        return dp("")
            
        