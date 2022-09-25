class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = []
        total = 1
        backward = 1
        
        for i in range(len(nums)):
            total *= nums[i]
            forward.append(total)
            
        # print(forward)
        for i in range(len(nums) - 1, 0, -1):
            # print(forward[i])
            forward[i] = backward * forward[i-1]
            backward *= nums[i]
            
        forward[0] = backward    
        return forward
            
        