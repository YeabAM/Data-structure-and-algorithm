class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, len(dp)):
            for j in range(len(coins)):
                if i - coins[j] >= 0:
                    # print('here')
                    dp[i] = min(dp[i], dp[i-coins[j]] + 1)
        # print(dp)        
        return dp[-1] if dp[-1] != inf else -1
                
            
        
        
        
                    
            
                
                
            
                