class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binaries = []
        power, result = 0, 0
        for i in range(1,n+1):
            binaries.append(bin(i).replace("0b",""))
            
        binString = "".join(binaries)
        result = int(binString, 2)
                
        return result % (10 ** 9 + 7)
                
            
            
            
        
        