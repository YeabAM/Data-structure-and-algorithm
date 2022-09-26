class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        
        for i in range(len(nums)-1, -1, -1):
            maxx = 0
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    maxx = max(maxx, dp[j])
            dp[i] = maxx + 1
            
        return max(dp)
        