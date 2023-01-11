class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @lru_cache(None)
        def countSteps(idx, total):
            if total == amount:
                return 1
            
            if idx >= len(coins):
                return 0
            
            count = 0
            
            for i in range(idx, len(coins)):
                if total + coins[i] <= amount:
                    count += countSteps(i, total + coins[i])
            
            return count
        
        return countSteps(0, 0)
                