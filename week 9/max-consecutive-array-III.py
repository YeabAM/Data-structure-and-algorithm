class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if nums.count(0) <= k:
            return len(nums)
        l = 0 
        r = 0
        countedZeros = 0
        maxCount = 0
        while r < len(nums):
            if nums[r] == 0 and countedZeros < k:
                r += 1
                countedZeros += 1
            elif nums[r] == 1:
                r += 1
            else:
                
                while nums[l] == 1:
                    l += 1
                countedZeros -= 1
                l += 1
            maxCount = max(maxCount , r - l)
        return maxCount