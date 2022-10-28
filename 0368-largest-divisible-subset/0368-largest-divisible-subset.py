class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        largest_subset = []
        memo = {}
        nums.sort()
        for i in range(len(nums)):
            curr_sub = self.findPossibleSubset(i, nums, memo)
            if len(largest_subset) < len(curr_sub):
                largest_subset = curr_sub
            
        return largest_subset
            
            
        
    def findPossibleSubset(self, index, nums, memo):
        if index == len(nums) - 1:
            return [nums[index]]
        
        if index in memo:
            return memo[index]
        
        runn_max = []
        
        for j in range(index + 1, len(nums)):
            
            if nums[index] % nums[j] == 0 or \
            nums[j] % nums[index] == 0:
                potential_sub = self.findPossibleSubset(j, nums, memo)
                # print(potential_sub, nums[index], "c")
                if len(potential_sub) > len(runn_max):
                
                    runn_max = potential_sub
                    
        memo[index] = runn_max + [nums[index]]
        return memo[index]
    
                
        