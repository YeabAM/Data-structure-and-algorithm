class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins) + 1)]
        
        dp[0][0] = 1
        
        for r in range(1, len(dp)):
            for c in range(len(dp[0])):
                dp[r][c] = dp[r-1][c]
                
                prevSum = c - coins[r-1]
                
                if prevSum >= 0:
                    dp[r][c] += dp[r][prevSum]
                
                    
        return dp[len(coins)][amount]