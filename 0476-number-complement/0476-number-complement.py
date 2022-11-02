class Solution:
    def findComplement(self, num: int) -> int:
        bitValue = bin(num)
    
        power = len(bitValue) - 2
        
        temp = (2 ** power) - 1
        
        return (temp ^ num)
            
                
            
        