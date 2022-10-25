class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        endingWith = [0 for _ in range(26)]
        
        endingWith[ord(s[0]) - 97] = 1
        
        for i in range(1, len(s)):
            curPos = ord(s[i]) - 97
            fromLeft = curPos - k
            fromRight = curPos + k
            
            if fromLeft <= 0:
                fromLeft = 0
                
            if fromRight >= 25:
                fromRight = 25
                
            #fromLeft 
            total = 0
            
            for j in range(fromLeft, fromRight + 1):
                total = max(total, endingWith[j])
                  
            endingWith[curPos] = total + 1
            # print(s[i], endingWith[curPos])
        
        return max(endingWith)
                
            
                
        
        