class Solution:
    def targetIndices(self, nums: List[int], target: int) :
        indice=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                indice.append(i)
        return indice