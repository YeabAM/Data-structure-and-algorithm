class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        maxLength = 0
        odd = False
        
        if len(s) == 1:
            return 1
        
        for l in counts:
            # print (counts[l] % 2 )
            if counts[l] % 2:
                odd = True
                if counts[l] > 1:
                    maxLength += counts[l] - 1
                    # print(l, counts[l], maxLength)
            else:
                maxLength += counts[l]
                # print(l, counts[l], maxLength)
                
        return maxLength if not odd else maxLength + 1
        
        
            
        