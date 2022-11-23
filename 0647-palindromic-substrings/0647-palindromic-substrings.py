class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        
        #check odd
        for i in range(len(s)):
            count += 1
            l = i - 1
            r = i + 1
            
            while (l >=0 and r < len(s)) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        
        #check even
        for j in range(1, len(s)):
            
            l = j - 1
            r = j
            
            while l >=0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
                
        return count
                
        