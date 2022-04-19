from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache(None)
        def getBuy(i, buy):
            if i >= len(prices):
                return 0
            
            if buy == -1:
                return max(getBuy(i,prices[i]) , getBuy(i+1, buy))
            else:
                return max((prices[i] -  buy) + getBuy(i+2, -1) , getBuy(i+1, buy))
                
        
        
        return max(getBuy(0, prices[0]) , getBuy(0, -1))