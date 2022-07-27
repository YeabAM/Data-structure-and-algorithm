class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left= 0
        summ = 0
        size = float("inf")
        
        for i in range(len(nums)):
            summ += nums[i]
            
            while (summ >= target):
                size = min(size, i - left + 1)
                summ -= nums[left]
                left += 1
                
        return size if size != float("inf") else 0
            
            
                
        