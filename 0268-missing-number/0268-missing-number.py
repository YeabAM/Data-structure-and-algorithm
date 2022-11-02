class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        missingValue = 0
        total = len(nums)
        for i in range(len(nums)):
            missingValue = missingValue ^ nums[i]
            total ^= i
            
        # print(total, missingValue)
            
        return (total ^ missingValue)
            
        
        