class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.findPosition(nums,target,True)
        fail = [-1,-1]
        if first == -1:
            return fail
        return [first,self.findPosition(nums,target,False)]        
        
        
    def findPosition(self,nums: List[int], target: int, isFirst : bool) -> List[int]:
        left = 0 
        right = len(nums) -1
        best = -1
        while left<=right:
            mid = left + (right -left)//2
            if nums[mid] > target:
                right = mid -1
            elif nums[mid] < target:
                left =  mid + 1
            else:
                if isFirst:
                    right = mid - 1
                elif not isFirst:
                    left = mid + 1
                best = mid
                
        return best
                
        
        