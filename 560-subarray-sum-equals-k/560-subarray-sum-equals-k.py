class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        currSum = 0
        ans = 0
        
        for i in range(len(nums)):
            currSum += nums[i]
            target = currSum - k
            ans += count[target]
            count[currSum] += 1
            
        return ans
            
        
        