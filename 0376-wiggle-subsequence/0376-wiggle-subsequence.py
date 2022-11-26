class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        size = len(nums)
        
        up = [1 for _ in range(size)]
        down = [1 for _ in range(size)]
        
        for i in range(1, size):
            if nums[i] > nums[i-1]:
                up[i] = down[i-1] + 1
                down[i] = down[i-1]
                
            elif nums[i] < nums[i-1]:
                down[i] = up[i-1] + 1
                up[i] = up[i-1]
                
            else:
                up[i] = up[i-1]
                down[i] = down[i-1]
                
        
        return max(up[-1], down[-1])
        
        