class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        maxx = 0
        memo = defaultdict(int)
        
        for r  in range(len(s)):
                memo[s[r]] +=1
                
                while memo[s[r]] > 1:
                    memo[s[l]] -= 1
                    l += 1
                    
                maxx = max(r - l + 1, maxx)
    
        return maxx
        