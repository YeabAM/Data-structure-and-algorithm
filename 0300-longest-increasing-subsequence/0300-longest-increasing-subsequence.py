class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dp(index):
            if index == len(nums) - 1:
                return 1
            if index in memo:
                return memo[index]
            run_max = 0
            for i in range(index + 1, len(nums)):
                
                if nums[index] < nums[i]:
                    run_max = max(run_max, dp(i))
            
            memo[index] = 1 + run_max
            return memo[index]
        longest = 0   
        memo = {}
        for i in range(len(nums)):
            longest = max(longest, dp(i))
            
        return longest