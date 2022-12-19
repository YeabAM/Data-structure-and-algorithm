class Solution:
    def checkValidString(self, s: str) -> bool:
        wildCount = 0
        pCount = 0
        cCount = 0
    
        left = 0
        right = 0
        
        for ch in s:
            # print(pCount, wildCount)
            if ch == '(':
                pCount += 1
                
            elif ch == '*':
                wildCount += 1
            
            else:
                cCount += 1
                
            if cCount > wildCount + pCount:
                return False
            
                    
                
        pCount = wildCount = cCount = 0
    
        
        for ch in reversed(s):
            
            if ch == ')':
                pCount += 1
            
            elif ch == '*':
                wildCount += 1
                
            else:
                cCount += 1
                
            if cCount > wildCount + pCount:
                return False
            
        return True
                