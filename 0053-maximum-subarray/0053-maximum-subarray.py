class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max = 0
        global_max = float('-inf')
        size = len(nums)
        
        for i in range(size - 1, -1, -1):
            local_max = max(nums[i], nums[i] + local_max)
            
            global_max = max(global_max, local_max)
            
        return global_max
        