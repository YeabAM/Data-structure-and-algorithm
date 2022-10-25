class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        def maxScore(l, r, ops):
            if ops >= len(multipliers):
                return 0
#            
            if (l, r, ops) in memo:
                return memo[(l, r, ops)]
            
            left =   nums[r] * multipliers[ops] + maxScore(l, r-1, ops + 1)
            right =  nums[l] * multipliers[ops] +  maxScore(l+1, r, ops + 1)
            
            memo[(l, r,ops)] = max(left, right)
            return memo[(l,r,ops)]
        
        memo = {}
        return maxScore(0, len(nums) - 1, 0)
        