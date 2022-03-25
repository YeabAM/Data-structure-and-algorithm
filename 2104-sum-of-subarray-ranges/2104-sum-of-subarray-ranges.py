class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        
        for i in range(len(nums)):
            maxm = float("-inf")
            minm = float("inf")
            for j in range(i,len(nums)):
                maxm = max(maxm, nums[j])
                # print("mx", maxm)
                minm = min(minm, nums[j])
                # print("mn", minm)
                
                ans += (maxm - minm)
                # print("tot", ans)
        return ans
                
        