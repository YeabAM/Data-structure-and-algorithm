class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        maxJump = float('-inf')
        
        for i in range(len(nums)):
            print(i + nums[i])
            maxJump = max(maxJump, i + nums[i])
            if maxJump >= len(nums) - 1:
                return True
            
            if nums[i] == 0 and maxJump <= i:
                return False
            
    
        return maxJump >= len(nums) - 1
            
            
            
            
                    
            
                
            
            
        
        
            