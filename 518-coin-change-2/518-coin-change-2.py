class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        coins.sort(reverse = True)
        def dp(idx, total):
            
            if (idx, total) in memo:
                return memo[(idx, total)]
            
            if total < 0:
                return 0
            
            if total == 0:
                # print("kd")
                return 1
            
            answer = 0
            for i in range(idx, len(coins)):
                answer += dp(i, total - coins[i])
            
            memo[(idx, total)] = answer
            return memo[(idx, total)]
        
        return dp(0, amount)
        
        