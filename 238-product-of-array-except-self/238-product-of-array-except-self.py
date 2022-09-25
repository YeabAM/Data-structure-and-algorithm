class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [0 for _ in range(len(nums) + 1)]
        backward = [0 for _ in range(len(nums))]
        forward[0] = 1
        backward[-1] = nums[len(nums) - 1]
        result = []
        
        for i in range(1, len(nums)+1):
            forward[i] = forward[i-1] * nums[i-1]
            
        for i in range(len(nums)-2, -1, -1):
            backward[i] = backward[i+1] * nums[i]
            
        backward.append(1)   
        # print(forward, backward)
        
        for i in range(1, len(forward)):
            result.append(forward[i-1] * backward[i])
            
        return result
            
        