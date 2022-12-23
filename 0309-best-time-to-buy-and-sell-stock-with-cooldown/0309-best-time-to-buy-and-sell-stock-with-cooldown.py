class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i, buy):
            if i >= len(prices):
                return 0
            
            if buy:
                #buy current stock
                option_1 = dp(i+1, 0) - prices[i]
                
                option_2 = dp(i+1, 1)
                
                return max(option_1, option_2)
            
            else:
                option_1 = dp(i+2, 1) + prices[i]
                option_2 = dp(i+1, 0)
                
                return max(option_1, option_2)
            
            
        option_1 = dp(1, 0) - prices[0]
        option_2 = dp(1, 1)
        
        return max(option_1, option_2)
        
        
        