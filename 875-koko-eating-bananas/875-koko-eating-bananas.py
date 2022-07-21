class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = ceil(sum(piles) / h)
        right = max(piles)
        
        while left < right:
            mid = (left + right) // 2 
            total = 0
            for p in piles:
                total += ceil(p/mid)
                
            
            if h >= total:
                right = mid
                
            else:
                left = mid + 1
                
        return right

       
        