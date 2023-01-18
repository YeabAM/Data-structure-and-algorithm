class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #kadane algo
        global_max = float('-inf')
        local_max = 0
        global_min = float('inf')
        local_min = 0
        total = 0
        #normal subarray
        for i in range(len(nums)):
            local_max = max(nums[i], nums[i] + local_max)
            global_max = max(global_max, local_max)
            local_min = min(nums[i], nums[i] + local_min)
            global_min = min(global_min, local_min)
            
            total += nums[i]
            
        # all negatives   
        if total == global_min:
            return global_max
        
        else:
            return max(global_max, total - global_min)
            

            
            
        
        