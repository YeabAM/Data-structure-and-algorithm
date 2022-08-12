class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        backward = nums[::-1]
        
        for i in range(1, len(nums)):
            backward [i] = (backward[i-1] or 1) * backward[i]
            nums[i] = (nums[i-1] or 1) * nums[i] 
            
        return max(max(backward), max(nums))