class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        for i in range (0,n):        
            for j in range (0,n-1):
                if nums[j] > nums[j + 1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        print (nums)
        """
        Do not return anything, modify nums in-place instead.
        """
        