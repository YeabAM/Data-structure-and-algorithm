class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        col = []
        
        while columnNumber > 0:
            columnNumber -= 1
            curr = columnNumber % 26
            col.append(chr(65 + curr))
            columnNumber //= 26
            
        return "".join(col[::-1])
        