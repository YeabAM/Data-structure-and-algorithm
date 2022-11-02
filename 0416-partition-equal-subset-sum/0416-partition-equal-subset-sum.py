class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        
        if total % 2 == 1:
            return False
        memo = {}
        
        return self.findPoss(0, nums, 0, 0, total // 2, memo)
        
        
    def findPoss(self,index, nums,  sum1, sum2, target, memo):
        if sum1 > target or sum2 > target:
            return False
        
        if index == len(nums):
            return sum1 == sum2
        
        if (index, sum1, sum2) in memo:
            return memo[(index, sum1, sum2)]
            
        memo[(index, sum1, sum2)] = self.findPoss(index + 1, nums, sum1 + nums[index], sum2, target,memo) or\
    self.findPoss(index + 1, nums, sum1, sum2 + nums[index], target, memo)
    
        return memo[(index, sum1, sum2)]
        
        
            
            
        