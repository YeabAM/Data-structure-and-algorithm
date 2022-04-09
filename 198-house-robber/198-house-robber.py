class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[-1]
        elif len(nums) ==2:
            return max(nums)
        else:
            dp = [nums[0], nums[1]] 
            for i in range(2, len(nums)):
                inc = max(dp[:i-1])
                # print(inc)
                dp.append(nums[i] + inc)
                # print(dp)
                
            return max(dp[-1], dp[-2])
            
        