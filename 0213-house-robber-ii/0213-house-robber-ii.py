class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        
        def houseRobbed(index, bound):
            if index > bound:
                return 0
            
            if index in memo:
                return memo[index]
            
            memo[(index)] = max(nums[index] + houseRobbed(index + 2, bound), houseRobbed( index + 1, bound))
            return memo[(index)]
        
        memo = {}
        FirstHouseRobbed = houseRobbed(0, len(nums) - 2)
        
        memo.clear()
        LastHouseRobbed = houseRobbed(1, len(nums) - 1)
        
        return max(FirstHouseRobbed, LastHouseRobbed)
        