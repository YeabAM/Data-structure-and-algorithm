class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        numStr = sorted(str(n))
        
        
        for i in range(30):
            num = str((2 ** i))
            if sorted(num) == numStr:
                return True
            
        return False
            
        