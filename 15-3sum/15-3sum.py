class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        
        for i  in range(len(nums)):
            if (i != 0 and nums[i] != nums[i-1]) or i == 0:
                target = 0 - (nums[i])
                dict = {}
                
                for j in range(i+1, len(nums)):
                    if nums[j] in dict:
                        result.add((nums[j],nums[i],target-nums[j]))

                    dict[target - nums[j]] = nums[j]
                
            
        return result
                    
                
        