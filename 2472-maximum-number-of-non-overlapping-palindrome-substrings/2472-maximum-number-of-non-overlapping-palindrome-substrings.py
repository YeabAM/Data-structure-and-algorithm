class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        
        if k == 1:
            return len(s)
        
        count = 0
        
        @lru_cache(None)
        def topDown(border, index):
            if index >= len(s):
                return 0
            
            result = 0
            
            #odd
            length = 1
            r = index + 1
            l = index - 1

            while l > border and r < len(s) and s[l] == s[r] and length < k:
                r += 1
                l -= 1
                length += 2

            if length >= k:
                result = max(1 + topDown(r-1, r), result)
                
            #even
            length = 0
            r = index
            l = index - 1

            while l > border and r < len(s) and s[l] == s[r] and length < k:
                r += 1
                l -= 1
                length += 2

            if length >= k:
                result = max(1 + topDown(r-1, r), result)
                
            result = max(result, topDown(border, index + 1))
            
            return result
        
        return topDown(-1, 1)