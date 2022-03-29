class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 !=0:
            return False
        parenthesis = [0] * len(s)
        
        for i in range(len(s)):
            if locked[i] == "1":
                if s[i] == "(":
                    parenthesis[i] = 1
                else:
                    parenthesis[i] = -1
                
        bal = 0
        left = 0
        for i, val in enumerate(parenthesis):
            bal += val
            
            while left <= i and bal < 0:
                if parenthesis[left] == 0:
                    parenthesis[left] = 1
                    bal += 1
                
                left += 1
            
            if bal < 0:
                return False
           
        bal = 0
        right = len(parenthesis) - 1
        for  i in range(len(parenthesis) - 1, -1, -1):
            bal += parenthesis[i]       
            while right >= i and bal > 0:
                if parenthesis[right] == 0:
                    parenthesis[right] = -1
                    bal -= 1
                
                right -= 1
            
            if bal > 0:
                return False
            
        return True
        