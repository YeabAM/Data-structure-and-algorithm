class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        ans = 0
        prefix = [0 for i in range(n + 1)]
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + nums[i-1]
            
        if firstLen < secondLen:
            firstLen, secondLen = secondLen, firstLen
            
        for i in range(n - firstLen + 1):
            firstSum = prefix[i + firstLen] - prefix[i]
            
            for j in range(n - secondLen + 1):
                if (i <= j + secondLen-1 < i + firstLen) or (i <= j < i + firstLen):
                    continue
                secondSum = prefix[j + secondLen] - prefix[j]
                ans = max(ans, firstSum + secondSum)
        return ans