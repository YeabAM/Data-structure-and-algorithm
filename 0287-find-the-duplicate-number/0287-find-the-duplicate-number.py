class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] <= mid:
                r = mid - 1
                
            else:
                l = mid + 1
                
        return l