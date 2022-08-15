class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if mid < len(nums) - 1 and nums[mid] == nums[mid + 1]:
                mid = mid + 1
                
            if (mid == 0 or nums[mid - 1] < nums[mid]) and (mid == len(nums) - 1 or \
            nums[mid] < nums[mid + 1]):
                return nums[mid]
            
            elif mid % 2 == 0:
                r = mid - 1
            
            else:
                l = mid + 1
                
        
        return nums[mid]
                
                
            
                
                    
                    
        