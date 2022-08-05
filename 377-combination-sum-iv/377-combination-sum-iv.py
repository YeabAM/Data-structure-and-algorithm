class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def backt(summ):
            if summ == target:
                return 1
            if summ > target:
                return 0
            if summ in memo:
                return memo[summ]
            count = 0   
            
            for num in nums: 
                if summ + num <= target:
                    count += backt(summ + num)
                    
        
            memo[summ] = count        
            return memo[summ]  
        
        
        return backt(0)
        