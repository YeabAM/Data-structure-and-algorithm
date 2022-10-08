class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ptr1 = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ptr1] , nums[i] = nums[i], nums[ptr1]
                ptr1 += 1
                
        return ptr1
                
        