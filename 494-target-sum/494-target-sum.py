class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0
        
        @lru_cache(None)
        def backtrack(summ, idx):
            nonlocal count
            
            if idx == len(nums):
                if summ == target:
                    return 1
                return 0
            return (backtrack(summ + nums[idx], idx + 1) + backtrack(summ - nums[idx], idx + 1))
            
        
        
        return backtrack(0,0)
        