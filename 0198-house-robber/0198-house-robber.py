class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0 for _ in range(len(nums) + 2)]
        
        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 1], dp[i-2] + nums[i-2])
            
        return max(dp[-1], dp[-2])