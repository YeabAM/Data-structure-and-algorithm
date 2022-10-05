class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        find mid
        if mid is greater than its left and smaller than its right
            if the target is less than the mid
                bring right pointer to mid
            if target is greater than mid
                bring left to mid
        else
            do opposite to the above

        '''
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            # print(left, mid, right)
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1         
            else:
                
                if nums[mid] <= target <= nums[right]: 
                    left = mid + 1
                else:
                    right = mid - 1
        # print(left, right)
        return -1 if nums[right] != target else right
                
        