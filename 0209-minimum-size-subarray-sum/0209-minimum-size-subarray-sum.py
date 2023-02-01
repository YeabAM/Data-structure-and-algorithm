class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        size = float('inf')
        l = 0
        
        for r in range(len(nums)):
            total += nums[r]
            
            while total >= target:
                window = r - l + 1
                size = min(window, size)
                total -= nums[l]
                l += 1
                
        return size if size != float('inf') else 0
                
        
        