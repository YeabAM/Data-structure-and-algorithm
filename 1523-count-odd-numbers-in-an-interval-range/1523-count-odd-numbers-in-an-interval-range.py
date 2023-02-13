class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if (high - low + 1) % 2 == 0:
            return (high - low + 1) // 2
        
        else:
            dif = high - low + 1
            if low % 2:
                return ceil(dif / 2)
            else:
                return dif // 2
        