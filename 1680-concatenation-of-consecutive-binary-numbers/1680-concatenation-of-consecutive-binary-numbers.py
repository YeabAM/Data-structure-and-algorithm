class Solution:
    def concatenatedBinary(self, n: int) -> int:
        shift = 0
        result = 0
        mod = 1000000007
        for i in range(1,n+1):
            if i & (i-1) == 0:
                shift += 1
            
            result = ((result << shift) | i) % mod
        
                
        return result
                
            
            
            
        
        