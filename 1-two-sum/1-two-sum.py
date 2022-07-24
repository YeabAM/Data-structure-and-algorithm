class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        pair = dict()
        
        for i, n in enumerate(nums):
            if n in pair:
                return [pair[n],i]
            else:
                pair[target-n] = i
            
                
            
                
                
        
        
                
            
            
            
        