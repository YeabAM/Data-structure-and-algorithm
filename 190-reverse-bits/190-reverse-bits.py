class Solution:
    def reverseBits(self, n: int) -> int:
        rev = bin(n)
        rev = rev[-1:1:-1]
        rev = rev + (32-len(rev)) * '0'
        rev = int(rev,2)
        
        return rev
        
            
         
        
        
        