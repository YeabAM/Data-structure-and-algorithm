class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
            changedValues = 0

            def revert(beg):
                l = beg
                r = len(nums) - 1
                
                while l < r:
                    if nums[r] <= nums[l]:
                        nums[l], nums[r] = nums[r], nums[l]
                    r -= 1
                    l += 1
                    
            def findminGreater(value):
                temp = len(nums) - 1
                
                while nums[temp] <= value:
                    temp -= 1
                        
                return temp
                        

            for i in range(len(nums)-1,0,-1):
                currVal = nums[i]

                if nums[i] > nums[i-1]:
                    pos = findminGreater(nums[i-1])
                    print(pos)
                    nums[pos], nums[i-1] = nums[i-1], nums[pos]
                    revert(i)
                    return nums
                    
                    
            revert(0)


            
        