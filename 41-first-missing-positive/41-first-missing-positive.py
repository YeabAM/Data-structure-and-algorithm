class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = 0
                
        for i, num in enumerate(nums):
            
            index = abs(num) - 1
            
            if index >= 0 and index < len(nums):
                
                if nums[index] == 0:
                    nums[index] = -inf
                    
                elif nums[index] > 0:
                    nums[index] *= -1
                    
        for i, num in enumerate(nums):
            if num >= 0:
                return i + 1
            
        return len(nums) + 1

        
        