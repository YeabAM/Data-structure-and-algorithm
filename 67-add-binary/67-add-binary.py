class Solution:
    def addBinary(self, a: str, b: str) -> str:
        total = bin(int(a,2) + int(b,2))
        return total[2:]
    