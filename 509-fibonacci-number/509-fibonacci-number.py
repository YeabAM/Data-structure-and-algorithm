class Solution:
    def fib(self, n: int) -> int:
        memo = dict()
        memo[0] = 0
        memo[1] = 1
        def dp(n):
            if n in memo:
                return memo[n]

            memo[n] = dp(n-1) + dp(n-2)
            return memo[n]
        
        return dp(n)
        