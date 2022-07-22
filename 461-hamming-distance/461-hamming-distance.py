class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x, y = bin(x)[2:], bin(y)[2:]
        count = 0
        if len(x) > len(y):
            y = "0" * (abs(len(x) - len(y))) + y
            
        elif len(y) > len(x):
            x = "0" * (abs(len(x) - len(y))) + x
            
        for i in range(len(x)):
            if x[i] != y[i]:
                count += 1
                
        return count
            
        