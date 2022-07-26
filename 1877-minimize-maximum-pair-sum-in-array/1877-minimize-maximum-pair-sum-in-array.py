class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        
        print(nums)
        
        maxSum = float("-inf")
        
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            maxSum = max(maxSum, nums[l] + nums[r])
            
            l +=1
            r -= 1
            
        return maxSum