class Solution:
    def jump(self, nums: List[int]) -> int:
        maxJump = 0
        min_step = 0
        next_dest = 0
        
        for i in range(len(nums) - 1):
            maxJump = max(maxJump, i + nums[i])
            
            if i == next_dest:
                next_dest = maxJump
                min_step += 1
                
        return min_step
            
            
    
            
        