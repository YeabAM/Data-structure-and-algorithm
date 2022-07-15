class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minimum = 1
        nums = set(nums)
        for n in nums:
            if n > 0 and n == minimum:
                minimum += 1
        # print(minimum)
              
        return minimum + 1 if minimum in nums else minimum
        
                

        
        