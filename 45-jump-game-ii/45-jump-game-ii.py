class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        count = 1
        jump = nums[0]
        _max = 0
        for i in range(1, len(nums)):
            if jump == 0:
                jump += _max
                count += 1
                _max = 0
            jump -= 1
            
            if jump + i >= len(nums) - 1:
                break

            if nums[i] - jump > _max:
                _max = nums[i] - jump   
                
        return count