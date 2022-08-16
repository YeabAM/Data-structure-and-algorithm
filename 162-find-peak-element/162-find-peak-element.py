class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while l< r:
            mid = l+(r-l)//2
            if mid < r and nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid
        return l
        
        
        
        
        
        
        
#         nums = [-inf] + nums + [inf]
#         l, r = 0, len(nums) - 1
#         while l < r:
#             mid = l + (r - l) // 2
            
#             if mid > 0 and mid < len(nums) - 1:
#                 if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
#                     return mid 
                    
#                 if nums[mid - 1] > nums[mid]:
#                     right = mid 
                
#                 elif nums[mid] < nums[mid + 1]:
#                     l = mid + 1
                    
#             elif mid == 0:
                
#                 if nums[mid + 1] < nums[mid]:
#                     return mid
                
#                 return mid + 1
            
#             elif (mid == len(nums) - 1):
#                 if nums[mid - 1] < nums[mid]:
#                     return mid
                
#                 return mid - 1
            
                    
                    
#         # print(l, r)
                    
#         if l != len(nums) and (nums[l - 1] < nums[l]):
#             return l
        
#         return r
        
                
            
                    
                
                
        