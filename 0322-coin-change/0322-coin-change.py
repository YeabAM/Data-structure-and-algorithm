class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @lru_cache(None)
        def countSteps(amount):
            
            # base case
            if amount == 0:
                return 0
            # if less than 0, which means the subproblem fails
            if amount < 0:
                return -1
            
            res = float('inf')
            for i in range(len(coins)):
                # recursion, minus each recursion
                subproblem = countSteps(amount - coins[i])
                if subproblem == -1:
                    continue
                    
                res = min(res, subproblem+1)
                
            if res == float('inf'):
                return -1
            else:
                return res
            
        return countSteps(amount)
    
        