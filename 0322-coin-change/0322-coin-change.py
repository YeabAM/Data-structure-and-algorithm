class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # minCount = float('inf')
        coins.sort(reverse = True)
        @lru_cache(None)
        
        def backtrack(total):
            
            if total == amount:
                return 0
            
            min_count = float('inf')
            
            for i in range(len(coins)):
                if total + coins[i] <= amount:
                    curr_count = 1 + backtrack(total + coins[i])
                    min_count = min(min_count, curr_count)
        
            return min_count
                    
        count = backtrack(0)
        
        return count if count != float('inf') else -1
        
        
                    
            
                
                
            
                