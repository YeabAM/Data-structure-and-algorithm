class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallestTill = [0 for _ in range(len(nums))]
        largestTill = [0 for _ in range(len(nums))]
        
        smallestTill[0] = nums[0]
        largestTill[-1] = nums[-1]
        
        for i in range(1, len(nums)):
            smallestTill[i] = min(smallestTill[i-1], nums[i])
            
        for j in range(len(nums) - 2, -1, -1):
            largestTill[j] = max(largestTill[j+1], nums[j])
            
        
        for k in range(len(nums)):
            # print(k, smallestTill[k], nums[k], largestTill[k])
            if smallestTill[k] < nums[k] < largestTill[k]:
                return True
        
        return False
        
        