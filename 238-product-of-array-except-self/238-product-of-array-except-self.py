class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [nums[0]]
        backward = [nums[-1]]
        result = []
        for i in range (1, len(nums)):
            forward.append(nums[i] * forward[i-1])
            
        for i in range(len(nums) - 2,-1,-1):
            backward.append(nums[i] * backward[-1])
            
        backward = backward[::-1]
        
        result.append(backward[1])
        
        for i in range(1, len(nums) - 1):
            result.append(forward[i - 1] * backward[i + 1])
            
        result.append(forward[-2])
        
        return result
        