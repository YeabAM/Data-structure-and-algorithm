class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k %= l    
        arr = [0] * l
        
        for i, num in enumerate(nums):
            arr[(i+k) % l] = num
        
        for i, val in enumerate(arr):
            nums[i] = val
        
        
        
        
        