class Solution:
    
    @lru_cache(None)
    def isPalindrome(self,s,l, r):
        if l > r:
            return True
        
        
        if s[l] == s[r]:
            return self.isPalindrome(s,l+1, r-1)
            
        return False
                
    
    def minCut(self, s: str) -> int:
        if s == s[::-1]:
            return 0
        
        
        def dfs(idx):
            if idx in memo:
                return memo[idx]
            
            
            if idx == len(s):
                return -1
            
            
            minCut = float('inf')
            
            for i in range(idx, len(s)):
                if self.isPalindrome(s,idx, i):
                    minCut = min(minCut, 1 + dfs(i+1))
                    
                    
            memo[idx] = minCut
            return memo[idx]
                    
                    
        memo= {}
        minCut = dfs(0)
        
        return minCut
        
        
        
    
        