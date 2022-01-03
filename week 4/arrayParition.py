class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        pairs = []
        minSum = 0
        nums.sort()
        
        for i in range(0,len(nums),2):
            pairs.append([nums[i],nums[i+1]])
        for i in range(len(pairs)):
            minSum += min(pairs[i][0], pairs[i][1])
        return minSum