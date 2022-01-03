class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        sortNums = []
        oddIndice = 1
        evenIndice = 0
        mid = n // 2
        for i in range(mid):
            sortNums.insert(oddIndice,nums[i])
            oddIndice += 2
        for i in range(mid,n):
            sortNums.insert(evenIndice,nums[i])
            evenIndice += 2     
        return sortNums
                    
                
            
        
        