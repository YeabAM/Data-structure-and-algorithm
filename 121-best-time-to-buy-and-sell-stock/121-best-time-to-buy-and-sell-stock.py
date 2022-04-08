class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        purchase = 0
        
        for i in range(1, len(prices)):
            if prices[purchase] > prices[i]:
                purchase = i
            maxProfit = max((prices[i] - prices[purchase]), maxProfit )
            
        return maxProfit
                
        