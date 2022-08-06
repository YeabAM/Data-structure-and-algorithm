class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        purchasePrice = prices[0]
        
        for i, currentPrice in enumerate(prices):
            if purchasePrice > currentPrice:
                purchasePrice = currentPrice
                
            maxProfit = max((currentPrice - purchasePrice), maxProfit)
            
        return maxProfit
                
            
                
        