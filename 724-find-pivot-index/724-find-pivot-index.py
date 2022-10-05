class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = [0]
        PivotFound = False
        for i in range(len(nums)):
            prefixSum.append(nums[i] + prefixSum[-1])
        
        # print(prefixSum)
        for j in range(1, len(prefixSum)):
            # print(j)
            if prefixSum[j-1] == prefixSum[-1] - prefixSum[j]:
                return j - 1
        
        return -1
            
            