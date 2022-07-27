class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxm = 1
        p1 = 0
        p2 = 1
        
        if len(s) == 0:
            return 0
        
        
        
        while p2 < len(s):
            
            if p2 - p1 + 1 != len(set(s[p1:p2 + 1])):
                p1 += 1
                
            else:
                maxm = max(maxm, p2 - p1 + 1)
            
            p2 += 1
                
        return maxm
        
            
            
            
            
            
        
        
            
        