class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        shiftCount = 0
    
        while num:
            lastDigit = num & 1
            
            if not lastDigit:
                ans |= 1 << shiftCount
                
            shiftCount += 1
            num >>= 1
            
        return ans
            
                
            
        