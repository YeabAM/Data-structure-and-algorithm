class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        minSpeed = ceil(sum(piles) / h)
        maxSpeed = max(piles)
        
        while minSpeed < maxSpeed:
            midSpeed = minSpeed + (maxSpeed - minSpeed) // 2
            total = 0
            for p in piles:
                total += ceil(p/midSpeed)
                
            if h >= total:
                maxSpeed = midSpeed
                
            else:
                minSpeed = midSpeed + 1
                
                
        return maxSpeed 
        