class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1 = 0
        n2 = 0
        power = 0
        
        for v in a[::-1]:
            n1 += int(v) * 2**power
            power += 1
        
        power = 0
        for v in b[::-1]:
            n2 += int(v) * 2**power
            power += 1
        
        return bin(n1+n2)[2:]
        
            
        