class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @lru_cache(None)
        
        def dp(idx, total):
            
            if idx >= len(coins):
                return 0
            
            if total == amount:
                return 1
            
            count = 0
            for i in range(idx, len(coins)):
                if total + coins[i] <= amount:
                    count += dp(i, total + coins[i])
                    
            return count
        
        return dp(0,0)
                
        