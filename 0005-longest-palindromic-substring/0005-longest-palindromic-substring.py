class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        pos = None
        #for odd
        for i in range(len(s)):
            count = 1
            r = i + 1
            l = i - 1
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                r += 1
                l -= 1
                count += 2
                
            if count > longest:
                pos = (l, r)
                longest = count
            
        
        #for even
        for j in range(1, len(s)):
            count = 0
            l = j -1
            r = j
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                r += 1
                l -= 1
                count += 2
                
            if count > longest:
                pos = (l, r)
                longest = count
        
        return s[pos[0]+1:pos[1]]
            
            
        