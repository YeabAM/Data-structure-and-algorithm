class Solution:
    def maxProfit(self, price: List[int]) -> int:
        @lru_cache(None)
        
        def dp(i, buy):
            if i == len(price):
                return 0
            
            if buy:
                # buy stock with current price
                option_1 = dp(i+1, 0) - price[i]
                # move on without buying
                option_2 = dp(i+1, 1)
                
                return max(option_1, option_2)
            
            else:
                # sell stock with current price
                option_1 = dp(i+1, 1) + price[i]
                # sell on without buying
                option_2 = dp(i+1, 0)
                
                return max(option_1, option_2)

                
        option_1 = dp(1, 0) - price[0]
        option_2 = dp(1, 1)

        return max(option_1, option_2)
        