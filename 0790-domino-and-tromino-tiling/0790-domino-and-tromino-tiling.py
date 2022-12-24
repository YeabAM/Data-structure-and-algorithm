class Solution:
    def numTilings(self, n: int) -> int:
        dp = [[0, 0, 0 ,0] for i in range(n+1)]
        dp[0][0] = 1
        m = 10**9 + 7
        for i in range(1, n+1):
            dp[i][3] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
            dp[i][2] = dp[i-1][1] + dp[i-1][0]
            dp[i][1] = dp[i-1][2] + dp[i-1][0]
            dp[i][0] = dp[i-1][0] + dp[i-1][3]
            for j in range(4):
                dp[i][j] %= m
        return dp[-1][0]