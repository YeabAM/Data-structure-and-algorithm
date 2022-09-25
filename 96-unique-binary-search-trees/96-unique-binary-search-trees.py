class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        
        for i in range(1, n+1):
            res = 0
            for j in range(1 , i + 1):
                left = dp[j-1]
                right = dp[i - j]
                res += left * right
            dp[i] = res
                
        return dp[-1]
                
        
        