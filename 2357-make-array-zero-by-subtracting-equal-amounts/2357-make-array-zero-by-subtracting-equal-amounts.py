class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        postives = set()
        
        for num in nums:
            if num != 0:
                postives.add(num)
                
        return len(postives)
                    
            
            
                
        