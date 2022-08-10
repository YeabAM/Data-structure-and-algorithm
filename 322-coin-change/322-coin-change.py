class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse= True)
        memo = {}
        
        def dp(total):
            if total in memo:
                return memo[total]
            if total < 0:
                return float('inf')
        
            if total == 0:
                return 0  
            
            minim = float('inf')            
            for i in range(len(coins)):
                minim = min(minim, dp(total - coins[i]) + 1)
            memo[total] = minim
            
            return memo[total]
                
        minimum = dp(amount)        
        return minimum if minimum != float('inf') else -1  