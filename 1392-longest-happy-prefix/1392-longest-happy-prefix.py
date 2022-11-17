class Solution:
    def longestPrefix(self, s: str) -> str:
        size = len(s)
        lps = [0 for _ in range(size)]
        j = 0
        longestPrefix = 0
        ans = None
        
        for i in range(1, size):
            while j and s[j] != s[i]:
                j = lps[j - 1]
                
            if s[j] == s[i]:
                lps[i] = j + 1
                j += 1
        
        longestPrefix = lps[-1]
        ans = s[:longestPrefix]
        
        return ans
                
        