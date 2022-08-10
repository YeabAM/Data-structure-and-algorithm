class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        dp = set([0])
        target = sum(nums) // 2
        
        for num in nums:
            newDp = set()
            
            for value in dp:
                #this is knapsack dp with two options of whether to take the current value into the sum or not
                #that is ensured by adding the first 0 in the main dp set
                newDp.add(value + num)
                newDp.add(value)
            
            
            dp = newDp
            
            
        # print(dp, target)    
        return target in dp