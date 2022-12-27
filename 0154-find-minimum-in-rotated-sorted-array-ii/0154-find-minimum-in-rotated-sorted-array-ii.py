class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        smallest = float('inf')
        
        while l <= r:
            mid = (r - l) // 2 + l
            smallest = min(smallest, nums[mid])
            
            if nums[mid] == nums[r]:
                r -= 1
                
            
            elif nums[mid] > nums[r]:
                l = mid + 1
                     
                
            else:
                r = mid - 1
                        
        return smallest
    
    

        